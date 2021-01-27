class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # class를 print하면 타입이 나오기 때문에 만들어준다.
    def __str__(self):
        return "Title: {}, Author: {}. Pages: {}".format(self.title,self.author,self.pages)
    
    # 이건 왜있는지 잘 모르겠슴
    def __len__(self):
        return self.pages

b = Book("Python", "jose", 200)
print(b)        # Title: Python, Author: jose. Pages: 200
print(len(b))   # 200