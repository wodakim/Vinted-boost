## CHAPITRE 4 : GÉNÉRATEUR D'ANNONCE SEO (PROCÉDURAL)

Ce module est le cœur "Business" de l'application. Il transforme des données brutes (Marque, Type, Couleur) en une description de vente optimisée pour l'algorithme Vinted, tout en s'adaptant à la langue et au style de l'utilisateur.

### 4.1 Logique de Génération Procédurale
Le générateur n'utilise pas de templates statiques, mais assemble dynamiquement des blocs de texte.

*   **Styles Disponibles** (Accessibles via menu déroulant) :
    1.  **Casual** : Ton amical, standard Vinted ("Coucou !").
    2.  **Pro** : Ton factuel, boutique, rassurant ("Article authentique").
    3.  **Emoji Max** : Visuel, accrocheur, pour la Gen Z ("✨ PÉPITE 🔥").
    4.  **Storytelling** : Émotionnel, crée une connexion ("Coup de foudre").
    5.  **Minimaliste** : Efficace, mots-clés purs ("Vente rapide").
*   **Moteur d'Assemblage (`updateSeoPreview`)** :
    Le texte final est une concaténation de 5 composants, piochés aléatoirement dans le jeu de données du style choisi :
    1.  **Hook (Accroche)** : La première phrase cruciale pour le CTR.
    2.  **Reason (Body)** : La raison de la vente (rassure sur l'origine).
    3.  **Specs (État)** : Description technique de la condition.
    4.  **Details** : Insertion des champs libres (Matière, Couleur) avec des puces.
    5.  **Closing (Appel à l'action)** : Incitation à l'achat ou au lot.
*   **Interpolation** :
    Une fonction `fillTemplate` remplace les placeholders `{brand}`, `{type}`, `{color}`, etc., par les saisies de l'utilisateur.

### 4.2 Score de Titre en Temps Réel
Un algorithme note la qualité du titre sur 100 points pour éduquer l'utilisateur au SEO.

*   **Critères de Notation** :
    *   **Longueur** : > 10 caractères (+20 pts).
    *   **Mots-clés** : Présence de la Marque (+20), du Type (+20).
    *   **Détails** : Présence de Couleur, Matière, État (+10 chacun).
    *   **Bonus** : Champ "Style/Vibe" rempli (+10).
*   **Pénalités** :
    *   Utilisation de mots subjectifs vides de sens SEO comme "joli", "sympa", "mignon" (-10 pts).
*   **Feedback Visuel** :
    *   Barre de progression colorée (Rouge < 40, Jaune < 80, Vert > 80).
    *   Conseils textuels dynamiques ("Manque la marque !", "Titre trop court").

### 4.3 Gestion des Hashtags & Tendances
Le module aide à catégoriser l'article via des tags pertinents.

*   **Packs Experts (2026)** :
    Listes pré-configurées pour cibler des niches esthétiques (Core) :
    *   *Gorpcore* (Techwear, Rando).
    *   *Office Siren* (Look bureau 90s/00s).
    *   *Coquette* (Nœuds, Romantique).
    *   *Old Money* (Luxe discret).
    *   *Y2K* (Années 2000).
*   **Librairie Rapide** : Boutons pour ajouter des tags courants (#vintage, #cuir, #ete) en un clic.
*   **Logique** : Ajout unique (pas de doublons) et limite à 15 tags pour éviter le spamming algorithmique.

### 4.4 UX "Extreme Guidance"
Pour aider les utilisateurs TDAH/Dys à remplir le formulaire sans anxiété :
*   **Placeholders Contextuels** : Traduits (ex: "Marque", "Brand").
*   **Micro-Guidance** : Sous chaque champ, un texte `<small class="guidance">` donne un exemple concret et traduit (ex: "Ex: Zara, Sézane" en FR, "Ex: Nike" en EN).
*   **Bouton "Remix Magique"** : Permet de régénérer une nouvelle variante du texte sans changer les données, idéal si le premier jet ne plaît pas.
