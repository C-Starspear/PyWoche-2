# -*- coding: utf-8 -*-
def start_game():
    print("Willkommen zu deinem Abenteuer!")
    print("\nDu merkst, wie kalte Regentropfen auf dein Gesicht fallen und du wachst auf. Du bemerkst, dass du an einem unbekannten Ort bist, allein bei Nacht und durchnässt vom Regen. Du gehst durch den vorderen Wald. Du findest einen Weg, der sich bald in zwei Richtungen aufspaltet. Aber dir geht es immer schlechter.")
    print("\nDer 1. Weg führt nach links und ist mit Laternen beleuchtet. Etwas weiter siehst du kleine Häuser. Der 2. Weg führt tiefer in den Wald, ohne Beleuchtung. Du hörst nur noch einen Schrei aus dieser Richtung.")

    choice = input("Welchen Weg möchtest du gehen? (1 oder 2): ")

    if choice == "1":
        print("\nDu gehst nach links und folgst dem beleuchteten Weg zu den kleinen Häusern. Auf dem Weg dahin merkst du, wie die Kälte dich langsam packt, aber du schaffst es noch bis zum ersten Haus.")
        print("\nAm Haus angekommen, merkst du erst, dass es dir gar nicht mehr gut geht. Egal wo du gerade gelandet bist, dir geht es sehr schlecht. Dir ist kalt und du bist komplett durchnässt. Deine einzige Chance ist es, schnell ins Warme zu kommen.")

        choice = input("Klopfst du an die Tür des ersten Hauses oder gehst du weiter? (an die Tür klopfen oder weiter gehen): ")

        if choice.lower() == "an die Tür klopfen":
            print("Eine große, grüne Kreatur öffnet die Tür. Keine 2 Sekunden später liegst du tot auf dem Boden. Was passiert ist, erfahren wir vielleicht im nächsten Game.")
        elif choice.lower() == "weiter gehen":
            print("\nDu gehst ein paar Schritte weiter, doch du schaffst es nicht bis zum nächsten Haus. Du stirbst an Kälte und Regen.")
        else:
            print("Das ist keine gültige Wahl. Du stirbst sofort. Das Spiel endet hier.")
            start_game()  # Neustart bei ungültiger Eingabe

    elif choice == "2":
        print("\nDu gehst nach rechts in den Wald und kommst dem Schrei immer näher, bis du bemerkst, dass es nur ein komisch aussehender Vogel ist, der einen todesähnlichen Schrei von sich gibt. Doch du bemerkst auch, dass es schon wieder zwei Wege gibt.")
        print("\nDer erste Weg führt in eine Höhle, die nicht gerade einladend aussieht, aber dir zumindest Schutz vor Regen und Wind bieten würde. Der andere Weg führt auf eine offene Wiese.")

        choice = input("Wohin gehst du? (Höhle oder Wiese): ")

        if choice.lower() == "höhle":
            print("\nDu gehst in die Höhle und bemerkst, wie es immer wärmer wird. Plötzlich springt etwas hinter dich und hält dir eine Streitaxt an deine Kehle... Fortsetzung folgt...")
        elif choice.lower() == "wiese":
            print("\nDu stellst dich mitten auf die Wiese und ein Blitz schlägt auf dich ein. Du wirst ohnmächtig...") 
        else:
            print("Das ist keine gültige Wahl. Du stirbst sofort. Das Spiel endet hier.")
            start_game()  # Neustart bei ungültiger Eingabe

    else:        
        print("\nDas ist keine gültige Wahl. Bitte wähle '1' oder '2'.")
        start_game()  # Neustart bei ungültiger Eingabe

# Starte das Spiel
start_game()
