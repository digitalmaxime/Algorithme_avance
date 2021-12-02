# read -rp "What's your name? " "name"
# SECONDS=0
# echo "Hello, $name"
# if (( $SECONDS > 3600 )) ; then
#     let "hours=SECONDS/3600"
#     let "minutes=(SECONDS%3600)/60"
#     let "seconds=(SECONDS%3600)%60"
#     echo "Completed in $hours hour(s), $minutes minute(s) and $seconds second(s)" 
# elif (( $SECONDS > 60 )) ; then
#     let "minutes=(SECONDS%3600)/60"
#     let "seconds=(SECONDS%3600)%60"
#     echo "Completed in $minutes minute(s) and $seconds second(s)"
# else
#     echo "Completed in $SECONDS seconds"
# fi

echo 'Debut des algos avec counter = 100 000!'

echo "test 66_99"
gtimeout 180 ./tp.sh -e './instances/66_99.0' ||  echo "ok, times up!\n"

echo "test 66_534"
gtimeout 180 ./tp.sh -e './instances/66_534.0' ||  echo "ok, times up!\n"

echo "test 66_970"
gtimeout 180 ./tp.sh -e './instances/66_970.0' ||  echo "ok, times up!\n"

echo "test 118_178"
gtimeout 180 ./tp.sh -e './instances/118_178.0' ||  echo "ok, times up!\n"

echo "test 118_1570"
gtimeout 180 ./tp.sh -e './instances/118_1570.0' ||  echo "ok, times up!\n"

echo "test 118_2962"
gtimeout 180 ./tp.sh -e './instances/118_2962.0' ||  echo "ok, times up!\n"

echo "test 558_837"
gtimeout 180 ./tp.sh -e './instances/558_837.0' ||  echo "ok, times up!\n"

echo "test 558_31973"
gtimeout 180 ./tp.sh -e './instances/558_31973.0' ||  echo "ok, times up!\n"

echo "test 558_63109"
gtimeout 180 ./tp.sh -e './instances/558_63109.0' ||  echo "ok, times up!\n"

echo "tout fini :)"