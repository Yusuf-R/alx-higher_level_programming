-- a script that creates a table with and unique field
CREATE TABLE IF NOT EXIST unique_id (
id INT DEFAULT 1 UNIQUE,
name VARCHAR(256)
);
