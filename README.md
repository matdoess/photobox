# photobox

Setup:
- mv /config/private-config.ini.example /config/private-config.ini
-- Werte eintragen
- Copy fonts to ~/photobox/fonts
-- Change Font in templates/screenmanager.kv or Comment out for deafault font


Hinweise:
- Aufgaben
-- Picamera kann keine Sonderzeichen in das Bild einfügen (äüöß ...)
- Photobox mit beliebigem Argument ausführen = Start im Testmodus z.B. auf Laptop für Entwicklung
-- python3 main.py xyz


TODO:
- StandyBy Slideshow


DONE
-- Video Thumbnails erstellen (incl. Video Icon)
-- Konvert Video to mkv after creation
-- Nach laden von Bild bei Aufgabe: Bild neben Aufgabentext anzeigen.
-- exit button einbauen.
-- Foto Spiegeln als Setting in Camera Classe einfügen.
-- Bei Aufagbe wird kein "Dein Bild wird geladen angezeigt" > Erledigt
-- Nach Aufgabe Button auf "Neues Foto" ändern (evtl.) > Erledigt "Aufgabe wiederholen"
-- Fehler Popup bei Email Senden ohne Bild einbauen. > erledigt (Button disabled)
-- telegram_bot in Helper Classe oder eigenes Modul einbauen. Zeit bei SOS mitschicken.
-- imageresize: check if mail folder exists. if not create it.


Changelog:
2018-01-02 (matze):
StartUpScreen eingefügt. Dadurch kann die Clear Tasks Aktion im MenuScreen on_enter verbleiben.
Habe noch einen fehelr gefunden wo die Clear Task im Back Button nicht angezogen wurde.
Beim Starten muss einmal mit OK bestätigt werden. Dann ist alles wie vorher.
Wollte eigentlich vom Startup Screen automatisch auf Menu Screen wechseln. Hat nicht geklappt.
