# Roadmap L'IMPÉRATRICE - Version 2.0 (Extension Infinite)

## 1. Jeu "Vinted Crush" (Match-3 Infini)
- [ ] Moteur de jeu grille 8x8.
- [ ] Logique de match-3 (swap, check matches, cascade).
- [ ] Thème visuel : Emojis/SVG (Robe 👗, Chaussure 👠, Sac 👜, Colis 📦, Etoile ⭐, Cœur 💖).
- [ ] Score et High Score persistants.
- [ ] Animations douces (pas de flash agressif).

## 2. Système de Succès & Trophées (Gamification)
- [ ] Interface "Salle des Trophées".
- [ ] Liste de 20 succès à débloquer (ex: "Première Annonce", "Reine du SEO", "Négociatrice", "Emballage Parfait").
- [ ] Logique de déblocage (basée sur l'utilisation des autres outils).
- [ ] Effet Confetti (Canvas JS) lors du déblocage.

## 3. Nouveaux Outils Interactifs (Basés sur le Rapport)
- [ ] **Calculatrice de Profit** : Prix Vente - (Prix Achat + Emballage) = Bénéfice + Marge %.
- [ ] **Générateur de Réponses (Soft Skills)** :
    - Scénarios : "Offre Lowball", "Pas de Bonjour", "Demande Réservation", "Litige", "Retard Envoi".
    - Scripts copiables basés sur la technique du "Contre-Pivot".
- [ ] **Checklist Colis Parfait** : Liste interactive (Lavage, Repassage, Pliage, Papier Soie, Parfum, Carte, Scotch).
- [ ] **Calendrier Stratégique (Règle des 3 semaines)** :
    - Widget affichant "Quoi vendre maintenant" et "Quoi préparer pour le mois prochain".

## 4. Enrichissement UX & Dopamine
- [ ] Micro-interactions (boutons qui rebondissent).
- [ ] Messages de félicitations aléatoires ("Boost Moral").
- [ ] Notifications visuelles douces (Toast notifications).
- [ ] Intégration complète Dark Mode pour tous les nouveaux éléments.

## 5. Architecture
- [ ] Tout dans `index.html`.
- [ ] Sauvegarde `localStorage` pour tout (Score jeu, Trophées, Checklists).
