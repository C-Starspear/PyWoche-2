import time

fragen = [
    "Was ist deine Lieblingsfarbe?",
    "Wie lautet deine Lieblingsserie?",
    "Was ist dein Lieblingstier?",
    "Wie gefällt dir das ADA BootCamp?",
    "Was machst du am Liebsten in deiner Freizeit?",
    "Wenn du eine Superkraft haben könntest, welche wäre es?",
    "Welche Jahreszeit magst du am meisten?",
    "Findest du Regen gut oder schlecht?",
    "Was ist dein Lieblingsessen?",
    "Zockst du gerne? Wenn ja was ist dein Maingame?"
]

i = 0
while i < 10:
    print("Frage:", fragen[i])
    print("Du hast 30 Sekunden Zeit, darüber nachzudenken.")
    
    sekunden = 30
    while sekunden > 0:
        print("Noch", sekunden, "Sekunden", end="\r")
        time.sleep(1)
        sekunden -= 1

    antwort = input("\nJetzt antworte: ")
    print(antwort,",Tolle Antwort ^^")
    i += 1

print("Deine Antworten werden nicht gespeichert! Vielen Dank fürs mitmachen C: ")
