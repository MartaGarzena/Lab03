import time
import multiDictionary as md


class SpellChecker:

    def __init__(self):
        self.listaRich = None

    def handleSentence(self, txtIn, language):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split(" ")

        print("------------------------------")
        print("metodo 1 ")
        t1 = time.time()
        parole = md.MultiDictionary().searchWord(words, language)
        for parola in parole:
            if not parola.corretta:
                print(parola)
        t2 = time.time()
        print("Time elapsed " + str(t2 - t1))

        print("------------------------------")
        print("Using searchWordDichotomic")
        t3 = time.time()
        parole = md.MultiDictionary().searchWordDichotomic(words, language)
        for parola in parole:
            if not parola.corretta:
                print(parola)
        t4 = time.time()
        print("Time elapsed " + str(t4 - t3))

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


def replaceChars(txtIn):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        txtIn = txtIn.replace(c, "")
    return txtIn
