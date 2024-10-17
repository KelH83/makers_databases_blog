from lib.post import Post
from lib.comment import Comment

class PostRepository:
    def __init__(self, connection):
        self._connection = connection
        
    def all(self):
        rows = self._connection.execute('SELECT * from posts')
        posts = []
        for row in rows:
            item = Post(row["id"],row["title"], row["content"])
            posts.append(item)
        return posts
    
    def find_all_comments(self, post_id):
        rows = self._connection.execute("SELECT posts.id AS post_id, posts.title,posts.content, comments.user_name,comments.content AS comment_content, comments.id AS comment_id "  
        "FROM posts JOIN comments ON posts.id = comments.post_id "
        "WHERE posts.id = %s", 
        [post_id])

        comments = []
        for row in rows:
            comment = Comment(row['user_name'],row["comment_content"],row["post_id"])
            comments.append(comment)

        return Post(rows[0]["post_id"],rows[0]["title"], rows[0]["content"], comments)
        