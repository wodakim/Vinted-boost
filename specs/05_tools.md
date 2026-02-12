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
