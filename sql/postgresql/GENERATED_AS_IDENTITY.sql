-- new constraint; The GENERATED AS IDENTITY constraint is the SQL standard-conforming variant of the good old SERIAL column.

CREATE TABLE color (
    color_id INT GENERATED ALWAYS AS IDENTITY,
    color_name VARCHAR NOT NULL
);
