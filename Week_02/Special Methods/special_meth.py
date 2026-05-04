class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
b = Book("2933" , "George Orwell")
print(b)
        

class Playlist:
    def __init__(self , songs):
        self.songs = songs
    def __len__(self):
        return len(self.songs)
    def __add__(self, other):
        return Playlist(self.songs + other.songs) 

p1 = Playlist(["Song1" , "Song2"])
p2  = Playlist(["Songs3"])

print(len(p1))
print(len(p1 + p2))

class Point:
    def __init__(self , x, y):
        self.x = x 
        self.y = y
    def __str__(self):
        return f"({self.x} , {self.y})"    
    def __add__(self, other):
        if not isinstance(other , Point):
            return NotImplemented
        return Point(self.x + other.x , self.y + other.y)
    
p1  = Point(2,4)   
p2 = Point(4,5)
print(p1+p2)

        