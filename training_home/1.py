class Movie :
    def __init__(self, title, director, year, genre) :
        self.title = title
        self.director = director
        self.year = year    
        self.genre = genre
        self.actors = []
    def add_actor(self, actor):
        self.actors.append(actor)
    def out(self):
        print(f'Movie: {self.title} \nDirector: {self.director} \nRelease Year: {self.year} \nGenre: {self.genre} \nActors: ')
        for actor in self.actors:
            print(" - " + actor)

d1 = Movie("Bones and all", "Luca", 2018, "romance")
d1.add_actor("Leo")
d1.add_actor("Timothee Chalamet")
d1.add_actor("Agnes Burrow")
d1.out()
d2 = Movie("Call me by your name", "Timotheee Chalamet", 2017, "Thriller")
d2.add_actor("Leonardo Dicaprio")
d2.add_actor("Oliver Elliot")
d2.add_actor("Anastasia Bobere")
d2.out()
# checking if merge works 