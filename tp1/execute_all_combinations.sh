folders=$(ls ./ex_folder | grep testset_)
nb_of_folders=$(wc -w <<< $folders)

if [[ $folder == '' ]]; then
    echo "consider running 'order_files_in_folders.sh' in the ex/folder.."
fi

echo "nb of FOLDERS " $nb_of_folders

for testset in $folders 
do
    for algo_type in 'conv' 'strassen' 'strassenSeuil'
    do   
        matrices=($(ls ./ex_folder/$testset)) # parenthesis make it into a list
        echo " " $matrices
        nb_of_matrices=${#matrices[@]}
        echo "nb of matrices: " $nb_of_matrices
        for ((i = 0; i < nb_of_matrices - 1; i++)) do
            for ((j = i; j < nb_of_matrices - 1; j++)) do
                echo ./ex_folder/$testset/${matrices[$i]}  times ./ex_folder/$testset/${matrices[$j+1]} 

                ./tp.sh -e1 ./ex_folder/$testset/${matrices[$i]} -e2 ./ex_folder/$testset/${matrices[$j+1]} -a $algo_type -t

            done
        done
    done
done