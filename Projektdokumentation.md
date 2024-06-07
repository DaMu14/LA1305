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

✍️ Die Nummer hat das Format `N.m`, wobei `N` die Nummer der User Story ist, die der Testfall abdeckt, und `m` von `1` an nach oben gezählt. Beispiel: Der dritte Testfall, der die zweite User Story abdeckt, hat also die Nummer `2.3`.

### 1.4 Diagramme

✍️ Hier können Sie PAPs, Use Case- und Gantt-Diagramme oder Ähnliches einfügen.

## 2 Planen

| AP-№ | Frist | Zuständig | Beschreibung | geplante Zeit |
| ---- | ----- | --------- | ------------ | ------------- |
| 1.A  |       |           |              |               |
| ...  |       |           |              |               |

Total: 

✍️ Die Nummer hat das Format `N.m`, wobei `N` die Nummer der User Story ist, auf die sich das Arbeitspaket bezieht, und `m` von `A` an nach oben buchstabiert. Beispiel: Das dritte Arbeitspaket, das die zweite User Story betrifft, hat also die Nummer `2.C`.

✍️ Ein Arbeitspaket sollte etwa 45' für eine Person in Anspruch nehmen. Die totale Anzahl Arbeitspakete sollte etwa Folgendem entsprechen: `Anzahl R-Sitzungen` ╳ `Anzahl Gruppenmitglieder` ╳ `4`. Wenn Sie also zu dritt an einem Projekt arbeiten, für welches zwei R-Sitzungen geplant sind, sollten Sie auf `2` ╳ `3` ╳`4` = `24` Arbeitspakete kommen. Sollten Sie merken, dass Sie hier nicht genügend Arbeitspakte haben, denken Sie sich weitere "Kann"-User Stories für Kapitel 1.2 aus.

## 3 Entscheiden

✍️ Dokumentieren Sie hier Ihre Entscheidungen und Annahmen, die Sie im Bezug auf Ihre User Stories und die Implementierung getroffen haben.

## 4 Realisieren

| AP-№ | Datum | Zuständig | geplante Zeit | tatsächliche Zeit |
| ---- | ----- | --------- | ------------- | ----------------- |
| 1.A  |       |           |               |                   |
| ...  |       |           |               |                   |

✍️ Tragen Sie jedes Mal, wenn Sie ein Arbeitspaket abschließen, hier ein, wie lang Sie effektiv dafür hatten.

## 5 Kontrollieren

### 5.1 Testprotokoll

| TC-№ | Datum | Resultat | Tester |
| ---- | ----- | -------- | ------ |
| 1.1  |       |          |        |
| ...  |       |          |        |

✍️ Vergessen Sie nicht, ein Fazit hinzuzufügen, welches das Test-Ergebnis einordnet.

# Portfolioeintrag
