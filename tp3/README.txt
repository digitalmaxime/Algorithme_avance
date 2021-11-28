Algorithme avancé
cours d'algorithme avancé de poly
matricules 1946878 1897918

METHOD 1 : 
1)    
    ./tp.sh -e PATH_INSTANCE -p > sortie.out
    
    # will print each solution found in sortie.out 

2) 
    cat sortie.out | ./check_sol.py -e PATH_INSTANCE

    # will check each solution printed in sortie.out 


METHOD 2 : 
1) 
    (timeout 180s ./tp.sh -e PATH_INSTANCE -p; exit 0) | ./check_sol.py -e PATH_INSTANCE [-s FICHIER_SORTIE]

    # will pipe each solution found in 180s through check_sol to verify the solution
