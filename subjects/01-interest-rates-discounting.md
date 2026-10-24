# Sujet 01 — Théorie des taux d'intérêt, actualisation et taux forward

**Niveau :** Master 2 avancé / doctorat (initiation)  
**Source principale :** C. Alexander, *Market Risk Analysis*, vol. III, § III.1.2.1–III.1.2.5 (pp. 2–8).  
**Approfondissements :** Björk (absence d’arbitrage), Tuckman–Serrat (conventions), Brigo–Mercurio (modèles de taux).  
**Données empiriques :** estimations officielles BCE des taux spot zéro-coupon AAA en zone euro.  
**Statut :** énoncé à résoudre ; aucune solution n'est présentée comme achevée.

## Problématique
Sous quelles hypothèses les taux spot, forward, simples, composés et continus sont-ils des représentations cohérentes des mêmes prix de marché, et quelles relations sont imposées par l'absence d'arbitrage ?

**Cadre :** dates 0 ≤ S < T en années, nominal N, valeur future V(T), facteur D(0,T)>0 avec D(0,0)=1. Les taux r sont continus, les taux R discrets; les forwards f_{n,m} et F_{n,m} ont pour *term* n et *tenor* m. Chaque taux doit mentionner fréquence, annualisation et convention de décompte. Ne pas assimiler forward de marché et espérance historique du taux futur. Les scénarios initiaux sont déterministes, sans défaut ni frictions; l'emprunt et le prêt au même taux sont admis pour démontrer les relations d'absence d'arbitrage. Ne pas assimiler une courbe de taux souverains AAA estimés à une courbe OIS collatéralisée.

## Partie A — Fondements (15 points)
A1. Définir intérêt simple et intérêt composé; établir les facteurs d'accumulation et d'actualisation.  
A2. À partir d'un taux nominal annuel R, démontrer la convergence de (1+R/m)^(mT) vers exp(RT), avec les conditions de positivité.  
A3. Résoudre V'(t)=r(t)V(t) pour une fonction intégrable r(t); déduire la formule de capitalisation.  
A4. Analyser les dimensions et unités; distinguer maturité, *term*, *tenor* et période d'accumulation avec une frise chronologique.  
A5. Expliquer quelles hypothèses justifient A(0,T)=1/D(0,T). Distinguer D(0,T) et D(t,T) et interpréter leur signification financière.

## Partie B — Spot et forward continus (20 points)
B1. Définir r(0,T) à partir de D(0,T) et démontrer la relation de composition entre 0, S et T par deux stratégies sans arbitrage.  
B2. Déduire la formule d'un taux forward continu moyen sur [S,T]. Retrouver la relation du manuel (III.1.3) à un et deux ans.  
B3. Lorsque T↦D(0,T) est C¹, établir f(0,T)=−∂_T log D(0,T), sa forme intégrale et la relation entre spot moyen et forward instantané.  
B4. Comparer courbe spot plate, croissante et non monotone; expliquer pourquoi un forward observé aujourd'hui n'est pas automatiquement l'espérance historique d'un futur spot.  
B5. Pour les fonctions r(0,T)=a, r(0,T)=a+bT et r(0,T)=a+bT exp(−T), établir analytiquement D(0,T) et le forward instantané; les représenter.  
B6. Tester puis démontrer ou réfuter l'affirmation : « toute courbe spot croissante implique des forwards instantanés croissants ».

## Partie C — Conventions et taux équivalents (20 points)
C1. Démontrer la conversion entre taux continu r et taux nominal R capitalisé m fois par an. Préciser le domaine valide.  
C2. Montrer que des taux équivalents donnent le même facteur d'actualisation, alors que la même valeur numérique sous deux conventions n'en donne généralement pas.  
C3. Retrouver l'exemple III.1.1 du manuel (N=500, R=4 %, T=3,5 ans, capitalisation semestrielle) et comparer à une capitalisation continue au taux numérique de 4 %.  
C4. Comparer la convention hybride du manuel (III.1.11) pour une maturité non entière avec la capitalisation fractionnaire; exemple T=1,4 et R=5 %.  
C5. Calculer le nombre exact de jours entre le 15 janvier et le 17 avril 2026 puis le coupon d'un nominal de 10 M€ au taux annualisé de 3,2 % en ACT/360 et ACT/365F.  
C6. Reprendre C3 et calculer le taux continu équivalent au taux semestriel de 4 %; vérifier que ce taux produit exactement le même montant final, contrairement à un taux continu numériquement égal à 4 %.  
C7. Étudier le signe du taux et le domaine de validité des facteurs d'actualisation : D(0,T)>0 n'implique pas D(0,T)<1.

## Partie D — Spot et forward discrets (20 points)
D1. Démontrer (III.1.17), puis généraliser la relation de produit (III.1.18) du manuel.  
D2. Avec des taux spot annuels 1/2/3 ans de 5 %, 6 % et 6,5 %, calculer les forwards annuels successifs et vérifier les identités de non-arbitrage.  
D3. Pour une fraction d'année α(S,T), dériver le forward simple annualisé à partir de D(0,S)/D(0,T).  
D4. Examiner la notation F_{6,9} et les dates annoncées dans § III.1.2.4 du document. Le taux défini comme démarrant dans six mois pour un tenor neuf mois ne peut pas simultanément débuter au neuvième mois. Dessiner la chronologie correcte, identifier l'incohérence et expliquer la correction sans changer la convention de notation.  
D5. Avec des taux spot simples annualisés de 4,5 %, 4,3 %, 4,2 % et 4,0 % à 3, 6, 9 et 12 mois, retrouver les forwards 3M consécutifs et un 6M-forward démarrant à 6M; expliciter les accrual factors et les produits sans arrondir.

## Partie E — Analyse empirique sur données réelles BCE et laboratoire Python (15 points)

**Source obligatoire :** [BCE — euro area yield curves](https://www.ecb.europa.eu/stats/financial_markets_and_interest_rates/euro_area_yield_curves/html/index.en.html), [BCE — dataset YC](https://data.ecb.europa.eu/data/datasets/YC). Les taux publiés sont des **estimations zéro-coupon de titres souverains** selon Svensson, exprimées en **pourcentage annuel composé continûment**. Ils ne sont **pas** des taux OIS ou des prix d'obligations cotés individuellement à toutes les maturités.

Télécharger via le script dans scripts/download_ecb_yield_curve.py les séries AAA pour 3M, 6M, 1Y, 2Y, 3Y, 5Y, 7Y, 10Y et, en option, 15Y, 20Y, 30Y. Exemple de clé exacte : **YC.B.U2.EUR.4F.G_N_A.SV_C_YM.SR_1Y**. Période : 2026-09-01 à 2026-10-23. Date d'analyse préférée : 2026-10-22, **uniquement si toutes les séries y sont présentes** ; comparer à une seconde date commune un mois avant. Les observations **ne sont pas incluses** tant qu'une extraction réussie n'a pas été effectuée.

E1. Établir un dictionnaire des données avec identifiants des séries, dates de référence, date d'extraction, unités et observations manquantes. Montrer la conversion des données publiées en % vers le taux décimal.

E2. Développer discount_continuous, discount_simple, discount_compound, nominal_to_continuous, continuous_to_nominal, forward_continuous et forward_simple, avec domaines de validité et paramètres explicites.

E3. À partir des spots BCE à une date commune, reconstruire D(0,T), puis les forwards moyens sur [3M,6M], [6M,1Y], [1Y,2Y], [2Y,3Y], [3Y,5Y] et [5Y,10Y]. Pour cette première expérience fixer explicitement alpha(S,T)=T-S; indiquer pourquoi les conventions ACT réelles devront être intégrées ultérieurement.

E4. Ajouter au moins **dix tests indépendants** (réciprocité, équivalence, composition, continuité, unités, cas limites, taux négatifs admissibles et données manquantes). Fixer et justifier les tolérances.

E5. Produire quatre figures : (1) deux courbes spot BCE, (2) deux courbes de facteurs d'actualisation, (3) forwards moyens par segment, (4) mouvements historiques en points de base. Identifier clairement les taux observés, les taux calculés et les interpolations éventuelles.

E6. Retirer une maturité, la reconstituer par interpolation annoncée et quantifier l'écart avec le taux BCE. Expliquer pourquoi l'ajustement statistique ne suffit pas à établir l'absence d'arbitrage.

**Bonus :** comparer le taux forward instantané BCE IF_1Y ou IF_2Y avec un forward moyen sur une période finie.

**Attention :** l'ancien data/spot_curve_synthetic.csv reste uniquement un jeu de données **synthétiques de tests**, et ne doit jamais être présenté comme une observation réelle.

## Partie F — Réflexion critique (10 points)
F1. Expliquer le rôle historique de LIBOR dans § III.1.2.5 : pourquoi il ne faut pas présenter LIBOR comme référence vivante en 2026 (publication finale le 30/09/2024) ? Distinguer €STR, Euribor et taux souverains AAA. Sources : https://www.fca.org.uk/news/press-releases/end-libor ; https://www.ecb.europa.eu/stats/financial_markets_and_interest_rates/euro_short-term_rate/html/index.en.html ; https://www.emmi-benchmarks.eu/benchmarks/euribor/.  
F1bis. Retrouver un fixing quotidien vérifiable de €STR et distinguer date d'observation, date de publication et tenor.  
F2. Essai argumentatif (700–1000 mots) : « Pourquoi les facteurs d'actualisation sont-ils plus fondamentaux que les cotations de taux ? » Discuter conventions, prix, arbitrage et hypothèses du cadre.

## Livrables attendus pour marquer ce sujet terminé
1. Démonstrations et calculs personnels dans `reports/01_interest_rates.md`.
2. Fonctions Python avec signatures explicites dans `src/rates/`, accompagnées de notes d'hypothèses.
3. Tests reproductibles dans `tests/test_01_rates.py`.
4. Notebook `notebooks/01_interest_rates.ipynb`, graphes issus des séries officielles BCE et analyse des quatre graphiques.  
5. Conserver les données BCE et leur manifeste de provenance (voir data/README.md).
6. Résumé critique des résultats dans `results/01-summary.md`.

**Sources :** *Market Risk Analysis* III.1.2, équations III.1.1 à III.1.18 et exemples III.1.1–III.1.3. Travail original inspiré du chapitre et non transcription du manuel.

## Bibliographie scientifique élargie

- Carol Alexander, *Market Risk Analysis*, vol. III, § III.1.2.1–III.1.2.5 : trame du sujet, terminologie, exemples III.1.1–III.1.3 et relations III.1.1–III.1.18.
- Tomas Björk, *Arbitrage Theory in Continuous Time*, 4e éd. : approfondissement de la logique sans arbitrage, sans importer sans justification les hypothèses stochastiques plus avancées.
- Bruce Tuckman et Angel Serrat, *Fixed Income Securities* : conventions de marché et interprétations.
- Damiano Brigo et Fabio Mercurio, *Interest Rate Models: Theory and Practice* : extension ultérieure aux cadres de taux avancés.
- BCE : [Yield curves — methodology](https://data.ecb.europa.eu/methodology/yield-curves) et [YC dataset](https://data.ecb.europa.eu/data/datasets/YC).
- FCA : [The end of LIBOR](https://www.fca.org.uk/news/press-releases/end-libor).

**Condition de validation :** aucune partie n'est déclarée terminée sans preuves, tests vérifiés et données correctement sourcées. Les calculs restent à réaliser par l'étudiant.
