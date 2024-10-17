from lib.post import Post

def test_post_constructs():
    post = Post(1,"Databases", "Info on how to build databases")
    assert post.id == 1
    assert post.title == "Databases"
    assert post.content == "Info on how to build databases"

def test_post_format_nicely():
    post = Post(1,"Databases", "Info on how to build databases")
    assert str(post) == "ID:1,Title:Databases,Content:Info on how to build databases"