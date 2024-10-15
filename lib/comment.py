class Comment:
    def __init__(self, user_name, content, post_id):
        self.user_name = user_name
        self.content = content
        self.post_id = post_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"User:{self.user_name},Comment:{self.content}, Post ID:{self.post_id}"
