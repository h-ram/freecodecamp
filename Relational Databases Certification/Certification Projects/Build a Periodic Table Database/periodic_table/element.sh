#!/bin/bash

PSQL="psql --username=freecodecamp --dbname=periodic_table --no-align --tuples-only -c"


if [[ -z $1 ]]
then
  echo "Please provide an element as an argument."
  exit
fi

# given atomic number
if [[ "$1" =~ ^[0-9] ]]
then 
  IFS="|" read ATOMIC_NUMBER ELEMENT_SYMBOL ELEMENT_NAME ELEMENT_TYPE ATOMIC_MASS MELTING_POINT BOILING_POINT <<< $($PSQL "SELECT atomic_number, symbol, name, type, atomic_mass, melting_point_celsius, boiling_point_celsius FROM elements JOIN properties USING(atomic_number) JOIN types USING(type_id) WHERE atomic_number=$1")

# given element symbol
elif [[ ${#1} -le 2 ]]
then

  IFS="|" read ATOMIC_NUMBER ELEMENT_SYMBOL ELEMENT_NAME ELEMENT_TYPE ATOMIC_MASS MELTING_POINT BOILING_POINT <<< $($PSQL "SELECT atomic_number, symbol, name, type, atomic_mass, melting_point_celsius, boiling_point_celsius FROM elements JOIN properties USING(atomic_number) JOIN types USING(type_id) WHERE symbol='$1'")
# given element name
else [[ ${#1} -gt 2 ]]
  IFS="|" read ATOMIC_NUMBER ELEMENT_SYMBOL ELEMENT_NAME ELEMENT_TYPE ATOMIC_MASS MELTING_POINT BOILING_POINT <<< $($PSQL "SELECT atomic_number, symbol, name, type, atomic_mass, melting_point_celsius, boiling_point_celsius FROM elements JOIN properties USING(atomic_number) JOIN types USING(type_id) WHERE name='$1'")
fi

if [[ -z $ELEMENT_NAME ]]
then
  echo "I could not find that element in the database."
else
  echo "The element with atomic number $ATOMIC_NUMBER is $ELEMENT_NAME ($ELEMENT_SYMBOL). It's a $ELEMENT_TYPE, with a mass of $ATOMIC_MASS amu. $ELEMENT_NAME has a melting point of $MELTING_POINT celsius and a boiling point of $BOILING_POINT celsius."
fi