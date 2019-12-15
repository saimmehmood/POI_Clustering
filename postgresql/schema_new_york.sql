 
 
 create table poi_ny(
	poi_enum serial primary key,
  	poi_id text,  -- this key is fetched from the data retrieved from Google Places API.
  	geom_point geometry -- I'm adding POINT inside the datasets using python script. Just mentioning it as "geometry(POINT, 4326)" doesn't work.
 )

 update poi_new_york set geom_point = st_setsrid(geom_point, 4326)

 create table real_traj (
  	traj_id serial primary key,  
 	traj_path geometry -- Adding LINESTRING in the data column through notepad++
  )

 update real_traj set traj_path = st_setsrid(traj_path, 4326) 

create table cells_new_york (
	cell_id serial primary key,  -- changed to serial in cell_01
	grid_id float references grids(grid_id),
	cell_names text,
	coordinates geometry  -- Creating POLYGON geometry: need to specify first and last coordinate same for each of them. 
)

update cells_new_york set coordinates = st_setsrid(coordinates, 4326) 



-- This query misses the revisited polygons by the same trajectory (new query written further).

  SELECT traj_id, cell_id, cell_names into table traj_as_cells_ny
  FROM   (
    SELECT tr.traj_id, ce.cell_id, ce.coordinates, ce.grid_id, 
           ST_LineLocatePoint(tr.traj_path, ST_Centroid(ce.coordinates)) AS frac
    FROM   cells_new_york AS ce
    JOIN   real_traj AS tr
      ON   ST_Intersects(ce.coordinates, tr.traj_path)
  	where ce.grid_id = 1225
  ) q
  ORDER BY
         frac
  ; 


-- cell_poi_ny contains cell ids and poi ids for the POIs that are inside cell coordinates.

 select c.cell_id, p.poi_enum into table cell_poi_ny
   from poi_ny p, cells_new_york c
   where st_within(p.geom_point, c.coordinates) and grid_id = 1225
   order by c.cell_id
   
   
-- Getting the above cell coordinates that contains POI. (Doing visualization)
 
select cp.cell_id, st_astext(cn.coordinates)
	from cell_poi_ny cp, cells_new_york cn
	where cp.cell_id = cn.cell_id
	

-- Getting poi's value from poi_new_york based on their ids from cell_poi_new_york 

select cp.poi_id, st_astext(pn.geom_point)
	from cell_poi_new_york cp, poi_new_york pn
	where cp.poi_id = pn.poi_id

-- Storing traj_id and poi_id based on if they are part of the same cell.
	
select tn.traj_id, cp.poi_enum into table traj_as_poi_ny
	from traj_as_cells_ny tn, cell_poi_ny cp
	where tn.cell_id = cp.cell_id 	

-- Getting traj poi's from traj_as_poi table and poi table.
select tp.traj_id, tp.poi_id, st_astext(pn.geom_point) as points
 	from traj_as_poi_ny tp, poi_ny pn
 	where tp.poi_id = pn.poi_id	
	
	
-- Getting cells and pois inside those cells through which trajectory is passing. 

select tp.traj_id, st_astext(pn.geom_point) as point, st_astext(tr.traj_path) as traj_path, tc.cell_id, st_astext(tc.coordinates) as coordinates
  	from traj_as_poi_new_york tp, poi_new_york pn, real_traj tr, traj_as_cells_ny tc
  	where tp.poi_id = pn.poi_id and tp.traj_id = tr.traj_id and tp.traj_id = tc.traj_id and tp.traj_id = 560	
	
	
*** POIs = 559
***	Traj = 100


-- Getting traj_ids and cell_ids of the cells from which traj is passing through. (Considering single traj id)


SELECT tr.traj_id, ce.cell_id, ce.grid_id
FROM cells_new_york ce, real_traj tr
where ce.grid_id = 9 and tr.traj_id = 572

ORDER BY ST_LineLocatePoint(
    tr.traj_path,
    ST_CENTROID(
        (ST_DUMP(
            ST_Intersection(ce.coordinates, tr.traj_path)
        )).geom
    )
);

-- storing traj_as_cells for 1000 real new york trajectories. (with 35 * 35 grid).

SELECT tr.traj_id, ce.cell_id into table traj_as_cells_ny_1000
FROM cells_new_york ce, real_traj_1000 tr
where ce.grid_id = 1225 -- and tr.traj_id = 550 and tr.traj_id = 511 -- and tr.traj_id = 513

ORDER BY ST_LineLocatePoint(
    tr.traj_path,
    ST_CENTROID(
        (ST_DUMP(
            ST_Intersection(ce.coordinates, tr.traj_path)
        )).geom
    )
);

-- fetching traj related stuff

-- all traj's passing through cell
select tr.traj_id, st_astext(r.traj_path)
	from traj_as_cells_ny_1000 tr, real_traj_1000 r
	where tr.cell_id = 1729 and tr.traj_id = r.traj_id

-- Getting cell coordinates
select cell_id, st_astext(coordinates)
from cells_new_york 
where cell_id = 1729

-- the above query for traj_as_cells shows multiple cell_ids for trajectory self intersection

--  for avoiding repetitions of grid cells which contains self intersections of a trajectory

WITH t1 AS (
  SELECT tr.traj_id, ce.cell_id,
  ST_LineLocatePoint(
      tr.traj_path,
      ST_CENTROID(
          (ST_DUMP(
              ST_Intersection(ce.coordinates, tr.traj_path)
          )).geom
      )
  ) AS distance
  FROM cells_porto ce, porto_traj_1000 tr
	where tr.traj_id = 860
),

t2 AS (
  SELECT t1.traj_id, t1.cell_id,
  COALESCE(LEAD(t1.cell_id) OVER(ORDER BY t1.traj_id, t1.distance), -1) AS next_cell_id
  FROM t1
)

SELECT t2.traj_id, t2.cell_id
FROM t2
WHERE t2.cell_id <> t2.next_cell_id
;

-- for all trajectories
WITH t1 AS (
  SELECT tr.traj_id, ce.cell_id,
  ST_LineLocatePoint(
      tr.traj_path,
      ST_CENTROID(
          (ST_DUMP(
              ST_Intersection(ce.coordinates, tr.traj_path)
          )).geom
      )
  ) AS distance
  FROM cells_porto ce, porto_traj_1000 tr
-- 	where tr.traj_id = 860
),

t2 AS (
  SELECT t1.traj_id, t1.cell_id,
  COALESCE(LEAD(t1.cell_id) OVER(ORDER BY t1.traj_id, t1.distance), -1) AS next_cell_id
  FROM t1
)

SELECT t2.traj_id, t2.cell_id into table traj_as_cells_porto
FROM t2
WHERE t2.cell_id <> t2.next_cell_id
;


























