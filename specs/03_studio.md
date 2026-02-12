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
