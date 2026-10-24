# Sujet 01 — Théorie des taux d'intérêt, actualisation et taux forward

**Niveau :** Master 2 avancé / doctorat (initiation)  
**Source :** Carol Alexander, *Market Risk Analysis*, vol. III, § III.1.2.1–III.1.2.5  
**Statut :** énoncé à résoudre ; aucune solution n'est présentée comme achevée.

## Problématique
Sous quelles hypothèses les taux spot, forward, simples, composés et continus sont-ils des représentations cohérentes des mêmes prix de marché, et quelles relations sont imposées par l'absence d'arbitrage ?

**Cadre :** dates 0 ≤ S < T en années, nominal N, valeur future V(T), facteur D(0,T)>0 avec D(0,0)=1. Les taux r sont continus, les taux R discrets; les forwards f_{n,m} et F_{n,m} ont pour *term* n et *tenor* m. Chaque taux doit mentionner fréquence, annualisation et convention de décompte. Ne pas assimiler forward de marché et espérance historique du taux futur. Les scénarios initiaux sont déterministes.

## Partie A — Fondements (15 points)
A1. Définir intérêt simple et intérêt composé; établir les facteurs d'accumulation et d'actualisation.  
A2. À partir d'un taux nominal annuel R, démontrer la convergence de (1+R/m)^(mT) vers exp(RT), avec les conditions de positivité.  
A3. Résoudre V'(t)=r(t)V(t) pour une fonction intégrable r(t); déduire la formule de capitalisation.  
A4. Analyser les dimensions et unités; distinguer maturité, *term*, *tenor* et période d'accumulation avec une frise chronologique.

## Partie B — Spot et forward continus (20 points)
B1. Définir r(0,T) à partir de D(0,T) et démontrer la relation de composition entre 0, S et T par deux stratégies sans arbitrage.  
B2. Déduire la formule d'un taux forward continu moyen sur [S,T]. Retrouver la relation du manuel (III.1.3) à un et deux ans.  
B3. Lorsque T↦D(0,T) est C¹, établir f(0,T)=−∂_T log D(0,T), sa forme intégrale et la relation entre spot moyen et forward instantané.  
B4. Comparer courbe spot plate, croissante et non monotone; expliquer pourquoi un forward observé aujourd'hui n'est pas automatiquement l'espérance historique d'un futur spot.

## Partie C — Conventions et taux équivalents (20 points)
C1. Démontrer la conversion entre taux continu r et taux nominal R capitalisé m fois par an. Préciser le domaine valide.  
C2. Montrer que des taux équivalents donnent le même facteur d'actualisation, alors que la même valeur numérique sous deux conventions n'en donne généralement pas.  
C3. Retrouver l'exemple III.1.1 du manuel (N=500, R=4 %, T=3,5 ans, capitalisation semestrielle) et comparer à une capitalisation continue au taux numérique de 4 %.  
C4. Comparer la convention hybride du manuel (III.1.11) pour une maturité non entière avec la capitalisation fractionnaire; exemple T=1,4 et R=5 %.  
C5. Calculer le décompte d'une période de 92 jours en ACT/360 et ACT/365F; quantifier l'écart d'actualisation sur un flux donné.

## Partie D — Spot et forward discrets (20 points)
D1. Démontrer (III.1.17), puis généraliser la relation de produit (III.1.18) du manuel.  
D2. Avec des taux spot annuels 1/2/3 ans de 5 %, 6 % et 6,5 %, calculer les forwards annuels successifs et vérifier les identités de non-arbitrage.  
D3. Pour une fraction d'année α(S,T), dériver le forward simple annualisé à partir de D(0,S)/D(0,T).  
D4. Examiner la notation F_{6,9} et les dates annoncées dans § III.1.2.4 du document. Expliciter la cohérence exigée entre *term*, *tenor* et fin de période.

## Partie E — Laboratoire Python (15 points)
Utiliser `data/spot_curve_synthetic.csv`. Données synthétiques, non représentatives de cotations. Considérer `continuous_spot_rate` comme entrée fondamentale ; l'autre colonne est arrondie.

E1. Écrire et documenter `discount_continuous`, `discount_simple`, `continuous_to_nominal` et les fonctions inverses; contrôler les domaines.  
E2. Calculer les facteurs d'actualisation et forwards moyens consécutifs en continu et en simple, avec accrual factors explicités.  
E3. Vérifier D(0,0)=1, l'équivalence des conventions, l'inversion accumulation–actualisation et les décompositions forwards. Ajouter au moins six tests automatisés indépendants.  
E4. Tracer et commenter quatre graphiques : courbe spot, discount factors, forwards par segment, erreur issue d'une confusion des conventions.  
E5. Inclure un scénario de taux négatifs et examiner pourquoi la positivité n'exige pas une décroissance de D(0,T).

## Partie F — Réflexion critique (10 points)
F1. Expliquer le rôle historique de LIBOR dans § III.1.2.5, puis distinguer le cadre du manuel de la transition vers les indices overnight contemporains (FCA: https://www.fca.org.uk/markets/libor-transition).  
F2. Essai argumentatif (700–1000 mots) : « Pourquoi les facteurs d'actualisation sont-ils plus fondamentaux que les cotations de taux ? » Discuter conventions, prix, arbitrage et hypothèses du cadre.

## Livrables attendus pour marquer ce sujet terminé
1. Démonstrations et calculs personnels dans `subjects/solutions/01-report.md`.
2. Fonctions Python avec signatures explicites dans `src/`.
3. Tests reproductibles dans `tests/test_01_rates.py`.
4. Notebook `notebooks/01-experiments.ipynb` et analyse des quatre graphiques.
5. Résumé critique des résultats dans `results/01-summary.md`.

**Sources :** *Market Risk Analysis* III.1.2, équations III.1.1 à III.1.18 et exemples III.1.1–III.1.3. Travail original inspiré du chapitre et non transcription du manuel.
