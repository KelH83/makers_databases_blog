from lib.post import Post

def test_post_constructs():
    post = Post("Databases", "Info on how to build databases")
    assert post.title == "Databases"
    assert post.content == "Info on how to build databases"

def test_post_format_nicely():
    post = Post("Databases", "Info on how to build databases")
    assert str(post) == "Title:Databases,Content:Info on how to build databases"