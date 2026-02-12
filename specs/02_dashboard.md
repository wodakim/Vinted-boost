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
