# -*- coding: utf-8 -*-

def check_adulthood():
    ageCheck = int(input("Sag mal wie alt bist du eigentlich? "))
    law = input("Und bist du eigentlich in einem Land, wo man ab 18 als volljährig zählt? (ja/nein): ")
    if law == "ja":
        if ageCheck >= 18:
            adult = True
        else:
            adult = False
    else:
        if ageCheck >= 21:
            adult = True
        else:
            adult = False

    print("Volljährig:", adult)

    monthBirthday = int(input("In welchem Monat hast du Geburtstag? (1-12): "))
    monthCurrent = int(input("Ich habe meinen Kalender gerade nicht dabei, welchem Monat befinden wir und nochmal? (1-12): "))

    if monthBirthday >= monthCurrent:
        months_until_birthday = monthBirthday - monthCurrent
    else:
        months_until_birthday = 12 - (monthCurrent - monthBirthday)

    print(" Nice, in", months_until_birthday, "Monaten hast du Geburtstag. Solange ist das doch gar nicht")
    age_next = ageCheck + 1
    print("Du wirst dann", age_next, "Jahre alt.")

    if adult:
        horrormovie = input("Magst du Horrorfilme ab 18? (ja/nein): ")
        if horrormovie == "ja":
            print("Cool, dann viel Spaß beim nächsten Gruselfilm, ich selber mag Alien ganz gern ^^!")
        elif horrormovie == "nein":
            print("Alles gut, Horror ist nicht für jeden was, ich kann dir Ghibli Filme empfehlen.")
        else:
            print("Hmmm, das war irgendwie keine klare Antwort, versuch es nochmal.")
    else:
        print("Du bist noch nicht volljährig.")
        months_to_wait = (18 - ageCheck) * 12 - months_until_birthday
        print("Komm in", months_to_wait, "Monaten wieder, dann kannst du den Rest beantworten, viel Erfolg bis dahin!")

    print("Danke für's Mitmachen, bis zum nächsten mal!")

check_adulthood()
