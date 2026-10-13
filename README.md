# Handleiding voor de leraar — Les 09: Een veilig account

<!-- Beginvragen (stap 1 van CONTEXT.md), 13-10-2026. Jonas liet de keuzes aan de AI ("Je mag alles negeren wat ik had
     voorgesteld en de les maken die jou het beste lijkt!"):
     klassen 3ORLO, 4ORLOa, 4ORLOb · les 09 van het jaarplan, uur 1 van W08: 4ORLOb di 20 oktober (8ste uur),
     3ORLO di 20 oktober (9de uur), 4ORLOa wo 21 oktober (4de uur) · vorige les gegeven: les 07, in twee lesuren
     (les 08 vervalt) → lesstart = ophalen uit les 07 · toestel lokaal 18, Windows 11 · werkdocument: ja,
     WP3_Een-veilig-account, zonder bronbestanden of zip · context NovaDepot · na les 07 (13-10-2026): een les die ze
     goed kunnen volgen, alles in de browser, zodat ze de vaste manier van werken inoefenen. -->

**Vak:** Toegepaste Informatica
**Doelgroep:** 3ORLO, 4ORLOa en 4ORLOb — 2de graad Organisatie en logistiek, arbeidsmarktgerichte finaliteit
**Lesduur:** 1 × 50 minuten: 10 minuten instructie + 40 minuten keuzewerktijd
**Context:** NovaDepot, *de veiligheidsronde van Sara* (preventiedienst) — module 2 van het jaarplan, les 09
**Toestel:** **lokaal 18, Windows 11** — alles in Chrome, geen bestanden
**Lesdag:** 4ORLOb di 20 oktober (8ste uur) · 3ORLO di 20 oktober (9de uur) · 4ORLOa wo 21 oktober (4de uur)
**Kernleerplandoel:** `BV2_04.04` (toepassen) · ondersteunend `BV2_04.03`, `BK2_01.02.01`
**Deadline:** vrijdag 23 oktober 2026, 20.00 uur · 20 punten
**Pages:** https://jonasdaltongent.github.io/Account-NovaDepot/ · dia's: …/presentatie.html

De leerling helpt Sara van de preventiedienst: een briefje met een wachtwoord op de magazijn-pc, hetzelfde wachtwoord
voor Toms e-mail, en Toms account dat open staat op een tablet. Vier delen in het werkdocument: een wachtwoord
beoordelen en een wachtwoordzin maken, overal een ander wachtwoord en tweestapsverificatie, uitloggen en vergrendelen,
en wat je doet als je account gehackt is. **Nooit een echt wachtwoord**: er is geen invulveld voor een wachtwoord op
de pagina, en de regel staat in de opdracht, op de pagina en in het werkdocument. Opbouw en bronnen: `lesvoorbereiding.md`.

---

## 1. Inhoud van het pakket

```text
W08 - Les 09 - ORLO - Een veilig account/
├── index.html                   # de lespagina: route · één stap · checklist
├── presentatie.html             # 10 dia's: 1 Zo start je · 2 lesstart · 3 lesdoel · 4 de ronde van Sara · 5 wachtwoordzin · 6 sloten, toestellen, Windows + L · 7 controle · 8 stap 1 samen · 9 kloktijden · 10 exitvraag
├── css/style.css, css/slides.css
├── js/script.js, js/slides.js
├── assets/                      # logo's, lettertypes, mascotte (geen screenshots of filmpjes: alles zijn tekeningen)
├── werkdocument/
│   ├── WP3_Een-veilig-account.docx   # het werkdocument dat de leerling INLEVERT (kopie per leerling)
│   ├── maak_werkdocumenten.py        # maakt het opnieuw (python-docx)
│   └── huisstijl.py, go-dalton-gent.png
├── lesvoorbereiding.md
├── dalton-lesfiche.html         # openen, Kopieer de fiche, plakken in je planner
├── classroom.json               # de opdracht voor _tools/zet_opdracht_klaar.py
├── lesdoelen.json               # leerplandoelen voor je jaaroverzicht
└── README.md                    # deze handleiding
```

Geen zip en geen bronbestanden: er is niets te downloaden, uit te pakken of te uploaden.

### 1b. Hoe de lespagina werkt

Zoals les 07: links de **route** (*De veiligheidsronde*: stap 1–4 · *Als het toch misloopt*: stap 5), midden **één stap**
met *Stap voor stap / Kort* (de les begint in *Stap voor stap*), rechts de **checklist** met 15 taken. Geen *Hulp
nodig?*: grijze regels onder de handeling en één tip per stap.

- **Startpagina** met drie beelden: de opdracht in Classroom → deze lespagina → je werkdocument WP3 (groot, zonder
  `.vier`).
- **Infokaders** (`.info`, zoals MW les 4) bij het leesmateriaal: *Een sterk wachtwoord* (stap 2), *Overal een ander
  wachtwoord* en *Twee sloten op de deur* (stap 3), *Is je account gehackt?* (stap 5), in de volgorde van de vragen.
- **Stap 4**: een blauwe knop **Waar ben ik ingelogd?** naar `https://google.com/devices` (nieuw tabblad); de leerling
  kijkt alleen. De lijst met toestellen is een tekening (`.teken-dev`), toestelnamen en plaatsen zijn grijze balkjes.
  **Windows + L** staat als toetsen (`.key`).
- **Zelftest** in stap 5 (drie vragen met knoppen, niets bewaard): tweestapsverificatie, de sterkste wachtwoordzin,
  Windows + L. Geen invulveld, geen wachtwoordmeter.
- **Extra** (telt niet mee, niet in het werkdocument): de wachtwoordtest van Safeonweb en een tip voor thuis.
- `localStorage` bewaart alleen vinkjes en de laatste stap (voorvoegsel `novadepot_account_v1_`), met een wisknop.

---

## 2. Klaarzetten

### Stap 1 — Publiceren via GitHub Pages

Repository `jonasdaltongent/Account-NovaDepot`, Pages op `main`, map `/ (root)`; adres hierboven. Dat adres staat op dia 9,
in `classroom.json` en in `lesdoelen.json`.

### Stap 2 — De opdracht in Classroom, met de koppeling

`classroom.json`: **Werkplek 3 — Een veilig account**, onderwerp *Digitale competenties*, 3ORLO, 4ORLOa en 4ORLOb,
20 punten, deadline vrijdag 23 oktober 2026, 20.00 uur. Bijlagen: de link naar de lespagina en `WP3_Een-veilig-account`
(**Een kopie maken voor elke leerling**). Geen zip. Als **concept** klaargezet op 13-10-2026 en **ingepland** door de hoofdsessie (teruggelezen: `DRAFT` met een tijdstip):
Classroom publiceert zelf een half uur vóór elke les: di 20-10 om 14.05 (4ORLOb) en 14.55 (3ORLO), wo 21-10 om 10.45
(4ORLOa). Het Google-document aan de concepten kreeg op 13-10-2026 de nagelezen versie (zelfde bestand).

Instructietekst:

```text
1. Open de lespagina (link) en je werkdocument WP3_Een-veilig-account.
2. Typ nooit een echt wachtwoord, ook niet in je werkdocument.
3. Klik op Inleveren, ten laatste vrijdag 23 oktober 2026 om 20.00 uur.
```

### Stap 3 — Met de hand, als de koppeling niet werkt

1. Upload `werkdocument/WP3_Een-veilig-account.docx` **in Drive zelf** (**Nieuw** › **Bestand uploaden**, met *Uploads
   converteren* aan) en voeg het toe met **Bijvoegen** › **Drive** › **Een kopie maken voor elke leerling**.
2. Voeg de lespagina toe met **Link**.

### Afvinklijst vóór de les

- [ ] De lespagina staat online en het adres op dia 9 klopt.
- [ ] De opdracht staat in de drie klassen, met twee bijlagen.
- [ ] Een testleerling krijgt een eigen kopie van het werkdocument, met de eigen naam in de titel.
- [ ] Met een **leerlingaccount** geprobeerd: opent de knop in stap 4 `google.com/devices`, en wat toont die pagina?
- [ ] Voor dia 6: je eigen computer, om **Windows + L** te tonen (meld je daarna weer aan). Toon de lijst met toestellen
      **niet live** met je eigen account.
- [ ] De Dalton-lesfiche staat in je planner (open `dalton-lesfiche.html`, klik op **Kopieer de fiche**, plak).
- [ ] `presentatie.html` opent op de beamer; `N` toont je notities, `F` is volledig scherm.

### 2b. Nagelezen klikpaden

| Handeling | Klikpad / naam | Bron |
|---|---|---|
| Waar ben ik ingelogd? | rechtstreeks **google.com/devices**; of Google-account › **Beveiliging en inloggen** › onder **Je apparaten** › **Alle apparaten beheren**. Een toestel aanklikken › **Uitloggen** | [Google-account 3067630](https://support.google.com/accounts/answer/3067630?hl=nl&co=GENIE.Platform%3DDesktop), nagelezen 13-10-2026; zie *Wat nog moet blijken* |
| Computer vergrendelen | **Windows-toets + L** | [Microsoft](https://support.microsoft.com/nl-nl/windows/sneltoetsen-in-windows-dcc61a57-8ff0-cffe-9796-cb9706c75eec), nagelezen 13-10-2026 |
| Werkdocument openen | in de opdracht rechts bij **Jouw werk** op de naam klikken | `_afspraken/klikpaden.md` |
| Inleveren | **Inleveren** | [Classroom 6020285](https://support.google.com/edu/classroom/answer/6020285?hl=nl) |

---

## 3. Het verloop van de les

| Fase | Tijd | Wat |
|---|---|---|
| **Instructie** | **10'** | Dia 1 terwijl de computers opstarten. Dia 2 lesstart (3'): welke naam past een nieuwe leveringsbon van 20 oktober (jaar-maand-dag), met vingers; de brug *"je klassement staat in je Drive, wie kan erbij?"*. Dia 3–6 (5'): lesdoel, de veiligheidsronde van Sara met de Vlaamse cijfers, demo wachtwoordzin (`Nova2026!` tegenover een wachtwoordzin, tellen), demo twee sloten, de lijst met toestellen en **Windows + L** live. Dia 7 controle (1'): *"met een sterk en lang wachtwoord is mijn account altijd veilig"*. |
| **Samen** | **3'** | Dia 8: iedereen doet stap 1; duim op. |
| **Keuzewerktijd** | **tot het einde** | Dia 9 blijft staan, met **kloktijden** (`_tools/zet_lesmomenten.py`); stap 2 tot 5, inleveren inbegrepen. Dia 10 in de laatste minuut, met *Vertrek je? Log uit, of Windows + L*. |

Stap 1–5: 3 + 10 + 8 + 9 + 10 = **40 minuten**. Een gemiddelde leerling is na ± 30 minuten klaar.

**Eerste rondgang:** heeft iedereen het **eigen** werkdocument open (naam in de titel)? Typt niemand een echt wachtwoord?
**Tweede rondgang, rond stap 4:** opent `google.com/devices`? Zeg aan het einde mondeling dat wie niet klaar is, toch inlevert.

---

## 4. Verbetersleutel

De leerling levert alleen het werkdocument in (20 punten: 6 · 5 · 4 · 5).

### Deel 1 — Het briefje (6)

| Wachtwoord | Veilig? | Waarom |
|---|---|---|
| `Nova2026!` | nee | (voorbeeld, al ingevuld) te kort: 9 tekens; de naam van het bedrijf en een jaartal |
| `tompeeters` | nee | een naam, en te kort (10 tekens) |
| `12345678` | nee | te kort, en een reeks cijfers die iedereen als eerste probeert |
| `Drie groene vorken dansen op pallet 7!` | ja | lang (38 tekens), meerdere woorden, geen naam of jaartal |

Wachtwoordzin: minstens 15 tekens en minstens 4 woorden, zonder naam, bedrijf of jaartal (3 punten); de drie rijen
juist, met een reden die klopt (3 punten).

### Deel 2 — Overal hetzelfde (5)

- **a.** *Wie het briefje leest, kan ook in Toms e-mail.* (1)
- **b.** een gsm-code = iets wat je **hebt** · vingerafdruk = iets wat je **bent** · wachtwoord = iets wat je **weet**; rij 1 (pincode = weet) staat er al (2)
- **c.** Nee: de persoon kent het wachtwoord, maar niet het tweede bewijs (een code op de gsm of een vingerafdruk). (2)

### Deel 3 — De tablet aan de laadkaai (4)

- **a.** **Uitloggen** (bij het toestel in de lijst op google.com/devices).
- **b.** **Windows** + **L**.

### Deel 4 — Gehackt? (5)

- **a.** Zijn wachtwoord meteen veranderen.
- **b.** Tweestapsverificatie aanzetten · uitloggen bij het onbekende toestel · NovaDepot verwittigen. Niet: het wachtwoord
  op een briefje kleven, hetzelfde wachtwoord overal gebruiken.
- Punten: 4a = 2 punten, 4b = 3 punten (1 per juiste x); een x bij een fout antwoord kost 1 punt (niet onder 0).

### Essentiële fouten — geef hier altijd feedback op

- Een **echt wachtwoord** in het werkdocument: meteen laten wissen, en het wachtwoord laten veranderen.
- Een wachtwoordzin korter dan 15 tekens.
- Tweestapsverificatie uitgelegd als *twee wachtwoorden*.
- In deel 4 eerst afwachten of het wachtwoord doorsturen.

---

## 5. Schermafbeeldingen (optioneel)

Geen. Alle beelden zijn tekeningen in HTML en CSS (de opdracht in Classroom, het briefje, de tabellen van het
werkdocument, de lijst met toestellen, de toetsen **Windows + L**). Zie `assets/screenshots/LEESMIJ.md`.

---

## 6. Het materiaal opnieuw maken

```bash
python3 "werkdocument/maak_werkdocumenten.py"
```

Maakt `WP3_Een-veilig-account.docx` opnieuw. Vereist `python-docx` en `Pillow`.

---

## 7. Leerplandoelen in je jaaroverzicht

`lesdoelen.json`: `BV2_04.04` (kern), `BV2_04.03` en `BK2_01.02.01` (ondersteunend). De repository krijgt de `pre-push` hook
uit `_sjablonen/pre-push`.

---

## 8. Wat nog moet blijken in de klas

1. **google.com/devices met een leerlingaccount.** Getest met het testaccount demoleerling3 (13-10-2026): de pagina vroeg
   eerst om het wachtwoord opnieuw (een beveiligingscontrole). Er is dus **geen schermafbeelding** van de lijst: een
   tekening staat in de plaats. Sinds het nalezen door de hoofdsessie (13-10-2026) zegt de tip in stap 4: vraagt Google
   je wachtwoord opnieuw, dan is dat normaal; staat er bovenaan **accounts.google.com**, typ het dan in zoals bij het
   aanmelden; lukt het niet, kijk naar de tekening en ga verder met deel 3. Een goed moment voor één zin in de klas: je
   wachtwoord typ je alleen op de echte aanmeldpagina (phishing komt in les 13). Opent de pagina op een schoolaccount,
   en wat staat erin? Misschien blokkeert de beheerder ze.
2. **Typen leerlingen toch een echt wachtwoord** in een vak van het werkdocument, ondanks de regel op de pagina, in de
   opdracht en op dia 5? Kijk daar tijdens de eerste rondgang naar.
3. **Wachtwoordzin**: lukt het tellen van 15 tekens? Maken ze een zin met een naam of jaartal?
4. **Haalbaarheid**: een gemiddelde leerling is na ± 30 minuten klaar, maar niemand was snel klaar in les 07. Halen ze
   inleveren? Werken de grijze regels en infokaders zonder dat ze de antwoorden vooraan lezen?
5. **Werkdocument in Google Documenten**: nagekeken door de hoofdsessie (13-10-2026) als pdf uit het Google-document aan
   het concept: kader, vier delen met puntenvak, lichtblauwe vakken, kruisvakken in deel 2 en 4, de tabel *Nalezen*.
   Alleen de tabel van deel 2b breekt over twee bladzijden.
6. De lespagina en dia's zijn gemeten met scripts (geen horizontaal scrollen op 683, 1024, 1280 en 1440 px; elke dia
   binnen de rand) maar niet door een mens bekeken: kijk de tekeningen na.
