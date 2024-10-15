from lib.post_repository import PostRepository
from lib.post import Post


def test_get_all_records(db_connection): 
    db_connection.seed("seeds/blog_table.sql") 
    repository = PostRepository(db_connection)

    posts = repository.all() 

    assert posts == [
        Post('Apple VS Samsung', 'Which phone to get in 2024'),
        Post('My favourite pet', 'My cat Twyla is clearly the best out of all my pets'),
        Post('Rainbow', 'Red, Yellow, Pink, Green, etc etc')
    ]
