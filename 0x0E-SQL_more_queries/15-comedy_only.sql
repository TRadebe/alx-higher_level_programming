-- Lists all Comedy shows from the database
-- Retrieves the show title from tv_shows table using INNER JOIN for corresponding genres
-- Results are sorted in ascending order by show title
SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_genres ON tv_shows.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
