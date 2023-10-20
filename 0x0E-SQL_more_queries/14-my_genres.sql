-- lists all genres of the show Dexter.
-- The tv_shows table contains only one record where title = Dexter (but id should be diffarent)
-- Each record should display: tv_genres.name
--  Results must be sorted in ascending order by the genre name
-- you can use only one select statement
-- The database name will be passed as argument of the MySQL command

SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = "Dexter"
ORDER BY tv_genres.name;
