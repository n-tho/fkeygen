# fkeygen

fkeygen ist simples CLI-Tool zum Generieren von `<phone>`-XML-Konfigurationen für E.164-Telefonnummern.

Das Tool erstellt für jede Telefonnummer eine XML-Struktur, in der die eigene Nummer ausgeschlossen wird. Zusätzlich können beliebige `id`-Werte überspringen und der Output formatiert oder kompakt erzeugt werden.

---

## 🚀 Installation

### 🔹 Option 1: Empfohlen mit `pipx`

```bash
pip install pipx
pipx install .
```

Danach kann das Tool global verwendet werden:

```bash
fkeygen --list 53,54,57
```

### 🔹 Option 2: Klassisch mit `pip`

```bash
pip install .
```

---

## 🧪 Voraussetzungen

- **Python-Version:** ≥ 3.6 (empfohlen: 3.8 oder neuer)
- **Plattform:** läuft unter Linux, macOS & Windows

---

## 🪟 Windows-Nutzer

1. Lade [Python 3.10+](https://www.python.org/downloads/windows/) herunter und installiere es  
2. Installiere `pipx`:

   ```powershell
   python -m pip install --user pipx
   python -m pipx ensurepath
   ```

3. Klone und installiere `fkeygen`:

   ```powershell
   git clone https://github.com/dein-repo/fkeygen
   cd fkeygen
   pipx install .
   ```

---

## 🔧 Nutzung

```bash
fkeygen --list 53,54,57,61
```

### Optionen

| Option        | Beschreibung                                                                 |
|---------------|-------------------------------------------------------------------------------|
| `--list`      | Kommagetrennte E.164-Nummern, z. B. `53,54,57`                               |
| `--idskip`    | Kommagetrennte Liste von IDs, die ausgelassen werden sollen (z. B. `6,7`)    |
| `--pretty`    | Gibt das XML mehrzeilig & eingerückt aus                                     |
| `--file`      | Pfad zur Datei, in die der Output geschrieben wird                           |
| `--version`   | Zeigt die aktuelle Tool-Version                                              |
| `--help`      | Zeigt diese Hilfe                                                            |

---

## 📦 Beispielverwendung

**Standard-Ausgabe (kompakt, einzeilig):**

```bash
fkeygen --list 53,54,57
```

**IDs 6 und 7 überspringen:**

```bash
fkeygen --list 53,54,57,61 --idskip 6,7
```

**Schön formatierter XML-Output:**

```bash
fkeygen --list 53,54,57 --pretty
```

**Ergebnis in Datei schreiben:**

```bash
fkeygen --list 53,54,57 --file output.xml
```

---


## 📄 Beispielausgabe

### Einzeilig (Default)

```xml
### e164=53
<phone><f id='0'><p e164='54' pr='1' di='1'></p></f><f id='1'><p e164='57' pr='1' di='1'></p></f></phone>
```

### Mit `--pretty`

```xml
### e164=53
<phone>
    <f id='0'><p e164='54' pr='1' di='1'></p></f>
    <f id='1'><p e164='57' pr='1' di='1'></p></f>
</phone>
```

---
