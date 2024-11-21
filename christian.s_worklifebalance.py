# -*- coding: utf-8 -*-

import time
import webbrowser
import random

def main():
    print("Zzz... Halloooo!")
    print("Ich bin Pausi, das Faultierprogramm. Ich liebe Pausen mehr als alles andere!")
    print("Keine Sorge, ich helfe dir, alle 90 Minuten Pause zu machen. Aber wehe, du überarbeitest dich!")
    print("Dein Arbeitstag dauert 8 Stunden, und ich erinnere dich daran, entspannte Pausen mit deinem Lieblingslied zu machen!")
    print("Lass uns anfangen... aber denk dran, ich mach das nur wegen der Pausen. Zzz...")
    
    work_and_pause()

def play_song():
    lieblingslieder = [
        "https://www.youtube.com/watch?v=epVJQ4v68CY",  
        "https://www.youtube.com/watch?v=v_EWWyJfgPc",  
        "https://www.youtube.com/watch?v=rATbtwj1qls&list=RDrATbtwj1qls&start_radio=1",  
        "https://www.youtube.com/watch?v=xEGWKXwUb54",
        "https://www.youtube.com/watch?v=ulfeM8JGq7s",        
    ]
    zufallslied = random.choice(lieblingslieder)
    webbrowser.open(zufallslied)

def work_and_pause():
    arbeitszeit = 8 * 60  
    pause_dauer = 10  
    lernintervall = 90  
    aktueller_tag = 0  
    pause_counter = 0  
    arbeitszeit_counter = 0  

    while aktueller_tag < arbeitszeit:
        print(f"\nZzz... Ich hoffe, du arbeitest fleißig. Ich kann dich nicht kontrollieren, aber ich träume von Pausen!")
        print(f"Du hast bisher {arbeitszeit_counter} Minuten konzentriert gearbeitet.")
        
        time.sleep(lernintervall * 60)  
        arbeitszeit_counter += lernintervall  

        print("\nHurraaa, Pauseee! Endlich Zeit für Entspannung! ALSO FINGER WEG VON DER TASTATUR!")
        print("Ich öffne jetzt eines meiner Lieblingslieder... aber wehe, du machst danach weiter mit dem Arbeiten. Zzz...")

        play_song()  

        time.sleep(int(pause_dauer * 60))  
        aktueller_tag += lernintervall + pause_dauer  
        pause_counter += 1  

        print(f"Zzz... Pause vorbei :c Warum musst du überhaupt lernen? Naja, zurück an die Arbeit. Ich schlafe weiter.\n")
        print(f"Du hast bisher {pause_counter} Pausen gemacht.")
        
        warm_up = input("Möchtest du ein kleines Warm-Up machen? Käpt’n Krabs lädt dich ein, seine Schatzsuche zu spielen! (ja/nein): ").strip().lower()
        if warm_up == "ja":
            zahlenraten()

    print("\nOh, endlich! Dein Arbeitstag ist vorbei! Das hast du super gemacht.")
    print(f"Insgesamt hast du {pause_counter} Pausen gemacht und {arbeitszeit_counter} Minuten konzentriert gearbeitet!")
    print("Ich bin stolz auf dich... aber jetzt ab in die Hängematte!")

def zahlenraten():
    print("\nArrr, willkommen an Bord, du seetaugliche Landratte!")
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

main()
