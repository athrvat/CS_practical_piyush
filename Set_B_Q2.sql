-- Create a student table
CREATE TABLE student (
    student_id INT PRIMARY KEY,
    name VARCHAR(255),
    marks INT
);

-- Insert details of a new student
INSERT INTO student (student_id, name, marks) VALUES (1, 'John Doe', 90);

-- Delete details of a student
DELETE FROM student WHERE student_id = 1;

-- Select details of students with marks more than 80
SELECT * FROM student WHERE marks > 80;

-- Display various modifications of the 'name' column
-- Display names in capital letters
SELECT UPPER(name) FROM student;

-- Display names in small letters
SELECT LOWER(name) FROM student;

-- Display first 3 letters of the name
SELECT LEFT(name, 3) FROM student;

-- Display last 3 letters of the name
SELECT RIGHT(name, 3) FROM student;

-- Display the position of the letter 'A' in the name
SELECT LOCATE('A', name) AS position_of_A FROM student;

-- Remove extra spaces from the text
-- Remove extra spaces from both sides
SELECT TRIM(' ' FROM ' Informatics Practices Class XII ');

-- Remove extra spaces from left side
SELECT LTRIM(' ' FROM ' Informatics Practices Class XII ');

-- Remove extra spaces from right side
SELECT RTRIM(' ' FROM ' Informatics Practices Class XII ');

-- Display various date-related information for today's date
SELECT
    DAYNAME(NOW()) AS day_name,
    MONTHNAME(NOW()) AS month_name,
    DAY(NOW()) AS day,
    DAYNAME(NOW()) AS day_name,
    DAYOFMONTH(NOW()) AS day_of_month,
    DAYOFYEAR(NOW()) AS day_of_year;
