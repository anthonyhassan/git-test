class Band():
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def names(self):
        print(f"{self.name} had a score of {self.score}")
    
r1=Band("John","20")
r2=Band("Kayode", "80")
r3=Band("Melissa", "90")
r4=Band("Kola", "45")

r1.names()
r2.names()
r3.names()
r4.names()


