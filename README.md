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
Ici la fonction new_board crée directement les jetons des différents joueurs sur les extrémités des listes, horizontale avec j == 0 and i < n-1 et verticale avec i == n-1 and j > 0 afin que le display_board soit convenablement executé.

## display_board
La fonction display_board est la même que celle du premier jeu Snort, puisqu'elles ont le même fonctionnement d'affichage en dehors du fait qu'on ajoute le board via le new_board.

## possible_pawn
La fonction possible_pawn permet de vérifier si le pion n'est pas bloqué aux yeux des règles du jeu et peut être utilisé par la sutie dans la fonction de déplacement, on vérifie dans un premier temps si les coordonées sont dans les limites du plateau. 
Dans un second temps, on vérifie si la case choisie contient bien un pion valide pour le player. 
Dans le troisième temps on vérifie selon les règles imposées au player, pour le player 1 il ne peut pas se déplacer vers le bas et pour le player 2 vers la gauche. Et dans le dernier point on vérifie si le mouvement est considéré comme valide aux yeux des règles, pour le player 1, si il peut dépasser le haut du plateau, pour le deux si il peut dépasser la droite (ce qui correspond aux conditions de victoire) et enfinsi la case suivante en fonction de la direction est vide et que le mouvement peut être effectué.

## possible_move
La fonction possible_move permet de vérifier que les coordonées choisies par le joueur pour le pion sont dans les limites du plateau, que la direction m est bien située entre 1 et 4 (les quatre points cardinaux) et que la case contient un pion que le joueur peut déplacer. Ensuite les mouvements spécifiques, si m correspond à une direction interdite, on invalide la requête.
Si tout est true, alors on s'occupe de calculer les nouvelles coordonées que l'on stocke dans les valeurs new_i new_j en y ajoutant la valeur de direction m que le joueur a choisie.
Et on ajoute les conditions de victoire, avant de finalement réaliser le déplacement sur le board dans la fonction move.

## dodgem
La fonction dodgem est réalisée dans une forme while not afin de poursuivre la séquence du code tant qu'aucun des deux joueurs n'est victorieux. A chaque tour, on fait appel aux deux sous-fonctions de selection du pion et de la direction, qui vérifie quand à elle à chaque fois si le pion et le mouvement sont réalisables via les sous fonctions possible_move et possible_pawn. On réalise ensuite le déplacement et on affiche finalement de nouveau le board avec le mouvement effectué, tant que personne n'a gagné on change de joueur et on continue la partie.