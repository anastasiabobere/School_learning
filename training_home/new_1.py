class Video_Game:
    def __init__(self, title, genre, platform):
        self.title = title
        self.genre = genre
        self.platform = platform
        self.multiplayer = True
        self.ratings = []

    def add_rating(self, rating):
        self.ratings.append(rating)

    def toggle_Multiplayer(self):
        self.multiplayer = not self.multiplayer 

    def __str__(self):
        return f'Spēle {self.title} ir {self.genre} žanra {"multiplayer" if self.multiplayer else "single-player"} spēle uz {self.platform}. Atsauksmes: {", ".join(self.ratings) if self.ratings else "Nav atsauksmju"} '

game = Video_Game("Minecraft", "survival", "PC")
game.add_rating("Forši")
game.add_rating("Aizraujoši")
game.add_rating("Not good")
print(game)

game2 = Video_Game("Sims 4", "simulator", "XBOX")
game2.toggle_Multiplayer()
game2.add_rating("Cool")
game2.add_rating("Boringgg")
game2.add_rating("Good")
print(game2)
