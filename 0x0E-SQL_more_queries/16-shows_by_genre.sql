-- a script that lists all shows, and all genres linked to that show, from the database
SELECT ts.title, tg.name
FROM tv_shows ts
LEFT JOIN tv_show_genres tsg
ON ts.id = tsg.show_id
LEFT JOIN tv_genres tg
ON tg.id = tsg.genre_id
ORDER BY ts.title ASC, tg.name ASC;
