echo 'Debut des algos!'

folder='instances2'
testsets=$(ls ./$folder)

echo "glouton; nb_vertices; time; nbColorUsed" > ./results_glouton.csv
for testset in  $testsets     
do   
    echo 'path :  ./'$folder'/'$testset
    ./tp.sh -a 'glouton' -e ./$folder/$testset -t
done

echo "tabou; nb_vertices; time; nbColorUsed" > ./results_tabou.csv
for testset in  $testsets     
do   
    echo 'path :  ./'$folder'/'$testset
    ./tp.sh -a 'tabou' -e ./$folder/$testset -t
done

echo "branch_bound; nb_vertices; time; nbColorUsed" > ./results_branch_bound.csv
for testset in  $testsets     
do   
    echo 'path :  ./'$folder'/'$testset
    ./tp.sh -a 'branch_bound' -e ./$folder/$testset -t
done

echo 'tout fini :)'