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
