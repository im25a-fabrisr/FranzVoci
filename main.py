import random
vokabeln = {
    "die Natur schützen": "protéger la nature",
    "die Natur verschmutzen": "polluer la nature",
    "der Umweltschutz": "la protection de l'environnement",
    "die Umweltverschmutzung": "la pollution de l'environnement",
    "das Land (ländlich)": "la campagne",
    "der Fluss": "la rivière",
    "der Wald": "la forêt",
    "die Wüste": "le désert",
    "die Pflanze": "la plante",
    "die Blume": "la fleur",
    "ein Baum": "un arbre",
    "die Naturkatastrophe": "la catastrophe naturelle",
    "der Klimawandel": "le changement climatique",
    "der Abfalleimer": "la poubelle",
    "der Müll / Abfall": "les déchets",
    "giftig": "toxique",
    "atmen": "respirer",
    "die Konsumgesellschaft": "la société de consommation",
    "schädlich für die Umwelt sein": "être nuisible à l'environnement",
    "die Abgase": "le gaz des voitures",
    "Wasser vergeuden": "gaspiller de l'eau",
    "auf etwas verzichten": "renoncer à qc",
    "Abfall sortieren / recyclen": "trier / recycler des déchets",
    "öffentliche Verkehrsmittel benutzen": "utiliser les transports publics",
    "das Licht ausschalten": "éteindre la lumière",
    "erneuerbare Energien": "les énergies renouvelables",
    "Sonnenenergie": "l'énergie solaire",
    "Windenergie": "l'énergie du vent",
    "ziemlich": "assez",
    "sich verstecken": "se cacher",
    "verliebt": "amoureux/amoureuse",
    "bewegt / berührt": "ému/émue",
    "unruhig / aufgewühlt": "agité/agitée",
    "die Umwelt": "l'environnement",
    "zerstören": "détruire",
    "die Zerstörung": "la destruction",
    "die Landschaft": "le paysage",
    "der Berg": "la montagne",
    "der See": "le lac",
    "beeindruckend": "impressionnant/impressionnante",
    "Angst haben": "avoir peur",
    "ein Verkehrsmittel": "un moyen de transport",
    "eine Strecke": "un trajet",
    "acht Stunden brauchen": "mettre huit heures",
    "aussteigen": "descendre de",
    "ziehen": "tirer",
    "gefährlich": "dangereux/dangereuse",
    "das Leben": "la vie",
    "verhaften": "arrêter",
    "genug haben von": "en avoir assez",
    "die Gesundheit": "la santé",
    "die Kriminalität": "la criminalité",
    "dicht": "dense",
    "sich verirren": "se perdre",
    "was ... betrifft": "en ce qui concerne",
    "die Wirtschaft": "l'économie",
    "feststellen": "constater",
    "wirtschaftlich": "économique",
    "trinken": "boire",
    "etwas": "quelque chose",
    "endgültig": "définitif/définitive",
    "schließen": "fermer",
    "schockierend": "choquant/choquante",
    "darstellen": "représenter",
    "ein Polizist": "un gendarme",
    "eine Brücke": "un pont",
    "die Herkunft": "l'origine",
    "überqueren": "traverser",
    "ein Jahrhundert": "un siècle",
    "ein Viertel": "un quart",
    "die Hälfte": "la moitié",
    "ein Drittel": "un tiers",
    "Mobbing": "le harcèlement",
    "müde": "fatigué/fatiguée",
    "sich kümmern um": "s'occuper de",
    "sich fühlen": "se sentir",
    "aufstehen": "se lever",
    "manchmal": "parfois",
    "sich waschen": "se laver",
    "sich anziehen": "s'habiller",
    "fröhlich": "joyeux/joyeuse",
    "übertreiben": "exagérer",
    "aufwachen": "se réveiller",
    "sich einloggen in": "se connecter à",
    "das Gedächtnis": "la mémoire",
    "einstellen (Job)": "embaucher",
    "behalten": "garder",
    "verantwortungsbewusst": "responsable",
    "ernsthaft": "sérieux/sérieuse",
    "lügen": "mentir",
    "vorsichtig": "prudent/prudente",
    "sich in Acht nehmen vor": "se méfier de"
}


def trainer():
    items = list(vokabeln.items())
    random.shuffle(items)

    score = 0
    print("--- Französisch Vokabeltrainer ---")
    print("Befehle: 'q' = Ende, 'r' = Meine Antwort war doch richtig\n")

    for deutsch, franz in items:
        print(f"Deutsch: {deutsch}")
        user_input = input("Französisch: ").strip()

        if user_input.lower() == 'q':
            break

        if user_input.lower() == franz.lower():
            print("✅ Richtig!")
            score += 1
        else:
            print(f"❌ Falsch. Lösung: {franz}")
            check = input("War es trotzdem richtig? (r drücken für JA, Enter für NEIN): ").lower()
            if check == 'r':
                print("Ok, korrigiert! ✅")
                score += 1
        print("-" * 30)

    print(f"\nTraining beendet! Dein Score: {score}/{len(vokabeln)}")


if __name__ == "__main__":
    trainer()