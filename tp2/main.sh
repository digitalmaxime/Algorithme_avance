echo 'Debut des algos!'

folder='instances'
testsets=$(ls ./$folder)

echo "glouton; nb_vertices; time" > ./results_glouton.csv
for testset in  $testsets     
do   
    echo 'path :  ./'$folder'/'$testset
    ./tp.sh -a 'glouton' -e ./$folder/$testset -t
done
echo "branch_bound; nb_vertices; time" > ./results_branch_bound.csv
for testset in  $testsets     
do   
    echo 'path :  ./'$folder'/'$testset
    ./tp.sh -a 'branch_bound' -e ./$folder/$testset -t
done

echo 'tout fini :)'