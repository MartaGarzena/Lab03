import dictionary as d
import richWord as rw

dic = d.Dictionary()


class MultiDictionary:

    def __init__(self):
        pass

    def printDic(self, language):
        dic.loadDictionary(language)
        print(dic.printAll())

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

    def searchWordDichotomic(self, words, language):
        dic.loadDictionary(language)
        diz_ordinato = sorted(dic.dict)
        inizio = 0
        fine = len(diz_ordinato)

        parole_rich = []
        # Iterare le parole fornite
        for parola in words:
            # 'parola' si riferisce a ciascun elemento nella lista 'words'
            parola_rich = rw.RichWord(parola)
            found = False

            while inizio != fine:
                medio = inizio + int((fine - inizio) / 2)
                parola_corrente = diz_ordinato[medio]

                if parola_corrente == parola:
                    parola_rich.corretta = True  # Segnare la parola come corretta
                    found = True
                    break
                elif parola > parola_corrente:
                    inizio = medio + 1  # Cerca nella metà destra
                else:
                    fine = medio  # Cerca nella metà sinistra

            if not found:
                parola_rich.corretta = False
            # Parola non trovata

            parole_rich.append(parola_rich)

        return parole_rich
