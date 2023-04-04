-- a script that lists all genres from hbtn_0d_tvshows
-- and displays the number of shows linked to each.
-- First column must be called genre
-- Second column must be called number_of_shows
-- Don’t display a genre that doesn’t have any shows linked
-- Results must be sorted in descending order by the number of shows linked
SELECT tg.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres tg
JOIN tv_show_genres tsg
ON tg.id = tsg.genre_id
GROUP BY tsg.genre_id
ORDER BY number_of_shows DESC;
