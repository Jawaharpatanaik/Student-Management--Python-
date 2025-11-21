
CREATE DATABASE student_db;
USE student_db;

CREATE TABLE students(
 id INT AUTO_INCREMENT PRIMARY KEY,
 name VARCHAR(100),
 email VARCHAR(100),
 department VARCHAR(100)
);

CREATE TABLE attendance(
 id INT AUTO_INCREMENT PRIMARY KEY,
 student_id INT,
 status VARCHAR(20)
);

CREATE TABLE records(
 id INT AUTO_INCREMENT PRIMARY KEY,
 student_id INT,
 subject VARCHAR(100),
 marks INT
);
