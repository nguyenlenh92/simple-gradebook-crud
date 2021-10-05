-- Initialize the database.
-- Drop any existing data and create empty tables and populate with test data.

DROP TABLE IF EXISTS student_table;

CREATE TABLE student_table (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  student_name TEXT NOT NULL,
  student_id TEXT NOT NULL,
  student_points INTEGER
);

INSERT INTO student_table (student_name, student_id, student_points)
VALUES ('Steve Smith', '211', '80'),
('Jian Wong', '122', '92'), 
('Chris Peterson', '213', '91'),
('Sai Patel', '524', '94'),
('Andrew Whitehead', '425', '99'),
('Lynn Roberts', '626', '90'),
('Robert Sanders', '287', '75');
