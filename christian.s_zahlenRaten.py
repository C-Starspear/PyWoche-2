import random

print("Arrr, willkommen an Bord, du seetaugliche Landratte!")
print("Ich bin Käpt’n Krabs, und ich habe einen Schatz voller Gold!")
print("Errate die geheime Zahl zwischen 1 und 100, und der Schatz gehört dir.")
print("Du hast 6 Versuche. Verlierst du, bleibt mein Schatz MEIN Schatz! Har-har-har!\n")


geheime_zahl = random.randint(1, 100)


versuche = 6


for runde in range(1, versuche + 1):
    print(f"Versuch {runde} von {versuche}:")
    tipp = int(input("Welche Zahl wählst du, du möchtegern Seebär? "))

    if tipp < geheime_zahl:
        print("Zu niedrig, du übergewichtiger Planktonfresser! Har-har-har!\n")
    elif tipp > geheime_zahl:
        print("Zu hoch, mein Jung! So hoch springt nur SpongeBob, wenn er 'nen Gehaltsscheck sieht! Har-har-har!\n")
    else:
        print(f"Arrr, das ist korrekt! Die Zahl war {geheime_zahl}. Na schön, du hast gewonnen, aber ich werde den Verlust aus deinem Gehalt abziehen! Har-har-har!")
        break
else:

    print(f"Har-har-har! Du verlierst, ich kassiere!! Die geheime Zahl war {geheime_zahl}. Jetzt verschwind, bevor ich dir 'nen Job im Krosse Krabbe anbiete!")
