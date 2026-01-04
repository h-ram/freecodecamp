#! /bin/bash

if [[ $1 == "test" ]]
then
  PSQL="psql --username=postgres --dbname=worldcuptest -t --no-align -c"
else
  PSQL="psql --username=freecodecamp --dbname=worldcup -t --no-align -c"
fi

# Do not change code above this line. Use the PSQL variable above to query your database.

TRUNCATE_RESULT=$($PSQL "TRUNCATE TABLE teams, games")
if [[ ! -z $TRUNCATE_RESULT ]]; then echo "Truncated tables: teams, games"; fi

RESET_TEAMS_SEQ=$($PSQL "ALTER SEQUENCE teams_team_id_seq RESTART WITH 1;")
RESET_GAMES_SEQ=$($PSQL "ALTER SEQUENCE games_game_id_seq RESTART WITH 1;")

# Inserting teams
i=0
while IFS="," read -r YEAR ROUND WINNER OPPONENT WINNER_GOALS OPPONENT_GOALS
do
  # ignore column names
  if [[ $WINNER == "winner" || $OPPONENT == "opponent" ]]; then continue; fi

  # check if winner already inserted
  FIND_TEAM=$($PSQL "SELECT * FROM teams WHERE name='$WINNER'")
  if [[ -z $FIND_TEAM ]]
  then
    INSERT_RESULT=$($PSQL "INSERT INTO teams(name) VALUES('$WINNER');")
    ((i++))
  fi
  
  # check if opponent already inserted
  FIND_TEAM=$($PSQL "SELECT * FROM teams WHERE name='$OPPONENT'")
  if [[ -z $FIND_TEAM ]]
  then
    INSERT_RESULT=$($PSQL "INSERT INTO teams(name) VALUES('$OPPONENT');")
    ((i += 1))
  fi
done < "games.csv"

if [[ ! i -eq 0 ]]
then 
  echo -e "\n$($PSQL "SELECT * FROM teams LIMIT 5;")"
  echo "Inserted ($i) teams."
else
  echo "No teams inserted. "
fi


# Inserting games
i=0
while IFS="," read -r YEAR ROUND WINNER OPPONENT WINNER_GOALS OPPONENT_GOALS
do
  # ignore column names
  if [[ $WINNER == "winner" || $OPPONENT == "opponent" ]]; then continue; fi

  # get winner_id and opponent_id
  WINNER_ID=$($PSQL "SELECT team_id FROM teams WHERE name='$WINNER';")
  OPPONENT_ID=$($PSQL "SELECT team_id FROM teams WHERE name='$OPPONENT';")

  # insert game
  INSERT_RESULT=$($PSQL "INSERT INTO games(year, round, winner_id, opponent_id, winner_goals, opponent_goals) VALUES($YEAR, '$ROUND', $WINNER_ID, $OPPONENT_ID, $WINNER_GOALS, $OPPONENT_GOALS);")
  ((i++))
  
done < "games.csv"

if [[ ! i -eq 0 ]]
then 
  echo -e "\n$($PSQL "SELECT * FROM games LIMIT 5;")"
  echo "Inserted ($i) games."
else
  echo "No games inserted. "
fi