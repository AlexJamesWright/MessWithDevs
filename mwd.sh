#!/bin/bash

declare -a EXE=(".cc" ".c" ".cpp" ".cxx" ".cu" ".c++" ".js" ".java" ".ii" \
".ixx" ".ipp" ".i++" ".inl" ".idl" ".ddl" ".odl" ".h" ".hh" ".hxx" ".hpp" ".h++" \
".cs" ".d" ".php" ".php4" ".php5" ".phtml" ".inc" ".m" ".md" ".mm" ".html" \
".dox" ".py" ".pyw" ".f90" ".f95" ".f03" ".f08" ".f" ".for" ".tcl" ".vhd" ".vhdl" \
".ucf" ".qsf")

REVERSE=0
INPUTFILE=0

PATH_TO_PYTHON_SCRIPT=$(pwd)

# Determine input file and direction
for input in "$@"
do
  if [ $input == "-r" ]
  then
    REVERSE=1
  else
    for exe in "${EXE[@]}"
    do
      if [ ${input: -2} == $exe ] || [ ${input: -3} == $exe ] || [ ${input: -4} == $exe || [ ${input: -5} == $exe || [ ${input: -6} == $exe ]
      then
        INPUT=$input
        INPUTFILE=1
      fi
    done
  fi
done

if [ $INPUTFILE -eq 0 ]
then
  echo 'No input file matches the valid extensions.'
else
  # Rename script
  cp $INPUT source.txt
  if [ $REVERSE -eq 1 ]
  then
    python $PATH_TO_PYTHON_SCRIPT/messWithDevs.py -r
  else
    python $PATH_TO_PYTHON_SCRIPT/messWithDevs.py -f
  fi

  mv target.txt $INPUT
  rm source.txt
fi
