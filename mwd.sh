declare -a EXE=(".cc" ".c" ".cpp" ".cxx" "cu")
REVERSE=0

PATH_TO_PYTHON_SCRIPT="/home/alex/Documents/Play/MessWithDevs"

# Determine input file and direction
for input in "$@"
do
  if [ $input == "-r" ]
  then
    REVERSE=1
  else
    for exe in "${EXE[@]}"
    do
      if [ ${input: -2} == $exe ] || [ ${input: -3} == $exe ] || [ ${input: -4} == $exe ]
      then
        INPUT=$input
      fi
    done
  fi

done

# Rename script
cp $INPUT source.txt
if [ $REVERSE -eq 1 ]
then
  python2 $PATH_TO_PYTHON_SCRIPT/messWithDevs.py -r
else
  python2 $PATH_TO_PYTHON_SCRIPT/messWithDevs.py -f
fi

mv target.txt $INPUT
rm source.txt
