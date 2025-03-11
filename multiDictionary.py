import dictionary as d
import richWord as rw

dic=d.Dictionary()

class MultiDictionary:

    def __init__(self):
        pass

    def printDic(self, language):
        d.Dictionary.loadDictionary(language)
        print(d.Dictionary.printAll())
        #printa il dizionario di quella lingua

    def searchWord(self, words, language):
        # Caricamento del dizionario per la lingua specificata
        dic.loadDictionary(language)
        parole_rich = []
        # Iterare le parole fornite
        for parola in words:  # 'parola' si riferisce a ciascun elemento nella lista 'words'

            found = False

            parola_rich = rw.RichWord(parola)
            parole_rich.append(parola_rich)

            # Controllare se la parola è presente nel dizionario
            for p in dic.dict:
                if p == parola:
                    parola_rich.corretta = True  # Segnare la parola come corretta
                    found = True
                    break
            if not found:
                parola_rich.corretta = False  # Segnare la parola come errata

        return parole_rich
