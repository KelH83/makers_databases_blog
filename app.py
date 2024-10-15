from lib.database_connection import DatabaseConnection
from lib.post_repository import PostRepository
from lib.comment_repository import CommentRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/blog_table.sql")

# # Retrieve all posts
post_repository = PostRepository(connection)
posts = post_repository.all()

# # List them out
for post in posts:
    print(post)

# # Retrieve all comments
comment_repository = CommentRepository(connection)
comments = comment_repository.all()

# # List them out
for comment in comments:
    print(comment)