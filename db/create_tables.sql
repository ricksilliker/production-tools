-- Create Projects table.
CREATE TYPE project_type AS ENUM ('Commercial', 'Feature', 'Game', 'Software', 'Web');
CREATE TABLE project_items (
    id serial primary key,
    name text NOT NULL,
    code varchar(12) NOT NULL,
    image_uri text,
    project_type project_type NOT NULL,
    internal bool DEFAULT false
);