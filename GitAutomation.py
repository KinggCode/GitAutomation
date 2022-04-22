import random 
import datetime
import subprocess as cmd
import json

class GitAutomation:
    def __init__(self):
        self.automationId = 'GitAutomation-'+ str(random.randint(100,200))
        self.date = datetime.datetime.now()
        self.commit_message = ''
        self.branch_name = ''
        self.result = ''
        self.log = dict()

    def clone_git_repository(self):
        repository_name = input('Enter your desired Git repository url (http): ')
        clone_repo = f'git clone -m "{repository_name}"'
        cmd.run(clone_repo)
        print("Successfully Cloned Repository")
        print()

    def git_status(self):
        git_status = 'git status'
        cmd.run(git_status)

    def create_git_repository(self):
        dir_to_repo = 'git init'
        cmd.run(dir_to_repo)
        print("Successfully Changed Local Directory into a Repository")
        print()

        
    def link_remote_repository(self):
        remote_origin = input('Enter your desired remote url (http): ')
        add_origin = f'git remote add origin "{remote_origin}"'
        cmd.run(add_origin)
        print("Successfully linked remote repository to Git")
        print()

    def git_add(self):
        git_add = 'git add .'
        cmd.run(git_add)
        print("Successfully Added New changes to Local Repository")
        print()

    def git_status(self):
        git_status = 'git status'
        cmd.run(git_status)

    def git_push_process(self):
        try:
            self.git_add()
            
            self.commit_message = input('Enter commit message: ')
            self.commit_message = f'git commit -m "{self.commit_message}"'
            cmd.run(self.commit_message, check=True, shell=True)

            self.branch_name = input('Enter branch name: ')
            push = f'git push origin {self.branch_name}'

            print(f"Pushing to {self.branch_name} branch ...")

            cmd.run(push, check=True, shell=True)

            print(f"Successfully Pushed to {self.branch_name} branch")
            self.result = True
            return True
        except:
            print("Error git automation")
            self.result = False
            return False

    def git_pull_process(self):
        branch_name = input('Enter branch name: ')
        pull = f'git pull origin {branch_name}'
        cmd.run(pull)
        print(f"Successfully pulled from {self.branch_name} main")


    def git_new_branch(self):
        branch_name = input('Enter branch name you would like to create: ')
        create_branch = f'git checkout -b  {branch_name}'
        cmd.run(create_branch)
        print(f"Successfully created {self.branch_name} branch")

    def change_branch(self):
        branch_name = input('Enter branch name you would like to move to: ')
        move_to_branch = f'git checkout  {branch_name}'
        cmd.run(move_to_branch)
        print(f"Successfully moved to {self.branch_name} branch")



    def write_git_push_log(self):

    
        self.log["commit_message"] = str(self.commit_message)
        self.log["branch_name"] = str(self.branch_name)
        self.log["output"] = str(self.result)
        self.log["timestamp"] =  str(self.date)
        log = json.dump(self.log)

        file = 'git_push_log.txt'
        file = open(file,'a')
        file.write(log)
        file.close()
        print('Message Stored')
        return

    def welcome_screen(self):
        print('Welcome to Git Automation')
        return

if __name__ == "__main__":
    choice = 1 
    gitBot = GitAutomation()

    while choice != 0:
        print()
        print('0. Exiting Git Program')
        print('1. Git Automation Screen')
        print('2. Add New changes to Local Repository')
        print('3. Git push to specific branch')
        print('4. Git pull from specific branch')
        print('5. Get Repository Status')
        print('6. Create a new branch within the repository')
        print('7. Move to specific branch')
        print('8.Change Local Directory into Repository')
        print('9. Link Current Repository to Remote Repository')

        choice = eval(input('Enter Git Program number to run: '))
        if choice == 1:
            print()
            gitBot.welcome_screen()
        elif choice == 2:
            print()
            gitBot.git_add()
        elif choice == 3:
            print()
            gitBot.git_push_process()
            gitBot.write_git_push_log()
        elif choice == 4:
            print()
            gitBot.git_pull_process()
        elif choice == 5:
            print()
            gitBot.git_status()
        elif choice == 6:
            print()
            gitBot.git_new_branch()
        elif choice == 7:
            print()
            gitBot.change_branch()
        elif choice == 8:
            print()
            gitBot.create_git_repository()
        elif choice == 9:
            print()
            gitBot.link_remote_repository()
        else:
            print('Invalid program choice')
        
