-- Generating points from the trajectory linestring data so that
-- I can compare them with cells coordinates. 
-- Using ST_Within I can check which points are inside the grid cells and associate them with the cell. 
http://postgis.net/workshops/postgis-intro/spatial_relationships.html

SELECT ST_AsText(
   ST_PointN(
	  t.trajectory,
	  generate_series(1, ST_NPoints(d.trajectory))
   )) as TrajPoints
into table traj_point
FROM traj_table t; 			
