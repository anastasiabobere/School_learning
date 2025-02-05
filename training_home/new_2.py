class Musician:
    def __init__(self, name, genre, instrument):
        self.name = name
        self.genre = genre
        self.instrument = instrument
   
class Solomusician(Musician):
    def __init__(self, name, genre, instrument, albums):
        super().__init__(name, genre, instrument)
        if not isinstance(albums, int):
            raise ValueError("Albums must be an integer")
        self.albums = albums

    def __str__(self):
        return f"Musician {self.name} plays {self.instrument} in the {self.genre} genre and has {self.albums} albums."

class Group(Musician):
    def __init__(self, name, genre, instrument, members):
        super().__init__(name, genre, instrument)
        if not isinstance(members, int):
            raise ValueError("Members must be an integer")
        self.members = members

    def __str__(self):
        status = "ir instrument" if self.instrument else "nav instrumenta"
        return f"Grupa: {self.name}, Žanrs: {self.genre}, Dalībnieku skaits: {self.members}. {status} {self.instrument}"

class DJ(Musician):
    def __init__(self, name, genre, instrument, aprikojums):
        super().__init__(name, genre, instrument)
        self.aprikojums = aprikojums

    def __str__(self):
        status = "ir instrument" if self.instrument else "nav instrumenta"
        return f"DJ: {self.name}, Žanrs: {self.genre}, Aprikojums: {self.aprikojums}. {status} {self.instrument}"

musicians = [ 
    Solomusician("Billie Eilish", "pop", "voice", 2),
    Group("Imagine Dragons", "rock", "guitar", 4),
    DJ("David Guetta", "house", "DJ", "Mixer"),
    Solomusician("Eminem", "rap", "voice", 10),
    Group("The Beatles", "rock", "guitar", 4),
    DJ("Martin Garrix", "house", "DJ", "Mixer"),
    Solomusician("Ariana Grande", "pop", "voice", 3),
    Group("Queen", "rock", "guitar", 4),
    Solomusician("Ed Sheeran", "pop", "guitar", 4),
    Group("Coldplay", "rock", "guitar", 4),
]

for musician in musicians:
    print(musician)
    print("-----------------")

class Concert:
    def __init__(self, name):
        self.name = name
        self.musicians = []
        self.sold_out = False

    def add_musician(self, musician):
        self.musicians.append(musician)
    
    def all(self):
        return len(self.musicians)

    def ir_moderns(self):
        self.moderns = any(isinstance(musician, DJ) for musician in self.musicians)

    def izvade(self):
        print(f"Koncerts {self.name}")
        print("Mūziķi:", ", ".join(musician.name for musician in self.musicians))
        print(f"Koncerts {'ir moderns' if self.moderns else 'nav moderns'}")
        print(f"Kopējais mūziķu skaits: {self.all()}")

concert1 = Concert("Riga")
concert1.add_musician(musicians[0])
concert1.add_musician(musicians[1])
concert1.add_musician(musicians[2]) 

concert1.ir_moderns()
concert1.izvade()
