-- script that creates the database hbtn_0d_usa and the
-- table cities

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT AUTO_GENERATED PRIMARY KEY NOT NULL, state_id INT FOREIGN KEY NOT NULL, name VARCHAR(256) NOT NULL);
