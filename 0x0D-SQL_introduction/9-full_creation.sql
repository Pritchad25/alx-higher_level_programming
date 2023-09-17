-- Full creation
-- A script that creates a table called second_table in the
-- database called hbtn_0c_0 in the MySQL Server and adds
-- multiple rows.
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
-- The script will create 4 records in the table.
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, "John", 10);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (2, "Alex", 3);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (3, "Bob", 14);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (4, "George", 8);
