""" Provider that returns OpenScienceMap Tile data responses from our special PostGIS queries.

Note:
 
....

Keyword arguments:

  dsn:
    Database connection string suitable for use in psycopg2.connect().
    See http://initd.org/psycopg/docs/module.html#psycopg2.connect for more.
  
  
"""
import types
import TileData_pb2
from WKBParser import WKBParser
from StaticTags import getTags
from StaticKeys import getKeys
import logging
import struct
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
        
        data = self.content.SerializeToString()
        
        # zbuf = cStringIO.StringIO()
        # zfile = gzip.GzipFile(mode='wb', fileobj=zbuf, compresslevel=9)
        # zfile.write(data)
        # zout = zlib.compress(data, 9)    
        # logging.debug("serialized %s - %fkb <> %fkb" %(self.tile, len(data)/1024.0, len(zout)/1024.0))
        out.write(struct.pack(">I", len(data)))
        out.write(data)
        # zfile.close()
        # out.write(zbuf.getvalue())
        # out.write(self.content.SerializeToString())
    
class Provider:
    """
    """
    def __init__(self, layer, dsn):
        self.layer = layer
        self.dbdsn = dsn
        self.tileSize = 256
        self.query_tile = "SELECT tags, geom FROM __get_tile(%s,%s,%s)"
        self.query_tile_poi = "SELECT tags, geom FROM __get_tile_poi(%s,%s,%s)"
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
    
    def addItem(self, tile, row, coord, geomparser, tagdict):
        
        num_tags = 1024 + len(tagdict)
        statictags = getTags()
        statickeys = getKeys()
        wayTags = []
         
        for tag in row[0].iteritems():
            layer = 5
            # use unsigned int for layer. i.e. map to 0..10
            if "layer" == tag[0]:
                try:
                    l = max(min(10, int(tag[1])) + 5, 0)
                    if l != 0:
                        layer = l
                    continue
                except ValueError:
                    continue
            
            tag = self.fixTag(tag, coord.zoom)
            
            if tag is None:
                continue
            
            if statictags.has_key(tag):
                wayTags.append(statictags[tag])
                logging.debug('add static tag %s', tag)
            elif tagdict.has_key(tag):
                # add tag index to way data
                wayTags.append(tagdict[tag])
                logging.debug('add tag %s', tag)
            elif tag[0] in statickeys:
                # add tag string to tile data
                tile.keys.append(statickeys[tag[0]])
                tile.values.append(tag[1].decode('utf-8'))
                logging.debug('add tag: %d %s %s' % (statickeys[tag[0]], tag[0], tag[1]))
                
                #tile.tags.append(("%s=%s" % (tag[0], tag[1])).decode('utf-8'))
                
                # map tag => tile tag index
                tagdict[tag] = num_tags
                
                # add tag index to way
                wayTags.append(num_tags)
                num_tags += 1

        if len(wayTags) == 0:
            return
            
        geomparser.parseGeometry(row[1])
        way = None;
        
        if geomparser.isPoint:
            way = tile.points.add()
            # add number of points (for multi-point)
            if len(geomparser.coordinates) > 2:
                logging.info('points %s' %len(geomparser.coordinates))
                way.indices.add(geomparser.coordinates/2)                
        else:
            # empty geometry
            if len(geomparser.index) == 0:
                return
                
            if geomparser.isPoly: 
                way = tile.polygons.add() 
            else:  
                way = tile.lines.add()
        
            # add coordinate index list (coordinates per geometry)
            way.indices.extend(geomparser.index)
            
            # add indice count (number of geometries)
            if len(way.indices) > 1:
                way.num_indices = len(way.indices)
            
        # add coordinates 
        way.coordinates.extend(geomparser.coordinates)
        
        # add tags
        way.tags.extend(wayTags)                
        #if len(wayTags) > 1:
        #    way.num_tags = len(wayTags)
        
        logging.debug('tags %d, indices %d' %(len(wayTags),len(way.indices)))
    
        # add osm layer
        if layer != 5:
            way.layer = layer
            
    def renderTile(self, width, height, srs, coord):
        """ Render a single tile, return a SaveableResponse instance.
        """
        tilesize = 256 * 16
        
        # center pixel on zoomlevel
        center = (tilesize << coord.zoom) >> 1
        # maximum coordinate in web mercator
        f900913 = 20037508.342789244
        
        # pixel relative to global center
        dx = (coord.column * tilesize) - center
        # flip y-axis
        dy = center - (coord.row * tilesize + tilesize) 
        
        # size of one pixel 
        div = f900913 / center
        
        geomparser = WKBParser(dx, dy, div)
        
        conn = _connect(self.dbdsn)
        db = conn.cursor()
        register_hstore(conn, True, False)

        db.execute(self.query_tile, (coord.column * self.tileSize, coord.row * self.tileSize, coord.zoom))
        rows = db.fetchall()
        
        tile = TileData_pb2.Data()

        tagdict = {}
        
        for row in rows:
            # empty geometry
            if (row[0] is None) or (row[1] is None):
                continue
            
            self.addItem(tile, row, coord, geomparser, tagdict)
    
        db.execute(self.query_tile_poi, (coord.column * self.tileSize, coord.row * self.tileSize, coord.zoom))
        rows = db.fetchall()
        
        for row in rows:
            # empty geometry
            if (row[0] is None) or (row[1] is None):
                continue
            
            self.addItem(tile, row, coord, geomparser, tagdict)
            
        #db.close()
        tile.num_tags = len(tile.keys)
         
        try: 
            conn.commit()
        except Exception, e:
            logging.error(">>> %s", e)
            conn.rollback()
        
        conn.close()
        
        return SaveableResponse(tile, coord)

    
        
    def getTypeByExtension(self, extension):
        """ Get mime-type and format by file extension.

            This only accepts "osmtile" for the time being.
        """
        if extension.lower() == 'osmtile':
            return 'application/osmtile', 'OSMTile'


        raise KnownUnknown('OpenScienceMap Provider only makes ".osmtile", not "%s"' % extension)
