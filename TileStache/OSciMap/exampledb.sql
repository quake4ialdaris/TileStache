-- create spatial ref for spherical mercator
INSERT INTO spatial_ref_sys (srid, auth_name, auth_srid, srtext, proj4text)VALUES (900913,'EPSG',900913,'PROJCS["WGS84 / Simple Mercator",GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS_1984", 6378137.0, 298.257223563]],PRIMEM["Greenwich", 0.0],UNIT["degree", 0.017453292519943295],AXIS["Longitude", EAST],AXIS["Latitude", NORTH]],PROJECTION["Mercator_1SP_Google"],PARAMETER["latitude_of_origin", 0.0],PARAMETER["central_meridian", 0.0],PARAMETER["scale_factor", 1.0],PARAMETER["false_easting", 0.0],PARAMETER["false_northing", 0.0],UNIT["m", 1.0],AXIS["x", EAST],AXIS["y", NORTH],AUTHORITY["EPSG","900913"]]','+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +no_defs');


CREATE OR REPLACE FUNCTION __get_tile(IN tilex bigint, IN tiley bigint, IN tilez integer, IN cache boolean DEFAULT true)
  RETURNS TABLE(id bigint, tags hstore, geom bytea) 
  LANGUAGE plpgsql VOLATILE AS
$BODY$
DECLARE
bbox geometry;
min float;
BEGIN
	-- tile to bounding box
	bbox := __ttb(tileX, tileY, tileZ, 6);
	-- pixel at zoomlevel
	min := __paz(tileZ);
	
	-- IF cache THEN
-- 		PERFORM true FROM tiles WHERE x = tileX AND y = tileY AND z = tileZ LIMIT 1;
-- 		IF found THEN
-- 			--RAISE NOTICE 'found % % %', tileX, tileY,  tileZ;
-- 			RETURN QUERY SELECT 1::bigint, tiles.tags, ST_AsEWKB(tiles.geom) 
-- 				FROM tiles 
-- 				WHERE  x = tileX AND y = tileY AND z = tileZ;
-- 			RETURN;
-- 		 END IF;
-- 	ELSE
-- 		DELETE FROM tiles WHERE x = tileX AND y = tileY AND z = tileZ;
-- 	END IF;

	RETURN QUERY SELECT 1::bigint, p.tags, st_asewkb(p.geom) FROM __get_tile_water_poly(bbox,min) p; 
END;
$BODY$;

CREATE OR REPLACE FUNCTION __get_tile_poi(IN tilex bigint, IN tiley bigint, IN tilez integer, IN cache boolean DEFAULT true)
  RETURNS TABLE(id bigint, tags hstore, geom bytea) 
  LANGUAGE plpgsql VOLATILE AS
$BODY$
DECLARE
bbox geometry;
min float;
BEGIN
	RETURN;
END;
$BODY$;


CREATE OR REPLACE FUNCTION __get_tile_water_poly(bbox geometry, pixel double precision)
  RETURNS TABLE (tags hstore, geom geometry) 
  LANGUAGE sql VOLATILE AS
$BODY$
SELECT  ('natural' => 'water'), ST_Buffer(ST_Collect(ST_SimplifyPreserveTopology(geom, 2*$2)), -$2,1) FROM 
	(SELECT (ST_Dump(ST_Union(ST_Buffer(ST_Intersection($1, geom),$2,1)))).geom AS geom FROM
		ne_10m_ocean
		WHERE geom && $1
	) p WHERE geometrytype(geom) = 'POLYGON' AND ST_Area(geom) > (20*$2^2);
$BODY$;

CREATE OR REPLACE FUNCTION __ttb(tilex bigint, tiley bigint, tilez integer, pixel integer)
  RETURNS geometry 
  LANGUAGE plpgsql IMMUTABLE AS
$BODY$
DECLARE
scaleFactor double precision = 20037508.342789244;
size integer = 256;
minLon double precision;
maxLon double precision;
minLat double precision;
maxLat double precision;
center double precision;
BEGIN
	tileX := tileX * size;
	tileY := tileY * size;
	center := (size << tileZ) >> 1;
		
	minLat := ((center - (tileY + size + pixel)) / center) * scaleFactor;
	maxLat := ((center - (tileY - pixel)) / center) * scaleFactor;

	minLon := (((tileX - pixel) - center) / center) * scaleFactor;
	maxLon := (((tileX + size + pixel) - center) / center) * scaleFactor;
	
	-- this prevents a rendering issue on low zoom-levels, need to investigate..
	scaleFactor := 20037500;

	-- limit to max coordinate range:
	minLon := least(minLon, scaleFactor);
	minLon :=  greatest(minLon, -scaleFactor);

	maxLon := least(maxLon, scaleFactor);
	maxLon :=  greatest(maxLon, -scaleFactor);

	minLat := least(minLat, scaleFactor);
	minLat :=  greatest(minLat, -scaleFactor);

	maxLat := least(maxLat, scaleFactor);
	maxLat :=  greatest(maxLat, -scaleFactor);
	
	RETURN ST_MakeEnvelope(minLon, minLat, maxLon, maxLat, 900913);	
	
END;
$BODY$;

CREATE OR REPLACE FUNCTION __paz(zoom integer)
  RETURNS double precision 
  LANGUAGE sql IMMUTABLE AS
$BODY$
 SELECT 20037508.342789244 / 256 / (2 ^ $1)
$BODY$;