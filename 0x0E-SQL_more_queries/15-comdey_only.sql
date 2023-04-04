-- list all Comedy genre associated with the tv shows
SELECT ts.title 
FROM tv_shows ts
JOIN tv_show_genres tsg
ON ts.id = tsg.show_id
JOIN tv_genres tg
ON tg.id = tsg.genre_id
WHERE tg.name  = "Comedy"
ORDER BY ts.title ASC;
