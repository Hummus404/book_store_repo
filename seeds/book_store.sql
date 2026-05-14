-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
-- DROP TABLE IF EXISTS books;

-- Then, we recreate them

-- no longer need to create table as we are just resetting values with truncate now. truncate just removes all entries in a table. i learnt RESTART IDENTITY which should reset the id to 0 
CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title text,
    author text
);

TRUNCATE TABLE books RESTART IDENTITY;

-- Finally, we add any records that are needed for the tests to run
INSERT INTO books (title, author) VALUES ('Learning Python', 'Umut Can');
INSERT INTO books (title, author) VALUES ('Databases in a Nutshell', 'Hunter Khalil');
INSERT INTO books (title, author) VALUES ('HTML for Newbies', 'Mia Jade');
INSERT INTO books (title, author) VALUES ('The Art of SQL & Postgresql', 'Hunter Khalil');
INSERT INTO books (title, author) VALUES ('Turkish Food Recipes', 'Mia Jade');
