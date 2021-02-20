CREATE TYPE project_type AS ENUM (
    'Commercial', 'Feature', 'Game', 'Software', 'Web'
);
CREATE TYPE department_code AS ENUM (
    'Art', 'Rigging', 'Lighting', 'Animation'
);
CREATE TYPE status_code AS ENUM (
    'Ready To Start',
    'In Progress',
    'Complete',
    'Hold',
    'Blocked',
    'Omit'
);
CREATE TYPE work_item_type AS ENUM (
    'Asset',
    'Shot'
);
CREATE TYPE version_type AS ENUM (
    'Review',
    'Work',
    'Publish',
    'Vendor'
);
CREATE TYPE review_status AS ENUM (
    'Standby',
    'Next Up',
    'In Review',
    'Review Complete'
);
CREATE TYPE file_type AS ENUM (
    'Source',
    'Image',
    'Movie',
    'Cache',
    'Archive',
    'Documentation',
    'Delivery',
    'Resource',
    'Client'
);
CREATE TYPE rating_code AS ENUM (
    'A', 'B', 'C'
);
CREATE TYPE pass_status AS ENUM (
    'Approved',
    'Approved With Tweak',
    'Internal',
    'Client Review',
    'Phase 1',
    'Phase 2'
);
CREATE TYPE os_type AS ENUM (
    'Windows',
    'MacOS',
    'Linux'
);

-- Create Projects table.
CREATE TABLE project_items (
    id serial NOT NULL PRIMARY KEY,
    name text NOT NULL,
    code varchar(12) NOT NULL,
    image_uri text,
    project_type project_type NOT NULL,
    internal bool DEFAULT false
);

-- Create WorkItems table.
CREATE TABLE work_items (
    id serial NOT NULL PRIMARY KEY,
    type work_item_type NOT NULL
);

-- Create Assets table.
CREATE TABLE asset_items (
    id int NOT NULL PRIMARY KEY REFERENCES work_items,
    code varchar(24) NOT NULL,
    project_id int REFERENCES project_items,
    tags text[],
    image_uri text
);

-- Create Shots table.
CREATE TABLE shot_items (
    id int NOT NULL PRIMARY KEY REFERENCES work_items,
    code varchar(24) NOT NULL,
    project_id int REFERENCES project_items,
    cut int[2],
    buffer_frames int,
    movie_uri text,
    asset_list json
);

-- Create Users table.
CREATE TABLE users (
    id serial NOT NULL PRIMARY KEY,
    first_name text NOT NULL,
    last_name text NOT NULL,
    login text NOT NULL,
    password text NOT NULL
);

-- Create Tasks table.
CREATE TABLE task_items (
    id serial NOT NULL PRIMARY KEY,
    name text NOT NULL,
    status status_code DEFAULT 'Ready To Start',
    assignee_id int REFERENCES users,
    reviewer_id int REFERENCES users,
    department department_code NOT NULL,
    link_id int REFERENCES work_items,
    project_id int REFERENCES project_items,
    description varchar(120),
    priority int DEFAULT 1,
    start_date timestamp,
    due_date timestamp,
    started_at timestamp,
    completed_at timestamp
);

-- Create Versions table.
CREATE TABLE version_items (
    id serial NOT NULL PRIMARY KEY,
    task_id int NOT NULL,
    file_id int NOT NULL,
    type version_type NOT NULL,
    review_status review_status NOT NULL DEFAULT 'Standby',
    number int,
    descriptor varchar(12),
    preview_uri text
);

-- Create ProjectFiles table.
CREATE TABLE project_file_items (
    id serial NOT NULL PRIMARY KEY,
    path_uri text NOT NULL,
    type file_type NOT NULL,
    name text NOT NULL,
    size int NOT NULL,
    created_at timestamp NOT NULL,
    created_by int REFERENCES users NOT NULL
);

-- Create ScheduleEntryItems table.
CREATE TABLE schedule_entry_items (
    id serial NOT NULL PRIMARY KEY,
    task_id int NOT NULL REFERENCES task_items,
    bid float,
    estimated_effort float,
    actual_effort float,
    current_pass pass_status,
    rating rating_code
);

-- Create ScheduleItems tables.
CREATE TABLE schedule_items (
    id serial NOT NULL PRIMARY KEY,
    name text,
    entries int[]
);

-- Create Software table.
CREATE TABLE software_items (
    id serial NOT NULL PRIMARY KEY,
    display_name text,
    category varchar(24),
    linux_path text,
    windows_path text,
    mac_path text
);

-- Create Hardware table.
CREATE TABLE hardware_items (
    id serial NOT NULL PRIMARY KEY,
    os os_type NOT NULL,
    distro varchar(24) NOT NULL,
    version varchar(24) NOT NULL,
    cpu text,
    gpu text[],
    ram text[],
    storage text[],
    accessories text[],
    software int[]
);