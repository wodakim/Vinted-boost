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
