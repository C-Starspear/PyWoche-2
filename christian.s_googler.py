import webbrowser

print("Guten Tag \(^-^)/ tippe 'suche',dann öffne ich dein Browser für dich.")

while True:
    eingabe = input("Was willst du machen? O.o ")

    if eingabe == "suche":
        print("Gehtklar, ich öffne den Browser! Viel Spaß")
        webbrowser.open("https://duckduckgo.com")


    else:
        print("Ich glaube du hast etwas falsches eingegeben, bitte probiere es nochmal. ^^")
