-- script that lists all shows without the genre Comedy in the database
SELECT ts.title
FROM tv_shows ts
WHERE ts.id NOT IN (
	SELECT tsg.show_id
	FROM tv_genres tg
	JOIN tv_show_genres tsg
	ON tg.id = tsg.genre_id
	WHERE tg.name = 'Comedy'
)
ORDER BY ts.title ASC;
