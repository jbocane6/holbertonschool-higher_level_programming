-- Script that displays the average temperature (Fahrenheit)
-- by city ordered by temperature (descending).
SELECT city, AVG(city) AS avg_temp FROM temperatures ORDER BY AVG(city) DESC;
