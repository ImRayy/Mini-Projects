#!/bin/bash
#color
green="\e[0;92m"

git add .

echo Your commit message?
read commitMessage

git commit -m "$commitMessage"

git pull origin master

git push origin master

echo -e "${green}${bold} Successfull!${reset}"
