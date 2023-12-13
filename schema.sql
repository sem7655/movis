--Cхема
CREATE SCHEMA IF NOT EXISTS content;

--Таблица film_work
CREATE TABLE IF NOT EXISTS content.film_work (
    filmwork_id uuid PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    creation_date DATE,
    rating FLOAT,
    type TEXT NOT NULL,
    created timestamp with time zone,
    modified timestamp with time zone
); 

--Таблица Person
CREATE TABLE IF NOT EXISTS content.Person (
    person_id uuid PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    created timestamp with time zone,
    modified timestamp with time zone
 );
 
 
 --Таблица Genre
 CREATE TABLE IF NOT EXISTS content.Genre (
    genre_id uuid PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created timestamp with time zone,
    modified timestamp with time zone
);

-- Таблица Genre_film_work
CREATE TABLE IF NOT EXISTS content.filmwork_Genre (
    filmwork_Genre uuid PRIMARY KEY,
    genre_id uuid NOT NULL,
    filmwork_id uuid NOT NULL,
    created timestamp with time zone
);

  
  
--Таблица Person_film_work
  CREATE TABLE IF NOT EXISTS content.filmwork_Person (
    filmwork_Person_id uuid PRIMARY KEY,
    filmwork_id uuid NOT NULL,
    person_id uuid NOT NULL,
    role VARCHAR(255),
    created timestamp with time zone
);
