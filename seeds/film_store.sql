CREATE TABLE IF NOT EXISTS films (
id SERIAL PRIMARY KEY,
title TEXT,
genre TEXT,
release_year INT
);

TRUNCATE films RESTART IDENTITY;

INSERT INTO films (title, genre, release_year) VALUES ('Iron Man', 'Superhero', 2008);
INSERT INTO films (title, genre, release_year) VALUES ('Incredible Hulk', 'Superhero', 2008);
INSERT INTO films (title, genre, release_year) VALUES ('Shawshank Redemption', 'Drama', 1994);
INSERT INTO films (title, genre, release_year) VALUES ('Snatch ', 'Comedy', 2000);
INSERT INTO films (title, genre, release_year) VALUES ('Lord of the Rings The Return of the King ', 'Fantasy', 2003);
INSERT INTO films (title, genre, release_year) VALUES ('Forrest Gump', 'Drama', 1994);
