

-- Generating points from the trajectory linestring data so that
-- I can compare them with cells coordinates. 
-- Using ST_Within I can check which points are inside the grid cells and associate them with the cell. 
http://postgis.net/workshops/postgis-intro/spatial_relationships.html

SELECT ST_AsText(
   ST_PointN(
	  t.trajectory,
	  generate_series(1, ST_NPoints(d.trajectory))
   )) as TrajPoints
into table traj_points
FROM traj_table t; 			

-- experitmenting with st_within, to check points which are inside grid cells. To eventually store the cells and points in a seperate table.

-- putting data into new table to test

select st_astext(coordinates) as cell, st_astext(geom_point) as poi 
into table test_st_within_grid_02 
from cells, poi
limit 50


-- fixing polygon issues. first & last element of polygon should be same.

UPDATE public.cells
	SET grid_id=null, cell_names=null, coordinates=null;
	
-- Deleting previous data

DELETE FROM public.cells;

-- Imported data already, now setting srid.

update cells set coordinates = st_setsrid(coordinates, 4326)

-- inserted new stuff inside grid table.

INSERT INTO public.grids(
	grid_id, x_dim, y_dim)
	VALUES (108.0,2,3);

	
-- Retrieving points that are inside grid cells and associating them. 

-- ST_Within(geometry A , geometry B) returns TRUE if the first geometry is completely within the second geometry

select distinct cell_names, st_astext(geom_point), st_astext(coordinates)
  	from cells, poi
  	where st_within(geom_point, coordinates) 
	

-- Retrieving distinct grid_cells.

select distinct grid_cells from poi_cell_association;


-- Retrieving all points inside first grid cell i.e., C00

select poi
	from poi_cell_association
	where cell_names = 'C00'

-- Creating new cell table to avoid importing 'more data error.'	

 create table cells_01 (
 	cell_id serial primary key, -- Making id serial type helps in importing more data into the table. You can also leave column from the import.  
 	grid_id float references grids(grid_id),
 	cell_names text,
 	coordinates geometry 
)	


-- removing unneccasary stuff.
delete from cells_01
where cell_id >= 7

-- getting unique polygon.

select distinct st_astext(coordinates)
from cells_01


-- getting object trajectory:
select * from traj
where obj_id = 37


-- Adding more data into cells.

\\copy public.cells (grid_id, cell_names, coordinates) FROM 'C:/Users/saim/DOCUME~1/POI_CL~1/POSTGR~1/AREA_C~1.CSV' DELIMITER ',' CSV HEADER QUOTE '\"' ESCAPE '''';""

"C:\\Program Files (x86)\\pgAdmin 4\\v4\\runtime\\psql.exe" --command " "\\copy public.cells (grid_id, cell_names, coordinates) FROM 'C:/Users/saim/DOCUME~1/POI_CL~1/POSTGR~1/AREA_C~1.CSV' DELIMITER ',' CSV HEADER QUOTE '\"' ESCAPE '''';""
	

-- poi cell association from only one grid.

select poi_id, cell_id, grid_id
 from poi, cells
 where st_within(geom_point, coordinates) and grid_id = 216

-- poi cell association table

select poi_id, cell_id, grid_id into table poi_cell_association
  from poi, cells
  where st_within(geom_point, coordinates) and grid_id = 216

  
-- Checking distance stuff:

SELECT ST_Distance(
		ST_GeomFromText('POINT(43.775502 -79.521692)',4326),
		ST_GeomFromText('POINT(43.763545 -79.491160)', 4326)
	);

st_distance
0.032 -- which is around 3.2km. 

-- associating trajectories and POIs within 100m of each other.

select obj_id, traj_id, poi_id 
	from poi, traj
	where ST_DWithin(traj_path, geom_point, 0.001)
	order by obj_id;
	
-- stroing results in a traj_poi_association table.

select obj_id, traj_id, poi_id into table traj_poi_association
	from poi, traj 
	where ST_DWithin(traj_path, geom_point, 0.001)
	order by obj_id;
	

-- fetching unique trajectories from traj_poi_association.

select distinct traj_id 
 	from traj_poi_association
 	order by traj_id


-- running inner join from traj_poi_association on traj table to fetch traj paths.

select distinct tp.traj_id, tr.traj_id, st_astext(tr.traj_path) 
 	from traj_poi_association tp
	inner join traj tr on tp.traj_id = tr.traj_id
 	order by tp.traj_id
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	