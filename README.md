#Data Engineering Zoomcamp ♥️ 2026 Thanks for passing by. This is one of my 2026 target to get to know more about data. This is my cocooning place for studying data engineering zoomcamp organised by DataTalksClub

Question 1. Understanding Docker images
Run docker with the python:3.13 image. Use an entrypoint bash to interact with the container.

What's the version of pip in the image?

Step One:
docker run -it --entrypoint bash python:3.13
Step Two:
pip --version

Answer: 25.3

Question 2. Understanding Docker networking and docker-compose
Given the following docker-compose.yaml, what is the hostname and port that pgadmin should use to connect to the postgres database?

Answer: db:5432

Question 3. Counting short trips
For the trips in November 2025 (lpep_pickup_datetime between '2025-11-01' and '2025-12-01', exclusive of the upper bound), how many trips had a trip_distance of less than or equal to 1 mile?

SELECT COUNT(*)
FROM green_taxi_trips
WHERE lpep_pickup_datetime BETWEEN '2025-11-01' AND '2025-12-01'
AND trip_distance <= 1;

Answer: 8007

Question 4. Longest trip for each day
Which was the pick up day with the longest trip distance? Only consider trips with trip_distance less than 100 miles (to exclude data errors).

SELECT lpep_pickup_datetime
FROM green_taxi_trips
WHERE trip_distance < 100 order by trip_distance desc limit 1;

Answer: 2025-11-14

Question 5. Biggest pickup zone
Which was the pickup zone with the largest total_amount (sum of all trips) on November 18th, 2025?

SELECT "PULocationID", COUNT(*), "Zone"
FROM green_taxi_trips
left join taxi_zones on "PULocationID" = "LocationID"
WHERE lpep_pickup_datetime::date = DATE '2025-11-18'
GROUP BY "PULocationID" , "Zone" order by count(*)desc ;

Answer: East Harlem North
