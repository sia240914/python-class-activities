class book :
    def __init__(self,id,name,author):
        self.id=id
        self.name=name
        self.author=author
    def details (self):
        print("  book id is:",self.id )
        print("  book name is:",self.name )
        print("  book author is:",self.author )

class ebook (book):
    def __init__(self,id,name,author,file_size):
        super().__init__(id,name,author)
        self.file_size=file_size
        
    def ebook_details (self):
        self.details()
        print("file size is :",self.file_size)


b1=book(149982,"harry Potter","J.K Rowling")

b1.details()

b2=ebook(998213,"diary of a wimpy kid","Jeff Kinney","7mb")

b2.ebook_details()


