print("Hallo, ich bin Adam!")


name = input("Wie heißt du? ")


print(f"Schön, dich kennenzulernen, {name}. Hm, der Name klingt irgendwie nach jemandem, der die ganze Zeit in der Pause über 'die einen' redet... -.-")


alter = input(f"Wie alt bist du, {name}? ")
print(f"Ah, {alter} Jahre, du bist genau im Alter, wo der Körper langsam aufhört zu tun, was du ihm sagst. Aber keine Sorge, du wirst es irgendwann schaffen, nicht mehr nach den '5 besten Tipps für den Rücken' zu suchen. -.-")


antwort = input(f"{name}, bist du Team Nutella mit Butter oder Team Nutella ohne Butter? (mit Butter/ohne Butter):")

if antwort.lower() == "mit butter":
    print("Ah, ein echter Nutella-mit-Butter-Fan. Ja, klar, das war ja auch nötig, damit du den Geschmack erträglicher machst...")
elif antwort.lower() == "ohne butter":
    print("Oh, Nutella pur, also doch die pure Schokolade, weil du wahrscheinlich denkst, es macht dich 'gesünder'. HAHAHAHA XD")
else:
    print("Das war keine gültige Antwort. Aber egal, ich hoffe, du hast trotzdem Spaß.")


print("\nAber Moment, jetzt mal ehrlich... Wie heißt du mit Nachnamen?")
name2 = input("Wie lautet dein Nachname?: ")


adam_name = "Adam Supercool-Smartass"
print(f"Ah, {name2}, ein interessanter Nachname! Aber hey, ich heiße eigentlich {adam_name}. Besserer Nachname, oder?")


print(f"{name} {name2}, hmmm dein voller Name klingt wie jemand, der immer den letzten Keks nimmt und dann noch so tut, als wüsste er nichts davon...")


print(f"Es war schön, mit dir zu sprechen, {name}. Aber bitte schreibe mir nie wieder O_O")
