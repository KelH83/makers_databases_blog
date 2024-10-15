from lib.comment_repository import CommentRepository
from lib.comment import Comment


def test_get_all_records(db_connection): 
    db_connection.seed("seeds/blog_table.sql") 
    repository = CommentRepository(db_connection)

    comments = repository.all() 

    assert comments == [
        Comment('Annie', 'What even is this?!', 1),
        Comment('Joe', 'Dogs are so much better!', 2),
        Comment('Zippy', 'you missed a few colours', 3)
    ]
