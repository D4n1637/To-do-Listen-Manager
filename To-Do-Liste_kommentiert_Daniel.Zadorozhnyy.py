import json # Das eingebaute JSON-Modul wird geladen. JSON ist ein Textformat, um Daten zu speichern. 
import tkinter as tk # Tkinter ist ein Modul für grafische Benutzeroberflächen (Fenster, Buttons, Labels, etc.).
from PIL import Image, ImageTk # Das Pillow-Modul ist zum Laden und Bearbeiten von Bildern und zur Anzeige von Bildern in Tkinter.
from datetime import datetime, timedelta # Datetime arbeiten mit Datum und Uhrzeit und timedelta berechnet Zeitabstände .

DATEI_NAME = "todoliste.json" # Variable speichert einen String.

def wissen_laden(): # Nebenfunktion wird definiert.
    try:
       
        with open(DATEI_NAME, 'r', encoding='utf-8') as datei:# Die Datei mit dem Namen wissen.json.neu wird geöffnet. Das r steht für Lesemodus, bei welchem die Datei zum Auslesen geöffent wird.
            # Das utf-8 sorgt für eine Umwandlung von Zahlen zu Zeichen, da der Computer nur Zahlen speichern kann. Dabei steht die 8 für 8 Bits, was ein Byte ist.
            # Schriftzeichen werden in Bytes ugewandelt (1-4 Bytes pro Zeichen).
            return json.load(datei) # Die Datei wird ausgelesen und von einer JSON-Datei in eine Python-Dictionary umgewandelt.
    except FileNotFoundError: # Wenn die Datei nicht gefunden wird, dann wird folgender Inhalt zurückgegeben:
       
        return {
            "liste": ["Putzen","Sport","Lernen"],
            "erinnerungen": {
                "aufgaben": [],
                "zeiten": []
        }
}

def wissen_speichern(das_wissen): # Nebenfunktion wird definiert.
 
    with open(DATEI_NAME, 'w', encoding='utf-8') as datei: # Das W steht für den Schreibmodus, bei dem eine neue Datei erstellt wird oder komplett überschrieben wird, wenn sie schon existiert.
        json.dump(das_wissen, datei, indent=4) # indent sorgt für schöne Formatierung und die 4 steht für 4 Leerzeichen, mit denen Codeblöcke eingerückt werden.
        #Json.dump() sorgt dafür, dass die Python-Daten wie z.B. eine Dictionary in einen JSON-Text umgewandelt werden.
        # Das_wissen ist ein Parameter, der für die Daten steht, welche umgewandelt und gespeichert werden sollten. In der Variable datei wird die geöffnete Datei gespeichert.

def pause(): # Nebenfunktion wird definiert.
    root.after(500, loeschen) # Nach 500 ms wird die Nebenfunktino loeschen aufgerufen.
    
def pause2(): # Nebenfunktion wird definiert
    for i in range(len(variablenPrio)): # For-Schleife, welche solange geht wie lang die Liste variablenPrio ist.
        if variablenPrio[i].get(): # Wenn die Variable in dieser Liste am Index i True ist, dann
            checkboxenPrio[i].config(image = img_on) # ändert die checkbox mit welcher die Variable verknüpft ist ihr Bild.
            checkboxenPrio[i].image = img_on # Diese Zeile sorgt dafür, dass das Bild nicht gelöscht wird, sondern gespeichert bleibt. Würde diese Zeile fehlen, würde das Bild nach einiger Zeit direkt
            # gelöscht werden.
    root.after(500,priorisieren) # Nach 500 ms wird die Nebenfunktion priorisieren aufgerufen.

def pause3(): # Nebenfunktion wird definiert.
    for i in range(len(variablenTime)): # For-Schleife, welche solange geht wie lang die Liste variablenTime ist. 
        if variablenTime[i].get(): # Wenn die Variable in dieser Liste am Index i True ist, dann
            checkboxenTime[i].config(image = img_on_2) # ändert die checkbox mit welcher die Variable verknüpft ist ihr Bild.
            checkboxenTime[i].image = img_on_2 # Diese Zeile sorgt dafür, dass das Bild nicht gelöscht wird, sondern gespeichert bleibt. Würde diese Zeile fehlen, würde das Bild nach einiger Zeit direkt
            # gelöscht werden.
    root.after(500,erinnerung) # Nach 500 ms wird die Nebenfunktion erinnerung aufgerufen.

def loeschen(): # Nebenfunktion wird definiert.
    global liste # global gibt an, dass eine globale Variable gemeint ist. Verwendet man kein global, dann erkennt die Nebenfunktion diese Variable nicht.
    truezahlen = [] # Leere Liste wird definiert.
    for i in range(len(variablen)): # For-Schleife, welche solange geht wie lang die Liste variablen ist.
        variable = variablen[i] # In variable wird der Inhalt der Liste variablen am Index i gespeichert.
        if variable.get(): # Wenn diese Variable True ist, dann
            truezahlen.append(i) # wird die Liste um die Zahl i erweitert.
            
    liste2 = [] # Leere Liste wird definiert.
    for i in range(len(truezahlen)): # For-Schleife, welche solange geht wie lang die Liste truezahlen ist. 
        liste2.append(liste[truezahlen[i]]) # liste2 erhält die Elemente aus liste an den Indizes, welche in der Liste truezahlen gespeichert wurden.
    
    liste = [x for x in liste if x not in liste2] # In liste wird alles gespeichert, was nicht in liste2 ist. Wenn man hier set benutzt, dann ist die resultierende Liste ungeordnet.
    daten["liste"] = liste # Der Inhalt von liste wird im Dictionary daten an dem Key liste gespeichert.
    wissen_speichern(daten) # S. o.
           
    varCheckboxEntfernen() # Nebenfunktion wird aufgerufen.
    
    checkboxes() # Nebenfunktion wird aufgerufen.


def hinzufuegen(): # Nebenfunktion wird definiert.
    global liste # global gibt an, dass eine globale Variable gemeint ist. Verwendet man kein global, dann erkennt die Nebenfunktion diese Variable nicht.
    neuesToDo = entry.get().lower().capitalize() # Die Eingabe wird in der Variable neuesToDo gespeichert. Lower macht erstmal alles klein und capitalize macht den ersten Buchstaben groß.
    liste.append(neuesToDo) # Liste wird um den neuen Eintrag erweitert.
    daten["liste"] = liste # Inhalt von liste wird in der Dictionary daten am Key liste gespeichert.
    entry.delete(0,tk.END) # Dadurch wird der Inhalt vom Eingabefeld von Anfang (0) bis Ende (tk.END) gelöscht.
    wissen_speichern(daten)# S. o.
    
    varCheckboxEntfernen() # Nebenfunktion wird aufgerufen.
        
    checkboxes() # Nebenfunktin wird aufgerufen.

def priorisieren(): # Nebenfunktion wird definiert.
    global liste # global gibt an, dass eine globale Variable gemeint ist. Verwendet man kein global, dann erkennt die Nebenfunktion diese Variable nicht.
    for i in range(len(variablenPrio)): # For-Schleife, welche solange geht wie lang die Liste variablenPrio ist.
        varPrio = variablenPrio[i] # in varPrio wird der Inhalt der Liste variablenPrio am Index i gespeichert.
        if varPrio.get(): # Wenn diese Variable True ist, dann
            prio = [] # wird eine leere Liste erstmal definiert.
            prio.append(liste[i]) # Diese Liste wird das Element aus liste am Index i erweitert.
            liste = [x for x in liste if x != liste[i]] # In liste wird alles gespeichert außer das Element aus liste am Index i.
            prio.extend(liste) # Die Lsite prio wird um liste erweitert, wodruch nun das Element aus liste am Index i ganz am Anfang von prio steht.
            liste = prio # Der Inhalt von prio wird nun überschrieben in liste.
            daten["liste"] = liste # Der Inhalt von liste wird in der Dictionary daten an dem Key liste gespeichert.
            wissen_speichern(daten)# S. o.
            
            varCheckboxEntfernen() # Nebenfunktion wird aufgerufen.
            
            checkboxes() # Nebenfunktion wird aufgerufen.

def erinnerung(): # Nebenfunktion wird definiert.
    global liste # global gibt an, dass eine globale Variable gemeint ist. Verwendet man kein global, dann erkennt die Nebenfunktion diese Variable nicht.
    for i in range(len(variablenTime)): # For-Schleife, welche solange geht wie lang die Liste variablenTime ist.
        varTime = variablenTime[i] # in varTime wird der Inhalt der Liste variablenTime am Index i gespeichert.
        if varTime.get(): # Wenn diese Variable True ist, dann
            zielZeit = (datetime.now() + timedelta(seconds = 5)).isoformat() # wird in der Variable zielZeit die jetztige  Zeit + 5 Sekunden gespeichert. Isoformat sorgt dafür, dass das datetime Objekt
            # als string gespeichert wird. Das muss getan werden, da Json nicht auf datetime Objekte zugreifen kann.
            erinnerungen["aufgaben"].append(liste[i]) # In der Liste aufgaben aus der Dictionary erinnerungen wird das Element aus liste am Index i gespeichert. 
            erinnerungen["zeiten"].append(zielZeit) # In der Liste zeiten aus der Dictionary erinnerungen wird die Variable zielZeit gespeichert.
            daten["erinnerungen"]["aufgaben"] = erinnerungen["aufgaben"] # Der Inhalt der Liste aufgaben aus der Dictionary erinnerungen wird in der Dictionary daten am Key
            #erinnerungen in seiner Liste aufgaben gespeichert.
            daten["erinnerungen"]["zeiten"] = erinnerungen["zeiten"]# Der Inhalt der Liste zeiten aus der Dictionary erinnerungen wird in der Dictionary daten am Key
            #erinnerungen in seiner Liste zeiten gespeichert.
            wissen_speichern(daten) # S. o.
            
    varCheckboxEntfernen() # Nebenfunktion wird aufgerufen.
    
    check() # Nebenfunktion wird aufgerufen.
    checkboxes() # Nebenfunktion wird aufgerufen.

def check(): # Nebenfunktion wird definiert.
    entfernenZeit = [] # Leere Liste wird definiert.
    entfernenAufgaben = [] # Leere Liste wird definiert.
    for i in range(len(erinnerungen["zeiten"])): # For-Schleife, welche solange geht wie lang die Liste zeiten aus der Dictionary erinnerungen ist.
            if datetime.now() >= datetime.fromisoformat(erinnerungen["zeiten"][i]): # Wenn die Zeit jetzt größer ist als die gespeicherte Zeit der Liste zeiten am Index i aus der Dicitionary erinnerungen
                for i in range(len(erinnerungen["zeiten"])): # For-Schleife läuft solange wie die Liste zeiten lang ist. 
                    label3 = tk.Label(root, text="Erinnerung: " + erinnerungen["aufgaben"][i], borderwidth = 1, relief = "solid") # , dann wird folgender Text erstellt.
                    label3.grid(row = 0, column = 6, sticky = "ew") # Der Text wird hier richtig positioniert. Das ew sorgt für eine horizontale Streckung
                    root.after(2000, label3.destroy) # Nach 2 Sekunden wird der Text wieder gelöscht.
                    entfernenZeit.append(erinnerungen["zeiten"][i]) # Die Liste wird erweitert um das Element der Liste zeiten am Index i aus der Dictionary erinnerungen.
                    entfernenAufgaben.append(erinnerungen["aufgaben"][i]) # Die Liste wird erweitert um das Element der Liste aufgaben am Index i aus der Dictionary erinnerungen

            else:
                root.after(500,check) # Wenn aber keine gespeicherte Zeit größer als die jetztige ist, dann wird die Nebenfunktion check nach 500 ms nochmal aufgerufen.
    
    erinnerungen["aufgaben"] = [x for x in erinnerungen["aufgaben"] if x not in entfernenAufgaben] # In der Liste aufgaben alles außer der Inhalt von entfernenAufgaben gespeichert.
    erinnerungen["zeiten"] = [x for x in erinnerungen["zeiten"] if x not in entfernenZeit] # In der Liste aufgaben alles außer der Inhalt von entfernenZeit gespeichert.
    
    daten["erinnerungen"]["aufgaben"] = erinnerungen["aufgaben"] # Der Inhalt von der Liste aufgaben der Dictionary erinnerungen wird nun in der Dictionary daten am Key erinnerungen in dessen Liste
    # aufgaben gespeichert.
    daten["erinnerungen"]["zeiten"] = erinnerungen["zeiten"]# Der Inhalt von der Liste zeiten der Dictionary erinnerungen wird nun in der Dictionary daten am Key erinnerungen in dessen Liste
    # zeiten gespeichert.
    wissen_speichern(daten) # S. o.

def varCheckboxEntfernen(): # Nebenfunktion wird definiert.
    # Hier werden sämtliche Variablen in Listen und Checkboxen gelöscht, damit beim Neuerstellen der Checkboxen es keine Überlagerungen gibt und
    # damit die neuen Checkboxen auch mit neuen Variablen verknüpft werden.
    del variablen[:]  
    for checkbox in checkboxen:
        checkbox.destroy()
    del checkboxen[:]
    
    del variablenPrio[:]
    for checkboxPrio in checkboxenPrio:
        checkboxPrio.destroy()
    del checkboxenPrio[:]
    
    del variablenTime[:]
    for checkboxTime in checkboxenTime:
        checkboxTime.destroy()
    del checkboxenTime[:]
            
    del checkboxenPrio[:]

def ende(): # Nebenfunktion wird definiert.
    root.after(2000, root.destroy) # Nach 2 Sekunden wird das Fenster geschlossen.

def checkboxes(): # Nebenfunktion wird definiert.
    for i in range(len(liste)): # For-Schleife wird solange ausgeführt wie liste lang ist.
        var = tk.BooleanVar() # tk.BooleanVar() erstellt eine True/False-Variable für die normalen Checkboxen. Diese wird in var gespeichert.
        variablen.append(var) # Die Variable wird in der Liste variablen gespeichert.
        
        varPrio = tk.BooleanVar() # tk.BooleanVar() erstellt eine True/False-Variable für die Prioritätscheckboxen. Diese wird in varPrio gespeichert.
        variablenPrio.append(varPrio) # Die Variable wird in der Liste variablenPrio gespeichert.
        
        varTime = tk.BooleanVar() # tk.BooleanVar() erstellt eine True/False-Variable für die Timercheckboxen. Diese wird in varTime gespeichert.
        variablenTime.append(varTime) # Die Variable wird in der Liste variablenTime gespeichert.
        
        checkbox = tk.Checkbutton(root,text = liste[i],variable = var, command = pause) # tk.Checkbutton(...) erstellt eine Checkbox, welche im Hauptfenster angezeigt wird und den Text von liste am
        # Index i enthält. Variable = var sorgt dafür, dass die Checkbox mit der Variable var verbunden wird. Wenn man diese Checkbox anklickt, wird die Nebenfunktion pause aufgerufen.
        checkbox.grid(row = i + 1, column = 1, sticky = "W") # sticky = "W" sorgt dafür das der Text linksbündig angezeigt wird.
        checkboxen.append(checkbox) # Hier wird die erstellte Checkbox in der Liste checkboxen gespeichert.
        
        checkboxPrio = tk.Checkbutton(root,image = img_off,variable = varPrio, command = pause2, indicatoron = False, borderwidth = 0) # S. o. Image sorgt dafür, dass ein Bild in der Checkbox angezeigt
        # wird und zwar dieses, welches in img_off gespeichert wurde. Durch indicatoron = False wird das klassische Häckchen ausgeblendet und durch borderwidth = 0 wird der Rahmen der Checkbox
        # ausgeblendet.
        checkboxPrio.grid(row = i + 1, column = 2, sticky = "W")
        checkboxenPrio.append(checkboxPrio)
        
        checkboxTime = tk.Checkbutton(root, image = img_off_2,variable = varTime, command = pause3, indicatoron = False, borderwidth = 0) # S. o.
        checkboxTime.grid(row = i + 1, column = 3, sticky = "W")
        checkboxenTime.append(checkboxTime)
   
       
       
root = tk.Tk() # Hauptfenster wird erstellt. Root ist das Hauptfenster.
root.geometry("450x200") # Größe des Fensters wird definiert. 450 Pixel Breite und 200 Pixel Höhe.
root.title("To-Do-Liste") # Das Hauptfenster bekommt den Titel "To-Do-Liste". Dieser wird oben in der Leiste angezeigt.

img_off = ImageTk.PhotoImage(Image.open("star.jpg").resize((15, 15))) # Image.open("star.jpg") öffnet die Bilddatei star.jpg, .resize((15, 15)) verkleinert das Bild auf 15x15 Pixel,
# ImageTk.PhotoImage(...) wandelt das Bild in ein Format um, welches Tkinter anzeigen kann und in img_off wird das Ergebnis gespeichert
img_on = ImageTk.PhotoImage(Image.open("Star-icon.png").resize((15, 15))) # s. o.

img_off_2 = ImageTk.PhotoImage(Image.open("timer.icon.aus.webp").resize((15, 15))) # s. o.
img_on_2 = ImageTk.PhotoImage(Image.open("timer.icon.an.webp").resize((15, 15))) # s. o.

daten = { # Die Dictionary daten speichert folgenden Inhalt:
    "liste": ["Essen","Trinken","Schlafen"],
    "erinnerungen": {
        "aufgaben": [],
        "zeiten": []
        }
    }

daten = wissen_laden() # In der Variable daten werden entweder die JSON-Daten gespeichert oder falls diese nicht vorhanden sind, wird das zurückgegeben, was in der Nebenfunktion steht.

liste = daten["liste"] # In der Variable liste wird der Inhalt des Keys liste von der Dictionary daten gespeichert.
erinnerungen = daten["erinnerungen"] # In der Variable erinnerungen wird der Inhalt des Keys erinnerungen von der Dictionary daten gespeichert.

# Leere Listen werden definiert.
variablen = [] 
variablenPrio = []
variablenTime = []
checkboxen = []
checkboxenPrio = []
checkboxenTime = []

checkboxes() # Nebenfunktion wird aufgerufen.
check() # Nebenfunktion wird aufgerufen.

Button2 = tk.Button(root, text = "Hinzufügen", command = hinzufuegen).grid(row = 0, column = 4) # tk.Button(...) erstellt einen Button, durch root kommt der Button ins Hauptfenster, durch den Befehl text
# wird der Text "Hinzufügen" auf dem Button angezeigt, wenn man den Button drückt, wird die Nebenfuntion hinzufuegen aufgerufen und grid positioniert den Button in der ersten Reihe (row = 0) und in der
# fünften Spalte (column = 4)

entry = tk.Entry(root) # tk.Entry(root) erstellt eine Eingabefeld, welches in Hauptfenster angezeigt wird. Dies wird in der Variable entry gespeichert.
# Man darf nicht hier direkt grid verwenden, da sonst ein Nonetype zurück kommen kann.
entry.grid(row = 0, column = 5) # Das Eingabefeld wird in der ersten Reihe und in der sechsten Spalte positioniert.

label = tk.Label(root, text="Aufgaben", borderwidth = 1,relief = "raised").grid(row = 0, column = 1, sticky = "ew") # tk.Label(...) erstellt nur einen Text. Borderwidth erstellt einen Rahmen
# (hier mit einem Pixel Breite). Relief sorgt für einen Stil des Rahmens. Durch raised wirkt der Text erhöht. Sticky sorgt für die Ausrichtung des Textes in seiner Zeile und durch "ew" wird der Text
# horizontal gesreckt.
label2 = tk.Label(root, text="Aktion", borderwidth = 1, relief = "raised").grid(row = 0, column = 2, columnspan = 2) # S. o. Columnspan sorgt dafür das der Text hier über 2 Spalten geht.


root.protocol("WM_DELETE_WINDOW", ende) # Wenn das Fenster geschlossen wird, wird die Nebenfunktion ende ausgeführt.

root.mainloop() # Startet die Ereignisschleife, wodurch das Fenster geöffnet bleibt und auf Benutzerinteraktionen reagiert werden kann.