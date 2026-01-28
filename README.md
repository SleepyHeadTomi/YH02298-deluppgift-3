### Deluppgift 3 - Test av routes på fakestoreapi.com med pytest och requests

Denna uppgift innehåller automatiserade tester för att testa routes på fakestoreapi.com

Projektet har utvecklats med Python-version 3.13.4, men bör fungera med tidigare versioner (exempelvis med 3.11 om denna
version redan finns installerad på datorn).

#### Krav:
Följande behöver installerat på datorn:
- Python 3.13 (alt. 3.11)
- (IDE, tex PyCharm)

#### Installationsguide (via `cmd`, System: Windows):
1. Öppna kommandotolk och klona ner repot från GitHub, `git clone https://github.com/SleepyHeadTomi/YH02298-deluppgift-3.git`
2. Gå in i projekt-mappen: `cd YH02298-deluppgift-3`
3. Skapa virtuell miljö: `py -3.13 -m venv .venv`
4. Aktivera miljö: `.venv\Scripts\activate`
5. Installera paket: `pip install -r requirements.txt`
6. Kör test med: `pytest -v`
7. Deaktivera miljön efter körning: `deactivate`

Som i deluppgift 2, går det bra att köra denna procedur i IDE:n.