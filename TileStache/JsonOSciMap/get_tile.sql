CREATE OR REPLACE FUNCTION __get_json_tile(IN tilex bigint, IN tiley bigint, IN tilez integer, IN cache boolean DEFAULT true)
  RETURNS TABLE(tags hstore, geom text) AS
$BODY$
DECLARE
bbox geometry;
min float;
x float;
y float;
w float;
h float;
BEGIN
	-- tile to bounding box
	bbox := __ttb(tileX, tileY, tileZ, 0);
	
	x = xmin(bbox);
	y = ymin(bbox);
	w = 10000 / (xmax(bbox) - x);
	h = 10000 / (ymax(bbox) - y);
	
	return query select p.tags, st_asgeojson(st_snaptogrid(ST_TransScale(p.geom, -x, -y, w, h), 1)) from 
		(select p.tags, st_geomfromewkb(p.geom) geom from __get_tile(tilex, tiley, tilez, cache) p 
		) p where geometrytype(p.geom) != 'GEOMETRYCOLLECTION';


END;
$BODY$
  LANGUAGE plpgsql VOLATILE;