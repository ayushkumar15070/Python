class Person:
    def __init__(self, name, ):
        self.name = name

    def greet(self):
        print("Hello" + self.name)

p1 = Person("John")
print(p1.name)


class Calculator:
    def addition(seld, a, b):
        return a + b

    def subtraction(self, a, b):
        if a < b:
            return b - a
        else:
            return a - b


c1 = Calculator()

print(c1.addition(23, 44))
print(c1.subtraction(5, 23))



class person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"


p1 = person("Ayush", 20)
print(p1)

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"Added-{song}")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"removed-{song}")

    def show_song(self):
        print(f"Playlist - {self.name}")
        for i in self.songs:
            print(f"- {i}")


playlist_name = input("Enter your playlist name: ")

myplaylist = Playlist(playlist_name)

while True:
    addsong = input("Want to add songs: ")        
    if addsong.lower() == "yes":
        howmany = int(input("How many songs you want to add: "))
        for i in range(0, howmany):
            entersong = input("Enter your song name: ")
            myplaylist.add_song(entersong)
    else:
        break

myplaylist.show_song()

removesong = input("Want to remove songs: ")
if removesong.lower() == "yes":
    howmnay = int(input("How many songs you want to remove: "))
    for i in range(0, howmany):
        songwhichyouwanttoremove = input("Enter the song name which you want to remove: ")
        if songwhichyouwanttoremove in myplaylist.songs:
            myplaylist.remove_song(songwhichyouwanttoremove)


myplaylist.show_song()

