DROP TABLE IF EXISTS student;
CREATE TABLE student(
    id              serial PRIMARY KEY,
    first_name      char(50) NOT NULL,
    last_name       char(50) NOT NULL,
    age             integer NOT NULL,
    grade           char(1)
)