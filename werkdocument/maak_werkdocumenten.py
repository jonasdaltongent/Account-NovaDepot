#!/usr/bin/env python3
"""
maak_werkdocumenten.py
Genereert het werkdocument voor les 09 "Een veilig account" (NovaDepot, ORLO, Werkplek 3).

  WP3_Een-veilig-account.docx   het werkdocument dat de leerling INLEVERT (een kopie per leerling)

Geen bronbestanden en geen zip: de les werkt alleen in het werkdocument en in de browser.

Gebruik:  python3 maak_werkdocumenten.py
Vereist:  python-docx, Pillow

LET OP bij aanpassen:
 - Alle wachtwoorden in dit document zijn verzonnen (NovaDepot). Nooit een echt wachtwoord in het
   werkdocument, en ook geen invulveld dat daarop lijkt: de leerling maakt een wachtwoordzin voor de
   magazijn-pc van NovaDepot, met de regel erbij dat een echt wachtwoord nooit wordt opgeschreven.
 - Rij 1 van deel 1 (Nova2026!) is de demo van dia 5, al ingevuld in het grijs. Rij 1 van deel 2b ook.
 - De punten staan per deel (6 · 5 · 4 · 5) en samen in de controletabel (lesvoorbereiding § 22).
 - Aankruisen = een x typen in een vak (huisstijl.py, tabel met invulkolom). Bij 4b zijn drie van de vijf
   antwoorden juist; de leerling krijgt 1 punt per juiste x en verliest er 1 per foute (niet onder 0).
"""
import os

import huisstijl as hs   # de huisstijl van het werkdocument (uit _sjablonen/lespakket/werkdocument/)

HERE = os.path.dirname(os.path.abspath(__file__))
UIT = os.path.join(HERE, "WP3_Een-veilig-account.docx")

# Deel 1: wachtwoord, veilig?, waarom? Rij 1 = de demo, al ingevuld.
RIJEN_WACHTWOORDEN = [
    ("Nova2026!", "nee",
     "Te kort: 9 tekens. De naam van het bedrijf en een jaartal: dat probeert een computer eerst."),
    ("tompeeters", "", ""),
    ("12345678", "", ""),
    ("Drie groene vorken dansen op pallet 7!", "", ""),
]

# Deel 2a: een x bij één antwoord
ANTWOORDEN_2A = [
    "Zijn e-mail wordt trager.",
    "Wie het briefje leest, kan ook in Toms e-mail.",   # juist
    "Er is geen gevaar: het wachtwoord heeft een hoofdletter, cijfers en een teken.",
]

# Deel 2b: weet, hebt of bent? Rij 1 = de voorbeeldrij, al ingevuld.
RIJEN_BEWIJS = [
    ("je pincode", "iets wat je weet"),
    ("een code op je gsm", ""),
    ("je vingerafdruk", ""),
    ("je wachtwoord", ""),
]

# Deel 4a: een x bij één antwoord; 4b: een x bij de drie juiste
ANTWOORDEN_4A = [
    "Wachten: misschien gaat het vanzelf over.",
    "Zijn wachtwoord naar een collega sturen, die kan eens kijken.",
    "Zijn wachtwoord meteen veranderen.",   # juist
]
ANTWOORDEN_4B = [
    "Tweestapsverificatie aanzetten.",   # juist
    "Zijn nieuwe wachtwoord op een briefje aan zijn scherm kleven.",
    "Uitloggen bij het onbekende toestel.",   # juist
    "Hetzelfde nieuwe wachtwoord ook voor zijn andere accounts gebruiken.",
    "NovaDepot verwittigen: het is zijn werkaccount.",   # juist
]

# De criteria van lesvoorbereiding § 22 (samen 20)
CRITERIA = [
    ("Deel 1: ik beoordeelde de drie wachtwoorden juist, met een reden die klopt.", 3),
    ("Deel 1: mijn wachtwoordzin heeft minstens 15 tekens en minstens 4 woorden, zonder naam, bedrijf of jaartal.", 3),
    ("Deel 2: ik koos het gevaar van overal hetzelfde wachtwoord.", 1),
    ("Deel 2: ik schreef bij de drie voorbeelden weet, hebt of bent.", 2),
    ("Deel 2: ik legde uit waarom het briefje niet volstaat als tweestapsverificatie aan staat.", 2),
    ("Deel 3: ik schreef op op welke knop Tom klikt, en welke toetsen ik druk als ik even wegga.", 4),
    ("Deel 4: ik koos wat Tom eerst doet, en de drie juiste acties daarna.", 5),
]


def kruisvakken(doc, antwoorden):
    """Een x typen in het vak links van het antwoord."""
    return hs.tabel(doc, ["Een x bij", "Antwoord"], [("", a) for a in antwoorden], [2.4, 14.6],
                    invul=(0,), rijhoogte=0.95)


def werkdocument():
    """In de huisstijl van 12-10-2026 (huisstijl.py): alleen wat de leerling invult, en de feiten die hij
    daarvoor nodig heeft. Hoe hij werkt, staat op de lespagina."""
    doc = hs.nieuw_document()
    doc.core_properties.title = "WP3 Een veilig account - werkdocument"
    doc.core_properties.author = "Toegepaste Informatica"
    hs.kopblok(doc, "EEN VEILIG ACCOUNT", punten=20)

    hs.kader(doc, "De veiligheidsronde van Sara", [
        "Sara Claes van de preventiedienst van NovaDepot deed een veiligheidsronde in het magazijn. "
        "Ze vond drie dingen:",
        ("1.", "Op het scherm van de magazijn-pc kleeft een briefje met het wachtwoord Nova2026!"),
        ("2.", "Tom Peeters (magazijn) gebruikt hetzelfde wachtwoord ook voor zijn e-mail."),
        ("3.", "Op de tablet aan de laadkaai staat het account van Tom nog open."),
    ])

    hs.deel(doc, 1, "Het briefje", punten=6)
    hs.tabel(doc, ["Wachtwoord", "Veilig? (ja of nee)", "Waarom?"], RIJEN_WACHTWOORDEN, [5.6, 3.0, 8.4],
             invul=(1, 2), rijhoogte=1.3, voorbeeld_rij=1)
    hs.vraag(doc, "Maak een wachtwoordzin voor de nieuwe magazijn-pc: minstens 15 tekens en minstens 4 woorden.")
    hs.antwoordvak(doc, 1.5)
    hs.tekst(doc, "Dit is een oefening. Een echt wachtwoord schrijf je nooit op, ook niet in een document.",
             klein=True, cursief=True)

    hs.deel(doc, 2, "Overal hetzelfde", punten=5, nieuwe_pagina=True)
    hs.vraag(doc, "a. Tom gebruikt Nova2026! ook voor zijn e-mail. Wat is het gevaar?")
    kruisvakken(doc, ANTWOORDEN_2A)
    hs.vraag(doc, "b. Is het iets wat je weet, iets wat je hebt of iets wat je bent?")
    hs.tabel(doc, ["Bewijs", "Iets wat je weet, hebt of bent?"], RIJEN_BEWIJS, [6.0, 11.0],
             invul=(1,), rijhoogte=0.95, voorbeeld_rij=1)
    hs.vraag(doc, "c. Iemand leest het briefje met het wachtwoord van Tom. Tom heeft tweestapsverificatie aan. "
                  "Kan die persoon inloggen op het account van Tom? Leg uit.")
    hs.antwoordvak(doc, 2.2)

    hs.deel(doc, 3, "De tablet aan de laadkaai", punten=4)
    hs.vraag(doc, "a. Tom ziet in zijn Google-account de tablet van de laadkaai nog in de lijst. "
                  "Op welke knop klikt hij?")
    hs.antwoordvak(doc, 1.2)
    hs.vraag(doc, "b. Je gaat even weg van een computer die ook van anderen is. Welke toetsen druk je?")
    hs.antwoordvak(doc, 1.2)

    hs.deel(doc, 4, "Gehackt?", punten=5)
    hs.kader(doc, "Een mail voor Tom", [
        "Tom krijgt een mail: “Nieuwe aanmelding op je account, op een onbekend toestel.” "
        "Hij was het niet.",
    ])
    hs.vraag(doc, "a. Wat doet Tom eerst?")
    kruisvakken(doc, ANTWOORDEN_4A)
    hs.vraag(doc, "b. Wat doet hij daarna? Een x bij de drie juiste.")
    kruisvakken(doc, ANTWOORDEN_4B)

    hs.deel(doc, None, "Nalezen")
    # eerst het codewoord van de zelftest (15-10-2026): de lespagina toont het pas als de drie vragen van stap 5
    # juist zijn; zo ziet Jonas wie de zelftest echt maakte (_afspraken/lespagina.md, De laatste stap)
    hs.vraag(doc, "Het codewoord van de zelftest (stap 5 op de lespagina):")
    hs.antwoordvak(doc, 0.9)
    hs.controletabel(doc, CRITERIA)

    doc.save(UIT)


if __name__ == "__main__":
    werkdocument()
    print("Klaar.")
    print("  werkdocument om in te leveren : " + os.path.basename(UIT))
