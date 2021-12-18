#!/bin/bash
##created by ray
#Colourcoads

green="\e[0;92m"
red="\e[0;91m"
reset="\e[0m"
#Function
gitFunc()
{
    printf "0.Exit\n1. Pull\n2. Push\n3. Sync\n4. Create new repository\n\n"
    while true
    do
        read -p "-> " input
        read -p "Set branch name -> " branch

        if [ $input -eq 1 ];then
            git pull origin $branch
            echo -e "${green}${bold}Successfully synced with local repository${reset}"
            break

        elif [ $input -eq 2 ]; then
            git add -A
            read -p "Commit message -> " commitMsg
            git commit -m "$commitMsg"
            git push origin $branch
            echo -e "${green}${bold}Pushed to remote repository${reset}"
            break

        elif [ $input -eq 3 ];then
            read -p "Commit message -> " commitMsg
            git pull
            git add -A
            git commit -m "$commitMsg"
            git push origin $branch
            echo -e "${green}${bold}Synchronization Successfull!${reset}"
            break

        elif [ $input -eq 4 ];then
            while true
            do
                printf "1. Create locally\n2. Sync with online manager\n\n"
                read -p "-> " input
                if [ $input -eq 1 ];then
                    touch README.md
                    git init
                    git add -A
                    read -p "Commit message -> " commitMsg
                    git commit -m "commitMsg"
                    echo -e "${green}${bold}New local repository has been Successfully created${reset}"
                    break
                elif [ $input -eq 2 ];then

                        touch README.md
                        git init
                        git add -A
                        read -p "Commit message -> " commitMsg
                        git commit -m "$commitMsg"
                        read -p "Enter remote name -> " remoteName
                        read -p "Enter repository url -> " repoUrl
                        git remote add $remoteName $repoUrl
                        git push origin $branch
                        echo -e "${green}${bold}Repository Successfully updated on github${reset}"
                        break
                else
                    echo -e "${red}${bold}Invalid input!${reset}"

                fi
            done
            break
        else
            echo -e "${red}${bold}Invalid input!${reset}"
        fi
    done

}

# This part is for my own convenience, can be changed accordingly
printf "0. exit\n1. Notes\n2. Programing\n3. Manual path\n\n"

while true
do

    read -p '-> ' userInput
    if [ $userInput -eq 1 ]; then
        cd /media/Documents/Notes/
	gitFunc
	exit

    elif [ $userInput -eq 2 ];then
        cd /home/imray/MEGAsync/Programing/
	gitFunc
	exit
    elif [ $userInput -eq 3 ];then
   	read -p "Enter path -> " customPath
	cd $customPath
	gitFunc
	exit
    elif [ $userInput -eq 0 ];then
        exit 1
    else
        echo -e "${red}${bold}Invalid input!${reset}"
    fi
done

#!/bin/bash
##created by ray
#Colourcoads

green="\e[0;92m"
red="\e[0;91m"
reset="\e[0m"
#Function
gitFunc()
{
    printf "0.Exit\n1. Pull\n2. Push\n3. Sync\n4. Create new repository\n\n"
    while true
    do
        read -p "-> " input
        read -p "Set branch name -> " branch

        if [ $input -eq 1 ];then
            git pull origin $branch
            echo -e "${green}${bold}Successfully synced with local repository${reset}"
            break

        elif [ $input -eq 2 ]; then
            git push origin $branch
            echo -e "${green}${bold}Pushed to remote repository${reset}"
            break

        elif [ $input -eq 3 ];then
            read -p "Commit message -> " commitMsg
            git pull
            git add -A
            git commit -m "$commitMsg"
            git push origin $branch
            echo -e "${green}${bold}Synchronization Successfull!${reset}"
            break

        elif [ $input -eq 4 ];then
            while true
            do
                printf "1. Create locally\n2. Sync with online manager\n\n"
                read -p "-> " input
                if [ $input -eq 1 ];then
                    touch README.md
                    git init
                    git add -A
                    read -p "Commit message -> " commitMsg
                    git commit -m "commitMsg"
                    echo -e "${green}${bold}New local repository has been Successfully created${reset}"
                    break
                elif [ $input -eq 2 ];then

                        touch README.md
                        git init
                        git add -A
                        read -p "Commit message -> " commitMsg
                        git commit -m "$commitMsg"
                        read -p "Enter remote name -> " remoteName
                        read -p "Enter repository url -> " repoUrl
                        git remote add $remoteName $repoUrl
                        git push origin $branch
                        echo -e "${green}${bold}Repository Successfully updated on github${reset}"
                        break
                else
                    echo -e "${red}${bold}Invalid input!${reset}"

                fi
            done
            break
        else
            echo -e "${red}${bold}Invalid input!${reset}"
        fi
    done

}

# This part is for my own convenience, can be changed accordingly
printf "0. exit\n1. Notes\n2. Programing\n3. Manual path\n\n"

while true
do

    read -p '-> ' userInput
    if [ $userInput -eq 1 ]; then
        cd /media/Documents/Notes/
	gitFunc
	exit

    elif [ $userInput -eq 2 ];then
        cd /home/imray/MEGAsync/Programing/
	gitFunc
	exit
    elif [ $userInput -eq 3 ];then
   	read -p "Enter path -> " customPath
	cd $customPath
	gitFunc
	exit
    elif [ $userInput -eq 0 ];then
        exit 1
    else
        echo -e "${red}${bold}Invalid input!${reset}"
    fi
done

