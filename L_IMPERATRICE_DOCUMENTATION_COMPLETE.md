# DOCUMENTATION TECHNIQUE : L'IMPÉRATRICE
## CHAPITRE 1 : ARCHITECTURE & SYSTÈMES CENTRAUX

### 1.1 Architecture Globale
L'application repose sur une architecture **"Single-File Monolith" (Monolithe Fichier Unique)**, conçue pour une portabilité maximale et une résilience totale (fonctionnement hors ligne).

*   **Format** : Fichier unique `index.html` intégrant HTML, CSS et JavaScript.
*   **Dépendances** : Aucune (Zero-Dependency). Utilisation exclusive de Vanilla JS (ES6+) et CSS3.
*   **Compatibilité** : Navigateurs modernes (Chrome, Firefox, Safari, Edge).
*   **Mode de Distribution** : Fichier local (double-clic) ou hébergement statique simple.

### 1.2 Système de Stockage & Persistance (Local-First)
L'application utilise le `localStorage` du navigateur pour sauvegarder l'état utilisateur. Aucune donnée ne transite par un serveur (Privacy by Design).

| Clé Stockage | Type | Description |
| :--- | :--- | :--- |
| `app_lang` | String | Langue active ('fr', 'en', 'de', 'es', 'it', 'pl'). |
| `theme` | String | Thème visuel ('light' ou 'dark'). |
| `spoons` | Integer | Nombre de cuillères d'énergie restantes (0-12). |
| `spoons_date` | String | Date de la dernière réinitialisation des cuillères (Format Date String). |
| `packing_state` | JSON Array | Indices des cases cochées dans la checklist colis (ex: `[0, 2, 5]`). |
| `crush_highscore` | Integer | Meilleur score au jeu "Crush". |
| `unlocked_trophies` | JSON Array | Liste des IDs des succès débloqués (ex: `['first_visit', 'dark_mode']`). |

### 1.3 Design System & Thèmes (CSS)
Le style est géré via des **Variables CSS (Custom Properties)** définies dans `:root`. Le design est "Neuro-Inclusif", privilégiant la douceur et la lisibilité.

*   **Mode Clair (Défaut)** : Palette "Pastel/Feminine".
    *   `--bg-color`: Lavender Blush (`#FFF0F5`)
    *   `--primary-color`: Thistle (`#D8BFD8`)
    *   `--accent-color`: Lavender (`#E0BBE4`)
*   **Mode Sombre (Sensory Friendly)** : Palette "Slate/Mauve" pour réduire la fatigue oculaire.
    *   `--bg-color`: Dark Slate (`#2D2D3A`)
    *   `--text-main`: Off-White (`#E0E0E0`) pour éviter le contraste violent #FFF/#000.
*   **Composants UI** :
    *   Boutons arrondis (`border-radius: 20px` ou `50%` pour les icônes).
    *   Ombres douces (`--shadow-soft`) pour la profondeur sans bruit visuel.
    *   Animations : Transitions fluides (`0.3s`) et `fadeIn` lors des changements d'onglets.

### 1.4 Moteur d'Internationalisation (i18n)
Le système gère 6 langues (FR, EN, DE, ES, IT, PL) via un objet unique `i18nData`.

*   **Structure de Données** :
    ```javascript
    const i18nData = {
        fr: {
            "nav_home": "Accueil",
            "seo_data": { ... }, // Objets complexes pour le générateur
            // ... ~200 clés
        },
        en: { ... }
    };
    ```
*   **Logique de Changement (`changeLanguage`)** :
    1.  Mise à jour de la variable d'état `currentLang`.
    2.  Sauvegarde dans `localStorage`.
    3.  **Remplacement Statique** : Injection directe dans le DOM pour les éléments avec l'attribut `data-i18n` ou `data-placeholder-i18n`.
    4.  **Mise à jour Dynamique** : Appel des fonctions de rendu des composants (Studio, Calendrier, Conseils).
    5.  **Reload Popup** : Affichage d'une modale demandant le rechargement de la page pour assurer la propagation complète des changements (sauf initialisation silencieuse).

### 1.5 Système de Navigation
L'interface simule une application native via un système d'onglets (SPA).

*   **Barre de Navigation** : `nav-tabs` défilable horizontalement sur mobile.
*   **Gestion des Vues** :
    *   Les sections (`.section-view`) sont cachées par défaut (`display: none`).
    *   La fonction `switchTab(id)` applique la classe `.active` à la section cible.
    *   Animation CSS `fadeIn` (0.5s) à l'apparition pour une transition douce.
*   **Hooks** : Le changement d'onglet déclenche des événements secondaires (ex: déblocage de trophées "Explorateur", boost de dopamine aléatoire).
## CHAPITRE 2 : TABLEAU DE BORD & WIDGETS

Le tableau de bord ("Accueil") est le centre de commande de l'utilisateur. Il regroupe trois widgets essentiels conçus pour optimiser la performance de vente tout en préservant la santé mentale.

### 2.1 Widget "Mes Cuillères" (Gestion de l'Énergie)
Basé sur la "Théorie des Cuillères", ce module aide les utilisateurs neuroatypiques à visualiser et gérer leur stock d'énergie quotidien.

*   **Logique de Fonctionnement** :
    *   **Stock Initial** : 12 Cuillères par jour.
    *   **Reset** : Automatique si la date stockée (`spoons_date`) diffère de la date actuelle (`new Date().toDateString()`).
    *   **Interaction** :
        *   Cliquer sur une cuillère pleine la "consomme" (la grise).
        *   Cliquer sur une cuillère vide la "restaure".
        *   La mise à jour est immédiate via `updateSpoonCount(n)` et persistée dans `localStorage`.
*   **Feedback Visuel** :
    *   Les cuillères actives sont colorées (`var(--primary-dark)`).
    *   Les cuillères consommées sont grisées (opacité 0.3).
*   **Conseils Contextuels (i18n)** :
    *   **> 8 Cuillères (High)** : "Tu as de l'énergie ! Attaque les photos ou les mises en ligne."
    *   **> 4 Cuillères (Mid)** : "Énergie modérée. Fais des colis ou réponds aux messages."
    *   **< 4 Cuillères (Low)** : "Batterie faible. Repose-toi ou fais juste de la veille."

### 2.2 Widget "Chronobiologie" (Stratégie Temporelle)
Ce module indique le meilleur moment pour publier une annonce en fonction de l'heure actuelle et du jour de la semaine, maximisant ainsi la visibilité algorithmique.

*   **Algorithme de Slots (Créneaux Optimaux)** :
    Les créneaux sont définis jour par jour (0 = Dimanche, 1 = Lundi...) :
    *   **Dimanche (Jour fort)** : 10h-12h et 18h-21h (Prime Time absolu).
    *   **Lundi** : 07h-09h et 19h-21h.
    *   **Mercredi (Jour des enfants)** : 12h-14h et 18h-20h.
    *   **Vendredi** : 13h-16h et 20h-23h (Effet "Pré-Sortie/Paie").
    *   **Samedi** : 09h-11h et 17h-19h.
    *   **Mardi/Jeudi** : 19h-21h (Jours plus calmes).
*   **États du Widget** :
    1.  **PRIME (Rouge/Chaud)** : L'heure actuelle est dans un slot optimal. Message : "C'EST LE MOMENT ! Poste maintenant !".
    2.  **GOOD (Violet)** : L'heure actuelle est dans les 2 heures précédant un slot. Message : "Bientôt le pic (XXh). Finis tes photos !".
    3.  **NEUTRAL (Gris)** : Hors créneau. Message : "Moment calme. Prépare tes brouillons."
*   **Conseil Saisonnier** :
    En plus de l'heure, un conseil basé sur le mois courant est affiché (ex: "En Juillet : Soldes & Maillots"). Ces conseils sont traduits via les clés `tip_autumn`, `tip_winter`, etc.

### 2.3 Widget "Conseil du Jour" (Motivation)
Un élément de type "Post-it" rotatif pour maintenir la motivation et l'éducation continue.

*   **Mécanisme** :
    *   Sélection d'un conseil dans un tableau de ~10 entrées (`i18nData[lang].tips`).
    *   La sélection est pseudo-aléatoire mais stable pour la journée : `tips[dayOfMonth % tips.length]`. Cela garantit que tous les utilisateurs voient le même conseil le même jour, créant un sentiment de cohérence.
*   **Contenu** :
    Les conseils couvrent la psychologie de vente ("Ne baisse jamais le prix de plus de 10% d'un coup"), la logistique ("Un emballage soigné fidélise"), et l'algorithme ("L'algo adore la régularité").
*   **Design** :
    Style "Post-it" jaune, légèrement incliné (`rotate(-1deg)`), avec une punaise virtuelle, pour un aspect ludique et non-corporate.
## CHAPITRE 3 : MODULE STUDIO PHOTO VIRTUEL

Le "Studio Virtuel" est un guide interactif étape par étape conçu pour standardiser la prise de vue, un facteur critique pour l'algorithme de reconnaissance d'image de Vinted.

### 3.1 Architecture des Données (`getPhotoStudioData`)
Le contenu du studio est structuré par catégorie d'article. Chaque catégorie possède une suite d'étapes optimisée.

*   **Catégories Supportées** :
    1.  **Vêtements** (`cat_clothes`) : Focus sur la silhouette et les étiquettes.
    2.  **Chaussures** (`cat_shoes`) : Focus sur les semelles et les talons.
    3.  **Sacs** (`cat_bags`) : Focus sur les coins (usure) et l'intérieur.
*   **Structure d'une Étape** :
    ```javascript
    {
        id: 'cover',
        title: "Le Hook Visuel",        // Titre affiché
        description: "...",             // Instruction concrète
        algoSecret: "...",              // "Pourquoi" algorithmique (ex: +40% CTR)
        icon: "camera"                  // Icône SVG associée
    }
    ```

### 3.2 Interface "Pro Mode"
L'interface rompt avec les listes classiques pour offrir une expérience immersive.

*   **Composants Visuels** :
    *   **Carte Centrale** : Affiche l'étape en cours avec une grande icône et une instruction claire.
    *   **Zone "Secret Algorithmique"** : Un encart sombre (`#2D2D3A`) en bas de la carte révèle pourquoi cette photo est importante (ex: "L'OCR lit l'étiquette pour valider la marque"). Cela éduque l'utilisateur tout en le guidant.
    *   **Barre de Progression** : Des points (dots) indiquent l'avancement. Le point courant est agrandi (`scale(1.5)`).
*   **Navigation** :
    *   Bouton "Je valide cette étape" (Action principale).
    *   Bouton "Étape suivante" (Apparaît après validation pour laisser le temps de lire le feedback).
    *   Bouton "Quitter" pour revenir au choix de la catégorie.

### 3.3 Workflow & Gamification
1.  **Sélection** : L'utilisateur choisit sa catégorie.
2.  **Shooting** : Il suit les ~5 étapes. À chaque validation (`completeStep()`) :
    *   L'étape est marquée comme complétée dans l'état local.
    *   Le bouton change de couleur (Vert Succès).
    *   Le système passe automatiquement à l'étape suivante après un court délai (0.5s).
3.  **Completion (Écran de Succès)** :
    Une fois toutes les étapes finies, une vue de félicitations s'affiche avec :
    *   Un message de succès traduit (`studio_success`).
    *   Un rappel des **"Derniers conseils SEO"** (Mots clés, Prix psychologique, Heure de poste).
    *   Un bouton pour recommencer un nouveau shooting.
    *   **Récompense** : Débloque le trophée "Shooting Star" (`photo_pro`) si c'est la première fois.
    *   **Dopamine** : Déclenchement de l'effet "Confetti".
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
## CHAPITRE 5 : BOÎTE À OUTILS & RESSOURCES

Cette section regroupe les utilitaires pratiques pour gérer la logistique et la communication, réduisant la charge mentale liée aux "à-côtés" de la vente.

### 5.1 Calculatrice de Profit (ROI)
Un outil simple pour visualiser instantanément la rentabilité d'une vente.

*   **Entrées** :
    *   Prix d'Achat (`calc-buy`).
    *   Prix de Vente (`calc-sell`).
    *   Frais divers (Emballage, Essence, etc.) (`calc-fees`).
*   **Calcul** :
    *   `Bénéfice = Vente - Achat - Frais`.
    *   `Marge % = (Bénéfice / Achat) * 100`.
*   **Feedback Visuel** :
    *   Le résultat s'affiche en **Vert** si positif, **Rouge** si négatif (perte), et Gris si nul.
    *   Mise à jour en temps réel (`oninput`).

### 5.2 Scripts de "Réponses Magiques" (Soft Skills)
Une bibliothèque de modèles de messages pour gérer les interactions sociales difficiles ou répétitives.

*   **Scénarios Couverts** :
    *   **Négociation** : "Offre ridicule (-50%)", "Contre-offre", "Accepter une offre".
    *   **Conflit/Politesse** : "Pas de 'Bonjour'", "Ghosting (Plus de réponse)".
    *   **Logistique** : "Retard d'envoi", "Merci & Envoi", "Réserver".
    *   **Marketing** : "Proposer un lot", "Demander un avis", "Donner les mesures".
*   **Implémentation Technique** :
    *   Les clés de sélection (`script_lowball_label`) sont séparées du contenu (`script_lowball`) dans l'objet `i18nData` pour éviter les collisions.
    *   Bouton "Copier la réponse" pour un usage immédiat.

### 5.3 Checklist "Colis Parfait"
Une liste à cocher pour ne rien oublier lors de l'emballage, garantissant une expérience acheteur 5 étoiles.

*   **Items (Traduits)** :
    *   Vêtement lavé & repassé.
    *   Pliage soigné (Marie Kondo).
    *   Protection (Papier de soie).
    *   Petit mot de remerciement (facteur clé de fidélisation).
    *   Spray parfum (neutre).
*   **Persistance** :
    L'état des cases (cochées/décochées) est sauvegardé dans `localStorage` (`packing_state`). Si l'utilisateur quitte la page, il retrouve sa liste en l'état.
*   **Récompense** : Cocher toutes les cases déclenche une notification "Colis Prêt !".

### 5.4 Calendrier Stratégique
Un widget visuel indiquant sur quoi se concentrer ce mois-ci.

*   **Double Focus** :
    1.  **À Vendre (NOW)** : Ce qui se cherche *maintenant* (ex: En Septembre -> Cartables, Jeans).
    2.  **À Préparer (NEXT)** : Ce qu'il faut shooter pour dans 3 semaines (ex: En Septembre -> Manteaux d'hiver).
*   **Données** : Tableaux statiques `season_focus` et `season_prep` indexés par mois (0-11).
## CHAPITRE 6 : GAMIFICATION, BIEN-ÊTRE & SÉCURITÉ

Pour contrer la monotonie et l'anxiété liées à la vente en ligne, l'application intègre des mécanismes de jeu et de régulation émotionnelle.

### 6.1 Système de Trophées (Gamification)
Un système de récompenses pour encourager l'exploration et l'utilisation complète de l'application.

*   **Architecture** :
    *   30 Trophées définis (ex: `first_visit`, `dark_mode`, `seo_master`, `imperatrice`).
    *   Données : ID, Icône, Nom (Traduit), Description (Traduite).
*   **Mécanisme de Déblocage** :
    *   Des "Hooks" sont placés dans les fonctions clés (`switchTab`, `toggleTheme`, `updateSeoPreview`).
    *   Lorsqu'une action est réalisée, `unlockTrophy(id)` vérifie si le succès est déjà acquis.
    *   Si nouveau : Ajout à `unlocked_trophies` (localStorage), animation visuelle (CSS classe `.unlocked`), notification Toast et pluie de confettis.

### 6.2 Jeu "Vinted Crush Infini" (Match-3)
Un mini-jeu intégré pour "tuer le temps" ou se récompenser après une session de mise en ligne.

*   **Gameplay** : Grille 8x8 de type "Candy Crush" avec des icônes Vinted (Robe, Chaussure, Colis).
*   **Contrôles** :
    *   **Desktop** : Drag & Drop (HTML5 Drag API).
    *   **Mobile** : Toucher pour sélectionner A, puis B (ou Swipe basique).
*   **Score** :
    *   Alignement de 3 = +3 points.
    *   High Score sauvegardé dans `localStorage`.
    *   Paliers de trophées : 100 points et 500 points.

### 6.3 Zone de Décompression (Bien-être)
Outils pour gérer le stress ou la "dette de cuillères".

*   **Cohérence Cardiaque** : Un cercle animé en CSS (`@keyframes breathe`) qui guide la respiration (4s Inspire / 4s Expire) sur un cycle de 8 secondes.
*   **Minute Sourire** : Générateur de blagues aléatoires (5 par langue) pour casser la tension.

### 6.4 Module SOS (Sécurité Émotionnelle)
Un "Panic Button" accessible en permanence dans le header pour les crises d'hypersensibilité ou d'anxiété.

*   **Design** : Bouton rouge pulsant (`animation: pulse-sos`).
*   **Contenu de la Modale** :
    *   Affirmations positives immédiates ("Tu es en sécurité").
    *   **Technique d'Ancrage 5-4-3-2-1** : Guide textuel pour se reconnecter au réel (5 vues, 4 touchers, etc.).
*   **Sortie** : Bouton "Je me sens mieux" qui ferme la modale avec une transition douce et une notification bienveillante ("Douceur sur toi 🌸").

---
**FIN DE LA DOCUMENTATION TECHNIQUE**
Document généré pour le projet "L'IMPÉRATRICE".
Version : 1.0 (Final Release)
Date : 2025
