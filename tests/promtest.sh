#!/bin/sh
# fullname="USER INPUT"
echo
echo "=================================================================================================================================================="
echo 
echo "   You can pass for rules path as first argument or put your alerts to role file directory (../monitoring/files/alert_rules/)"
echo 
echo "=================================================================================================================================================="
echo


read -p "Do you want to continue with default path? (y/n or q to exit): " answer
# fullname="USER INPUT"
# user="USER INPUT"

default_rules_path=../monitoring/files/alert_rules
default_rules=$(ls $default_rules_path/)
#rule_path=$1

#while [ $answer != "y" || $answer != "n" $answer != "q"]

if [ $answer == "y" ]; then
   echo
   echo "******************* STARTING RULES CHECK *******************"
   echo
   echo "   Default rules path" $default_rules_path " will be used"
   echo
   echo "=================================================================================================================================================="
   echo
   for rule in $default_rules; do
     ./promtool/promtool check rules ../monitoring/files/alert_rules/$rule
   done

elif [ $answer == "n" ]; then
   echo

   read -p "Rules path: " rule_path

   echo
   echo "=================================================================================================================================================="
   echo
   
   if [ -z $rule_path ]; then
      echo "   Looks like you haven't enter the rule path or enter an empty path! Please try again!"
      echo
   else
      echo
      echo "******************* STARTING RULES CHECK *******************"
      echo   
      echo "   Your rules path" $rule_path " will be used"
      echo
      echo "=================================================================================================================================================="
      echo
      
      rules=$(ls $rule_path/)   
      for rule in $rules; do
        ./promtool/promtool check rules $rule_path/$rule
      done   
   fi

 else
     echo
     echo "   You need to enter \"y\" or \"n\" but you enter" \"$answer\""!" 
     echo "   Please try again!"
     echo
fi        