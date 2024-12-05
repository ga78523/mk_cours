class Chrono:
    "une classe pour représenter le temps mesuré en heures, minutes et secondes"
    def __init__(self, h, m, s):
        "le constructeur prend comme arguments temps, minutes et secondes"
        self.heures = h
        self.minutes = m
        self.secondes = s

    def display(self):
        """ affiche les heures, minutes, secondes"""
        return (str(self.heures) + "h" + str(self.minutes) + "m" + str(self.secondes) + "s") 

    def __str__(self):
        return (str(self.heures) + "h" + str(self.minutes) + "m" + str(self.secondes) + "s")

t = Chrono(12,23,56)
print(t)