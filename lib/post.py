class Post:
    def __init__(self, id, title, content, comments=[]):
        self.id = id
        self.title = title
        self.content = content
        self.comments = comments

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"ID:{self.id},Title:{self.title},Content:{self.content}"
