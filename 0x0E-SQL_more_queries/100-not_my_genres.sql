-- Import the database dump from hbtn_0d_tvshows to the MySQL server from this address: 
-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- Script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different).
-- Each record should display: tv_genres.name.
-- Results must be sorted in ascending order by the genre name.
-- You can use a maximum of two SELECT statement.
-- The database name will be passed as an argument of the mysql command.
SELECT DISTINCT name FROM tv_show_genres
INNER JOIN tv_shows	ON tv_show_genres.show_id = tv_shows.id
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name NOT IN
(
	SELECT DISTINCT name FROM tv_show_genres
	INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
	INNER JOIN tv_shows	ON tv_show_genres.show_id = tv_shows.id
	WHERE tv_shows.title = 'Dexter'
)
ORDER BY tv_genres.name;