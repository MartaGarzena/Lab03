import os
class Dictionary:



    def __init__(self):
        self._dizionarietto = []

    def loadDictionary(self, path):


        myfile = open(path, "r")
        for line in myfile:
            line = line.strip()
            self._dizionarietto.append(line)

    def printAll(self):
        mystr = ""
        for e in self._dizionarietto:
            mystr += e + "\n"
        return mystr

    @property
    def dict(self):
        return self._dizionarietto
    #funziona da getter

