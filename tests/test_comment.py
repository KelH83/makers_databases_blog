from lib.comment import Comment

def test_comment_constructs():
    comment = Comment("Mango_lover_1", "Not a fan of Apples", 1)
    assert comment.user_name == "Mango_lover_1"
    assert comment.content == "Not a fan of Apples"
    assert comment.post_id == 1

def test_comment_format_nicely():
    comment = Comment("Mango_lover_1", "Not a fan of Apples", 1)
    assert str(comment) == "User:Mango_lover_1,Comment:Not a fan of Apples, Post ID:1"