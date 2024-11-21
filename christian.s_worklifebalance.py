import time
import webbrowser
import random

print("Zzz... Halloooo!")
print("Ich bin Pausi, das Faultierprogramm. Ich liebe Pausen mehr als alles andere!")
print("Keine Sorge, ich helfe dir, alle 90 Minuten Pause zu machen. Aber wehe, du überarbeitest dich!")
print("Dein Arbeitstag dauert 8 Stunden, und ich erinner dich daran entspannte Pausen mit deinem Lieblingslied zu machen!")
print("Lass uns anfangen... aber denk dran, ich mach das nur wegen der Pausen. Zzz...")

arbeitszeit = 8 * 60  
pause_dauer = 10 #Finde 10 besser als 7.5
lernintervall = 90  
aktueller_tag = 0  

lieblingslieder = [
    "https://www.youtube.com/watch?v=epVJQ4v68CY",  
    "https://www.youtube.com/watch?v=v_EWWyJfgPc",  
    "https://www.youtube.com/watch?v=rATbtwj1qls&list=RDrATbtwj1qls&start_radio=1",  
    "https://www.youtube.com/watch?v=xEGWKXwUb54",
    "https://www.youtube.com/watch?v=ulfeM8JGq7s",        
]

while aktueller_tag < arbeitszeit:
    print("Zzz... Ich hoffe, du arbeitest. Ich kann dich nicht kontrollieren, aber ich träume von Pausen!")
    time.sleep(lernintervall * 60)  
    print("\n Hurraaa, Pauseee! Endlich Zeit für Entspannung! ALSO FINGER WEG VON DER TASTATUR! ")
    print("Ich öffne jetzt eines meiner Lieblingslieder... aber wehe, du machst danach weiter mit dem Arbeiten. Zzz...")
    
   
    zufallslied = random.choice(lieblingslieder)
    webbrowser.open(zufallslied)
    
    time.sleep(int(pause_dauer * 60))  
    aktueller_tag += lernintervall + pause_dauer  
    print("Zzz... Pause vorbei :c Warum musst du überhaupt lernen? Naja, zurück an die Arbeit. Ich schlafe weiter.\n")

print("Oh, endlich! Dein Arbeitstag ist vorbei! Das hast du super gemacht, Ich bin stolz auf dich... aber jetzt ab in die Hängematte!")
