#!/bin/bash

PSQL="psql -X --username=freecodecamp --dbname=salon --tuples-only -c"


SERVICES=$($PSQL "SELECT * FROM services")

while true; do
  echo -e "\nAvailable services:"
  echo "$SERVICES" | while read SERVICE_ID BAR SERVICE_NAME
  do
    echo "$SERVICE_ID) $SERVICE_NAME"
  done
  echo -e "\nChoose a service:"
  read SERVICE_ID_SELECTED

  FIND_CHOICE=$($PSQL "SELECT * FROM services WHERE service_id='$SERVICE_ID_SELECTED';")
  if [[ -z $FIND_CHOICE ]]
  then
    echo -e "\nInvalid choice"
  else
    break
  fi  
done

echo -e "\nEnter your phone-N:"
read CUSTOMER_PHONE

# phone number doesnt exist
FIND_PHONE=$($PSQL "SELECT * FROM customers WHERE phone='$CUSTOMER_PHONE';")
if [[ -z $FIND_PHONE ]]
then 
  echo -e "\nEnter your name:"
  read CUSTOMER_NAME

  INSERT_RESULT=$($PSQL "INSERT INTO customers(phone, name) VALUES('$CUSTOMER_PHONE', '$CUSTOMER_NAME');")
  echo "New customer registered!"
else
  CUSTOMER_NAME=$($PSQL "SELECT name FROM customers WHERE phone='$CUSTOMER_PHONE';")
  echo "Customer already exists:$CUSTOMER_NAME"
fi

echo -e "\nAppointment time:"
read SERVICE_TIME

CUSTOMER_ID=$($PSQL "SELECT customer_id FROM customers WHERE phone='$CUSTOMER_PHONE'")
APPOINTMENT_RESULT=$($PSQL "INSERT INTO appointments(customer_id,service_id,time) VALUES('$CUSTOMER_ID','$SERVICE_ID_SELECTED','$SERVICE_TIME');")

SELECTED_SERVICE_NAME=$($PSQL "SELECT name FROM services WHERE service_id='$SERVICE_ID_SELECTED';")
echo -e "\nI have put you down for a$SELECTED_SERVICE_NAME at $SERVICE_TIME, $CUSTOMER_NAME."
