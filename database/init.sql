CREATE DATABASE IF NOT EXISTS production;

USE production;

CREATE TABLE users (
  id int,
  user_name varchar(50),
  PRIMARY KEY ( id )
);