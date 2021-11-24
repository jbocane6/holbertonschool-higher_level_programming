-- Script that displays the top 3 of cities temperature during July and August
-- ordered by temperature (descending).
SELECT TOP 3 city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC WHERE month = 7,8;
