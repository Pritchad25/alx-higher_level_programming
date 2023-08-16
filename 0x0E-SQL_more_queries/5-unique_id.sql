-- Unique ID
-- A script that creates the table on the MySQL Server.
-- The script will not fail if the table already exists.
CREATE TABLE IF NOT EXISTS unique_id
       (id INT DEFAULT 1,
       UNIQUE (ID),
       name VARCHAR(256));
