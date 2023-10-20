-- list all genres not linked to the show dexter
-- The tv_shows table contains only one record where title =  Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the MySQL commad
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN
(SELECT tv_shows.id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.shows_id
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = "Comedy")
ORDER BY tv_shows.title;
