-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on the hbnb_dev_db database to the hbnb_dev user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on performance_schema to the hbnb_dev user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Apply the privilege changes
FLUSH PRIVILEGES;
