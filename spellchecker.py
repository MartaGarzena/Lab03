import time
import multiDictionary as md


class SpellChecker:

    def __init__(self):
        self.listaRich = None

    def handleSentence(self, txtIn, language):
        start_time=time.monotonic()
        chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
        for c in chars:
            txtIn = txtIn.replace(c, "")
        txtIn.lower()

        words = txtIn.split(" ")
        self.listaRich = md.MultiDictionary().searchWord(words, language)
        mystr = ""
        for r in self.listaRich:
            if not r.corretta:
                mystr += r._parola + "\n"

        end_time=time.monotonic()
        mystr += "\nTempo di esecuzione: " + str(end_time-start_time) + " secondi"
        return  mystr



    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n" +
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    pass
