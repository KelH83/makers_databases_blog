from lib.post_repository import PostRepository
from lib.post import Post
from lib.comment import Comment


def test_get_all_records(db_connection): 
    db_connection.seed("seeds/blog_table.sql") 
    repository = PostRepository(db_connection)

    posts = repository.all() 

    assert posts == [
        Post(1,'Apple VS Samsung', 'Which phone to get in 2024'),
        Post(2,'My favourite pet', 'My cat Twyla is clearly the best out of all my pets'),
        Post(3,'Rainbow', 'Red, Yellow, Pink, Green, etc etc')
    ]

def test_get_all_comments_on_a_post(db_connection):
    db_connection.seed("seeds/blog_table.sql") 
    repository = PostRepository(db_connection)

    all_comments = repository.find_all_comments(2)

    assert all_comments == Post(2, "My favourite pet", "My cat Twyla is clearly the best out of all my pets", [
        Comment('Joe', 'Dogs are so much better!', 2)
    ])