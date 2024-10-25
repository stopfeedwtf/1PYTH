# 1PYTH
Ci-joint une documentation simple des deux exercices composant le projet final 1PYTH.

# Exercice 1 - Snort

## display_board
La fonction display_board présente quelques spécificités dont l'utilisation de print(f"{i+1}", end=""), qui permet d'imprimer directement pour chaque valeur i+1 le nombre associé.
Les deux parties de la fonction display_board sous la partie principale permettent de décaler via un espace la numérotation et les traits afins qu'ils soient tout de même alignés même si le nombre n est supérieur à dix.

## possible_square
La fonction possible_square a été réalisée de sorte à ce que toutes les conditions soient remplies afin que le jeu se déroule correctement. La première partie permet de savoir si la case choisie par le joueur n'est pas out of range. La seconde partie permet de savoir si la case est occupée par un joueur. Finalement la troisième partie permet de savoir si les cases autour de celle sélectionnée dans un format orthogonal ne sont pas occupée par le joueur adverse.

## select_square
La fonctione select_square actualise la valeur avec un -1 afin que le joueur joue sur les cases à partir de 1 et non à partir de 0 comme le code le voudrait par défaut.

## main
On range l'entièreté de la fonction dans une fonction main qui comprend la totalité du programme principal afin de facilité les modifications en ajoutant simplement des sous-programmes à l'intérieur.

# Exercice 2 - Dodgem

## new_board
Ici la fonction new_board crée directement les jetons des différents joueurs sur les extrémités des listes, horizontale avec j == 0 et verticale avec i == n-1 afin que le display_board soit convenablement executé.

## display_board
La fonction display_board est la même que celle du premier jeu Snort, puisqu'elles ont le même fonctionnement d'affichage en dehors du fait qu'on ajoute le board via le new_board.

## possible_pawn
La fonction possible_pawn permet de vérifier si le pion peut se déplacer selon les règles, on vérifie dans un premier temps si les coordonées sont dans les limites du plateau. 
Dans un second temps, on vérifie si la case choisie contient bien un pion valide pour le player. 
Dans le troisième temps on vérifie selon les règles imposées au player, pour le player 1 il ne peut pas se déplacer vers le bas et pour le player 2 vers la gauche. Et dans le dernier point on vérifie si le mouvement est considéré comme valide aux yeux des règles, pour le player 1, si il peut dépasser le haut du plateau, pour le deux si il peut dépasser la droite (ce qui correspond aux conditions de victoire) et enfinsi la case suivante en fonction de la direction est vide et que le mouvement peut être effectué.

## possible_move
La fonction possible_move vérifie que les coordonées sont dans les limites du plateau, que la direction m est bien située entre 1 et 4 (les quatre points cardinaux) et que la case contient un pion que le joueur peut déplacer. Ensuite les mouvements spécifiques, si m correspond à une direction interdite, on invalide la requête.
Si tout est true, alors on s'occupe de calculer les nouvelles coordonées que l'on stock dans les valeurs new_i new_j en y ajoutant la valeur de direction m que le joueur a choisie.
Et on ajoute à nouveau les conditions de victoire, avant de finalement réaliser le déplacement sur le board.