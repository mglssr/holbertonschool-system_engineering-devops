-- Create a database named tyrell_corp.
CREATE DATABASE IF NOT EXISTS tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6 (
	name VARCHAR(256), 
	id INT
);
INSERT INTO nexus6 (name, id) VALUES ("Leon", 1);
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
