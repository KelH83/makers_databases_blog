## 1. Extract nouns from the user stories or specification

```
As a blogger
So I can write interesting stuff
I want to write posts having a title.
User > Post > Title

As a blogger
So I can write interesting stuff
I want to write posts having a content.
User > Post > Content

As a blogger
So I can let people comment on interesting stuff
I want to allow comments on my posts.
Others > Comment

As a blogger
So I can let people comment on interesting stuff
I want the comments to have a content.
Others > Comment > Content

As a blogger
So I can let people comment on interesting stuff
I want the author to include their name in comments.
Others > Comment > Name

```

```
Nouns:

Post, Title, Content, Comment, Content, Name, post_id
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                  | Properties                 |
| ---------------------   | ------------------         |
| Posts                   | title, content             |
| Comments                | content, user_name, post_id|


1. Name of the first table (always plural): `posts` 

    Column names: `title`, `content`

2. Name of the second table (always plural): `comments` 

    Column names: `content`, `user_name`, `post_id`

## 3. Decide the column types
```
# EXAMPLE:

Table: posts
id: SERIAL
title: text
content: text

Table: comments
id: SERIAL
content: text
user_name: text
post_id: foreign key
```

## 4. Decide on The Tables Relationship

1. **[posts] has many [comments]**
2. And on the other side, **[comments] belongs to [posts]**
3. In that case, the foreign key is in the table [comments]

Replace the relevant bits in this example with your own:

```
# EXAMPLE

1. Can one post have many comments? YES
2. Can one comment have many posts? NO

-> Therefore,
-> A post HAS MANY comments
-> A comment BELONGS TO a post

-> Therefore, the foreign key is on the comments table.
```
## 5. Write the SQL

```sql
-- EXAMPLE
-- file: blog_table.sql

-- Create the table without the foreign key first.
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title VARCHAR(250),
  content VARCHAR(500) --NEED TO CHECK FOR UNLIMITED LENGTHS
);

-- Then the table with the foreign key second.
CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  user_name VARCHAR(250),
  ucontent VARCHAR(500), --NEED TO CHECK FOR UNLIMITED LENGTHS
-- The foreign key name is always {other_table_singular}_id
  post_id int,
  constraint fk_post foreign key(post_id)
    references posts(id)
);

```

## 6. Create the tables

```bash
psql -h 127.0.0.1 blog < blog_table.sql
```