DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title VARCHAR(250),
  content TEXT
);

CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  user_name VARCHAR(250),
  content TEXT,
  post_id int,
  constraint fk_post_id foreign key(post_id)
    references posts(id)
    on delete cascade
);


INSERT INTO posts (title, content) VALUES ('Apple VS Samsung', 'Which phone to get in 2024');
INSERT INTO posts (title, content) VALUES ('My favourite pet', 'My cat Twyla is clearly the best out of all my pets');
INSERT INTO posts (title, content) VALUES ('Rainbow', 'Red, Yellow, Pink, Green, etc etc');

INSERT INTO comments (user_name, content, post_id) VALUES ('Annie', 'What even is this?!', 1);
INSERT INTO comments (user_name, content, post_id) VALUES ('Joe', 'Dogs are so much better!', 2);
INSERT INTO comments (user_name, content, post_id) VALUES ('Zippy', 'you missed a few colours', 3);