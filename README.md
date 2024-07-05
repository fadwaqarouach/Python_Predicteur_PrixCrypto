 *Prédicteur de Prix de Cryptomonnaies :*
Cette application Python récupère les prix historiques des cryptomonnaies en utilisant l'API CryptoCompare, effectue une régression linéaire pour prédire les prix futurs, et visualise à la fois les prix historiques et prédits dans une interface graphique (GUI) créée avec tkinter.

 *Fonctionnalités :*
- Récupération des Données: Récupère les prix historiques des cryptomonnaies depuis CryptoCompare.
- Régression Linéaire: Utilise l'apprentissage machine (régression linéaire) pour prédire les prix futurs basés sur les données historiques.
- Interface Graphique: Permet aux utilisateurs de sélectionner une cryptomonnaie, une devise, le nombre de jours historiques et le nombre de jours futurs à prédire.
- Visualisation: Trace les prix historiques, les prix prédits et met en évidence les points les plus hauts et les plus bas.
 *Bibliothèques Utilisées :*
- requests: Pour effectuer des requêtes HTTP pour récupérer les données des cryptomonnaies.
- pandas: Pour la manipulation des données et la gestion des séries temporelles.
- matplotlib et seaborn: Pour le tracé des graphiques et la visualisation des données.
- sklearn: Pour implémenter la régression linéaire.
- tkinter: Pour créer l'interface graphique utilisateur.
