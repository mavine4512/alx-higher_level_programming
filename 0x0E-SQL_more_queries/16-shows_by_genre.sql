-- lists all comedy shows in the database hbtn_0d_tyshows.
-- The tv_genres table contains only one record where name = comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Result must be sorted in ascending order by the slow title
-- You can use only one select statement
-- The database name will be passed as an argument of the MySQL command

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
INNER JOIN tv_show§_genres
ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name;
