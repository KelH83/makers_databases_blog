class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Title:{self.title},Content:{self.content}"
