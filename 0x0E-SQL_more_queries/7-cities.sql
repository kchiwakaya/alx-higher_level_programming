-- create a table in server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- set database to new DB
USE hbtn_0d_usa;
-- create table if doesnt exist
CREATE TABLE IF NOT EXISTS cities(
  id INT PRIMARY KEY AUTO_INCREMENT,
  state_id INT NOT NULL,
  name VARCHAR(256) NOT NULL,
  FOREIGN KEY (state_id) REFERENCES states(id)
);
