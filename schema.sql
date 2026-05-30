
CREATE TABLE events(
 id SERIAL PRIMARY KEY,
 event_type VARCHAR(50),
 track_id INT,
 camera_id VARCHAR(50),
 event_time TIMESTAMP
);
