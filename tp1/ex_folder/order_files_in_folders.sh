dimensions=$(ls | grep ex | cut -b 3 | uniq)

for num in $dimensions
do
    mkdir testset_size$num
    matrices=$(ls | sort -n | grep ex$num)
    for ex in $matrices
    do
        mv $ex ./testset_size$num 
    done
done
