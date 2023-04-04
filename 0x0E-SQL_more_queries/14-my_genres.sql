-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter 
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
SELECT tg.name
FROM tv_shows ts
JOIN tv_show_genres tsg
ON ts.id = tsg.show_id
JOIN tv_genres tg
ON tg.id = tsg.genre_id
WHERE ts.title = 'Dexter'
ORDER BY tg.name ASC;
