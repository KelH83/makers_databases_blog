from lib.comment import Comment

class CommentRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from comments')
        comments = []
        for row in rows:
            item = Comment(row["user_name"], row["content"], row["post_id"])
            comments.append(item)
        return comments