# Projekt-Dokumentation



Damian Müller
Julian Hitz
                                                           |

## 1 Informieren

### 1.1 Ihr Projekt

In diesem Projekt wollen wir ein Sudoku mit Python programmieren, welches auch in der Lage ist ein neues Rätsel zu generieren.

### 1.2 User Stories

| US-№ | Verbindlichkeit | Typ  | Beschreibung                       |
| ---- | --------------- | ---- | ---------------------------------- |
| 1    |  Muss               | Funktional     | Als User möchte ich das Sudoku in verschiedenen Schwierigkeitsstufen spielen können, damit ich es meinen Fähigkeiten anpassen kann.  |
| 2    |  Muss               | Funktional     | Als User möchte ich das Sudoku starten können, damit ich die Schwierigkeitsstufen wählen kann. |
| 3    | Muss            | Funktional       | Als User möchte ich Zahlen in leere Felder eingeben können, damit ich das Spiel lösen kann. |
| 4    |   Muss       | Funktional    | Als User möchte ich eine Anleitung haben, wie das Spiel funktioniert damit ich das Spiel lernen kann. |
| 5  |  Muss     | Funktional    | Als User möchte ich eine einzelne Zahl überprüfen können, damit ich weiss ob ich Fehler habe. |
| 6   | Muss     | Funktional     | Als User möchte ich mein ganzes Sudoku überprüfen können, damit ich weiss ob ich Fehler habe.  |
| 7  |  Muss     | Funktional    | Als User möchte ich bei den verschiedenen Schwierigkeitsstufen unterschiedlich viele Felder frei haben, damit ich das Spiel besser lernen kann. |
| 8  | Muss       | Funktional    | Als User möchte ich das Spiel neu starten können , damit ich ohne Probleme weiterspielen kann. |
| 9  | Muss |    Funktional   | Als User möchte ich die eingegebene Zahl löschen können, damit ich meine Fehler verbessern kann. |
| 10 | Muss | Funktional      | Als User möchte ich, dass meine falschen Eingaben farblich hervorgehoben werden, damit ich gleich sehe wo der Fehler ist. |


### 1.3 Testfälle

| TC-№ | Ausgangslage | Eingabe | Erwartete Ausgabe |
| ---- | ------------ | ------- | ----------------- |
| 1.1  | Schwierigkeitsstufen werden angezeigt | Einfach auswählen | Sudoku mit gewählter Schwierigkeitsstufe |
| 1.2  | Schwierigkeitsstufen werden angezeigt | Mittel auswählen  | Sudoku mit gewählter Schwierigkeitsstufe  |
| 1.3  | Schwierigkeitsstufen werden angezeigt | Schwer auswählen | Sudoku mit gewählter Schwierigkeitsstufe  |
| 2.1  | Spiel starten | -  | Anzeige von Schwierigkeitsstufen |
| 3.1  | Sudoku Feld erstellt | 1 | Zahl wird angezeigt                  |
| 4.1  | Spiel gestartet | Button für Anleitung | Spielerklärung |
| 5.1  | Zahl 2 in Position 1,2 eingegeben | Einzelne Zahlen prüfen auswählen  | Die Zahl 2 an Position 1, 2 ist ungültig   |
| 5.2  | Zahl 3 in Position 1,2 eingegeben  | Einzelne Zahlen prüfen auswählen | Alle eingegebenen Zahlen sind korrekt |
| 6.1  | Sudoku gelöst | Prüfen auswählen  | Glückwunsch! Sie haben das Rätsel gelöst |
| 6.2  | Sudoku gelöst | Prüfen auswählen  | Die Lösung ist nicht korrekt. |
| 7.1  | Spiel ist gestartet | Einfach auswählen | Sudokufeld mit 30 leeren Felder |
| 7.2  | Spiel ist gestartet | Mittel auswählen  | Sudokufeld mit 40 leeren Felder |
| 7.3  | Spiel ist gestartet | Schwer auswählen  | Sudokufeld mit 50 leeren Felder |
| 8.1  | Sudoku gelöst   | neues Spiel auswählen  | Schwierigkeitsstufen werden angezeigt |
| 9.1  | Anzeige von falscher Zahl | Zahl löschen   | Feld ist leer | 
| 10.1 | Zahl eingegeben      | Zahl überprüfen   | falsche Zahl wird rot markiert | 

✍️ Die Nummer hat das Format `N.m`, wobei `N` die Nummer der User Story ist, die der Testfall abdeckt, und `m` von `1` an nach oben gezählt. Beispiel: Der dritte Testfall, der die zweite User Story abdeckt, hat also die Nummer `2.3`.

### 1.4 Diagramme

✍️ Hier können Sie PAPs, Use Case- und Gantt-Diagramme oder Ähnliches einfügen.

## 2 Planen

| AP-№ | Frist | Zuständig | Beschreibung | geplante Zeit |
| ---- | ----- | --------- | ------------ | ------------- |
| 1.A  | 07.06.2024  | Müller | Schwierigkeitsstufen | 3*45'    |
| 2.A  | 07.06.2024  | Müller | Sudoku starten       | 30'      |
| 3.A  | 07.06.2024  | Müller | Eingabe in Felder    | 2*45     |
| 4.A  | 07.06.2024  | Hitz   | Anleitung            | 30'      |
| 5.A  | 07.06.2024  | Hitz   | Überprüfung einzelner Zahlen    |  2*45' |
| 6.A  | 07.06.2024  | Hitz   | Überprüfung alles    | 45'      |
| 7.A  | 07.06.2024  | Müller | Schwierigkeitsstufen Anzahl leere Felder | 2*45' |
| 8.A  | 07.06.2024  | Müller | Neustart             | 30'      |
| 9.A  | 07.06.2024  | Hitz   | Zahl löschen         | 30'      |

Total: 570' 


## 3 Entscheiden

✍️ Dokumentieren Sie hier Ihre Entscheidungen und Annahmen, die Sie im Bezug auf Ihre User Stories und die Implementierung getroffen haben.

## 4 Realisieren

| AP-№ | Datum | Zuständig | geplante Zeit | tatsächliche Zeit |
| ---- | ----- | --------- | ------------- | ----------------- |
| 1.A  | 24.05.2024 | Müller  | 30' | 30'     |
| 2.A  | 24.05.2024 | Müller  | 30' | 30      |
| 3.A  | 31.05.2024 | Müller  | 2*45 | 60'    |
| 4.A  | 31.05.2024 | Hitz    | 30' | 30'     |
| 5.A  | 07.06.2024 | Hitz    | 2*45' | 2*45' |
| 6.A  | 07.06.2024 | Hitz    | 45'   |  60'  |
| 7.A  | 22.05.2024 | Müller  | 2*45'         |  2*45'         |
| 8.A  | 31.05.2024 | Müller  | 30'           |  30'           |
| 9.A  | 22.05.2024 | Hitz    | 30'           |  30'           |

✍️ Tragen Sie jedes Mal, wenn Sie ein Arbeitspaket abschließen, hier ein, wie lang Sie effektiv dafür hatten.

## 5 Kontrollieren

### 5.1 Testprotokoll

| TC-№ | Datum | Resultat | Tester |
| ---- | ----- | -------- | ------ |
| 1.1  |14.6.24  |  OK        | Müller       |
| 1.2  |   14.6.24    | OK         |  Müller      |
|  1.3      | 14.6.24    |  OK        |  Müller       |
|  2.1     | 14.6.24        | OK       |  Müller     |
|  3.1      |14.6.24     | OK         | Müller        |
|   4.1     | 14.6.24    | OK         |  Müller       |
|  5.1      | 14.6.24    |   OK       |  Müller       |
| 5.2       |  14.6.24   |  OK        |  Müller       |
|  6.1        | 14.6.24    |  OK        |  Müller       |
|  6.2      | 14.6.24    | OK         | Müller        |
| 7.1       | 14.6.24    |  OK        |  Müller       |
| 7.2    | 14.6.24    |  OK        |  Müller       |
|   7.3 | 14.6.24    |  OK        |  Müller       |
|  8.1      |14.6.24     | OK         |Müller         |
| 9.1   | 14.6.24    |  OK        | Müller        |
 



✍️ Vergessen Sie nicht, ein Fazit hinzuzufügen, welches das Test-Ergebnis einordnet.

# Portfolioeintrag
