-- The name of the new user should be replica_user
CREATE USER IF NOT EXISTS 'replica_user'@'%'IDENTIFIED BY 'maiu';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
