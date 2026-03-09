#!/bin/bash

PSQL="psql --username=freecodecamp --dbname=number_guess -t --no-align -c"

echo -e "\n --- Number Guessing Game ---\n"

echo -e "Enter your username:"
read USERNAME

# check if already exists
IFS="|" read USER_ID GAMES_PLAYED BEST_GAME <<< $($PSQL "SELECT user_id, games_played, best_game FROM users WHERE username='$USERNAME';")
if [[ -z $USER_ID ]]
then
  echo "Welcome, $USERNAME! It looks like this is your first time here."
else
  echo "Welcome back, $USERNAME! You have played $GAMES_PLAYED games, and your best game took $BEST_GAME guesses."
fi

NUMBER=$(( $RANDOM % 1000 + 1 ))
echo $NUMBER

echo -e "\nGuess the secret number between 1 and 1000:"
read GUESS

TRIES=1
while [[ $GUESS -ne $NUMBER ]]
do
  if [[ ! $GUESS =~ ^[0-9]+$ ]]
  then
    echo "That is not an integer, guess again:"

  elif [[ $GUESS -lt $NUMBER ]]
  then
    echo "It's higher than that, guess again:"

  else
    echo "It's lower than that, guess again:"
  fi
  read GUESS
  ((TRIES++))
done

echo "You guessed it in $TRIES tries. The secret number was $NUMBER. Nice job!"

if [[ -z $USER_ID ]]
then
  INSERT_RESULT=$($PSQL "INSERT INTO users(username, games_played, best_game) VALUES ('$USERNAME', 1, $TRIES);")
else
  UPDATE_RESULT=$($PSQL "UPDATE users SET games_played=$GAMES_PLAYED+1, best_game=GREATEST($BEST_GAME, $TRIES) WHERE username='$USERNAME';")
fi

# GOODBYE :) <3 <3 <3