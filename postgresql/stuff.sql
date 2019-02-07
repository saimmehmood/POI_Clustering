create Table driving_01 (
id integer primary key,
distance text,
time text,
trajectory text)

ALTER TABLE driving_01 ALTER COLUMN trajectory TYPE Geometry(POINT, 4326) USING ST_SetSRID(trajectory::Geometry,4326);

select st_astext(geom)
from poi_latlong

select st_astext(d.trajectory), st_astext(p.geom) 
from poi_latlong p, driving d 
where st_dwithin(d.trajectory, p.geom, 0.0000001)



