import spellchecker

sc = spellchecker.SpellChecker()

while True:
    sc.printMenu()

    txtIn = input()
    if not txtIn.isdigit() or int(txtIn) < 1 or int(txtIn) > 4:
        print("Inserisci un numero tra 1 e 4\n")
        continue
    # Add input control here!

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        sc.handleSentence(txtIn, "Italian.txt")
        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        sc.handleSentence(txtIn, "./resources/English.txt")

        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        sc.handleSentence(txtIn, "Spanish.txt")  # non funziona

        continue

    if int(txtIn) == 4:
        break
