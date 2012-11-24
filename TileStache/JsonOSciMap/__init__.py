""" Provider that returns OpenScienceMap Tile data responses from our special PostGIS queries.

Note:
 
A Standard osm2pgsql import can be used as source. The Database requires the functions
'__get_tile(x,y,z)' and '__get_tile_poi(x,y,z)' which return columns of 'tags' as hstore
and geometries as ewkb ('geom'). Geometries need to be clipped to tile boundary 
(plus a few pixel offset).

Keyword arguments:

  dsn:
    Database connection string suitable for use in psycopg2.connect().
    See http://initd.org/psycopg/docs/module.html#psycopg2.connect for more.
  
Example Configuration:
  "map": 
    {
        "provider": 
        { 
               "class": "TileStache.OSciMap:Provider",
                "kwargs": 
                { 
                            "dsn": "dbname=gis user=osm password=osm" 
                            "query_tile": "SELECT tags, geom FROM __get_tile(%s,%s,%s,false)",
                            "query_poi": "SELECT tags, geom FROM __get_tile_poi(%s,%s,%s)"
                }
        }
    }
"""
import types
import logging
import struct
import json

try:
    from json import JSONEncoder
except ImportError:
    from simplejson import JSONEncoder

try:
    from psycopg2 import connect as _connect
    from psycopg2.extras import register_hstore
    from psycopg2.pool import ThreadedConnectionPool
except ImportError:
    # At least it should be possible to build the documentation.
    pass


from TileStache.Core import KnownUnknown
import gzip
import cStringIO
import zlib

#import sys
#sys.setdefaultencoding("utf-8")                    # a hack to support UTF-8

class SaveableResponse:
    """ Wrapper class for OpenScienceMapTile response that makes it behave like a PIL.Image object.
    
        TileStache.getTile() expects to be able to save one of these to a buffer.
    """
    def __init__(self, content, tile):
        self.content = content
        self.tile = tile

    def save(self, out, format):
        if format != 'OSMTile':
            raise KnownUnknown('OpenScienceMap provider only saves .osmtile tiles, not "%s"' % format)
        
        out.write(self.content)
#         
#        for atom in self.content:
#            out.write(atom)
#       
    
class Provider:
    """
    """
    def __init__(self, layer, dsn, query_tile = None, query_poi = None):
        self.layer = layer
        self.dbdsn = dsn
        self.tileSize = 256
        
        #if query_tile == None:
        #self.query_tile = "SELECT tags, st_asgeojson(ST_TransScale(st_geomfromewkb(geom))) FROM __json_tile(%s,%s,%s)"
        self.query_tile = "SELECT tags, geom FROM __get_json_tile(%s,%s,%s)"
        #else: 
        #    self.query_tile = query_tile
            
        #self.query_tile_poi = "SELECT tags, geom FROM __get_tile_poi(%s,%s,%s)"
        self.query_exists = "SELECT true FROM tiles WHERE x=%s AND y=%s AND z=%s"
        #self.pool = ThreadedConnectionPool(10,50,dsn)
        #register_hstore(None, True, False, 267)
 
    # fix tags from looking things up in wiki where a value should be used with a specific key,
    # i.e. one combination has a wiki page and more use in taginfo and the other does not
    # TODO add:
    # natural=>meadow
    # landuse=>greenhouse,public,scrub
    # aeroway=>aerobridge
    # leisure=>natural_reserve
    
    def fixTag(self, tag, zoomlevel):
        drop = False
         
        if tag[1] is None:
            drop = True
        
        key = tag[0].lower();
        
        if key == 'highway':
            # FIXME remove ; separated part of tags
            return (key, tag[1].lower().split(';')[0])
            
        if key == 'leisure':
            value = tag[1].lower();
            if value in ('village_green', 'recreation_ground'):
                return ('landuse', value)
            else:
                return (key, value)
                
        elif key == 'natural':
            value = tag[1].lower();
            if zoomlevel <= 9 and not value in ('water', 'wood'):
                return None
            
            if value in ('village_green', 'meadow'):
                return ('landuse', value)
            if value == 'mountain_range':
                drop = True
            else:
                return (key, value)
                
        elif key == 'landuse':
            value = tag[1].lower();
            if zoomlevel <= 9 and not value in ('forest', 'military'):
                return None
            
            # strange for natural_reserve: more common this way round...
            if value in ('park', 'dog_park', 'natural_reserve'):
                return ('leisure', value)
            elif value == 'field':
                # wiki: Although this landuse is rendered by Mapnik, it is not an officially 
                # recognised OpenStreetMap tag. Please use landuse=farmland instead.
                return (key, 'farmland')
            elif value in ('grassland', 'scrub'):
                return ('natural', value)
            else:
                return (key, value)
        
        elif key == 'oneway':
            value = tag[1].lower();
            if value in ('yes', '1', 'true'):
                return (key, 'yes')
            else: 
                drop = True
        
        elif key == 'area':
            value = tag[1].lower();
            if value in ('yes', '1', 'true'):
                return (key, 'yes')
            # might be used to indicate that a closed way is not an area
            elif value in ('no'):
                return (key, 'no')
            else: 
                drop = True
                
        elif key == 'bridge':
            value = tag[1].lower();
            if value in ('yes', '1', 'true'):
                return (key, 'yes')
            elif value in ('no', '-1', '0', 'false'):
                drop = True
            else:
                return (key, value)
            
        elif key == 'tunnel':
            value = tag[1].lower();
            if value in ('yes', '1', 'true'):
                return (key, 'yes')
            elif value in ('no', '-1', '0', 'false'):
                drop = True
            else:
                return (key, value)
            
        if drop:
            logging.debug('drop tag: %s %s' % (tag[0], tag[1]))
            return None
        
        return tag
    
    def addItem(self, tile, row, coord):
        pass
        
            
    def renderTile(self, width, height, srs, coord):
        """ Render a single tile, return a SaveableResponse instance.
        """
#        tilesize = self.tileSize * 16
#        
#        # center pixel on zoomlevel
#        center = (tilesize << coord.zoom) >> 1
#        # maximum coordinate in web mercator
#        f900913 = 20037508.342789244
#        
#        # pixel relative to global center
#        dx = (coord.column * tilesize) - center
#        # flip y-axis
#        dy = center - (coord.row * tilesize)
#        
#        # size of one pixel 
#        div = f900913 / center
#        
        
        conn = _connect(self.dbdsn)
        db = conn.cursor()
        register_hstore(conn, True, False)

        db.execute(self.query_tile, (coord.column * self.tileSize, coord.row * self.tileSize, coord.zoom))
        rows = db.fetchall()
        logging.debug(self.query_tile)
        
        bbox = 0
        tile = {"bbox": bbox, "granularity":10000, "features":[]}
        features = []
        for row in rows:
            # empty geometry
            if (row[0] is None) or (row[1] is None):
                continue
            
            #logging.debug(str(row[1]))
            
            geojson = json.loads(str(row[1]))
#            tags = {}
#            for tag in row[0].iteritems():
#                tags[tag[0]] = ("%s" %(tag[1])).decode('utf-8')
#            
#            print tags
#            
#            geojson["properties"] = tags

            geojson["properties"] = row[0]

            features.append(geojson)
   
        tile["features"].extend(features)
    
        try: 
            conn.commit()
        except Exception, e:
            logging.error(">>> %s", e)
            conn.rollback()
        
        conn.close()
        
        #encoded = JSONEncoder().iterencode(tile)
        #print encoded
         
        callback = "onKothicDataResponse"
        encoded = callback + "(" + json.dumps(tile, True, ensure_ascii=True, separators=(',', ':')) + ",%s,%s,%s);" % (coord.zoom, coord.column, coord.row)
        
        #data = bytes(data)
        
        #logging.debug(data)
        
        return SaveableResponse(encoded, coord)

    
        
    def getTypeByExtension(self, extension):
        """ Get mime-type and format by file extension.

            This only accepts "osmtile" for the time being.
        """
        if extension.lower() == 'osmtile':
            return 'application/osmtile', 'OSMTile'


        raise KnownUnknown('OpenScienceMap Provider only makes ".osmtile", not "%s"' % extension)
