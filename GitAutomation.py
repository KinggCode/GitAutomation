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

    def create_git_repository(self):
        '''
        Everything starts from here. The first step is to initialize a new Git repo locally in your project root. 
        '''
        dir_to_repo = 'git init'
        cmd.run(dir_to_repo)
        print("Successfully Changed Local Directory into a Repository")
        print()

    def clone_git_repository(self):
        repository_name = input('Enter your desired Git repository url (http): ')
        clone_repo = f'git clone -m "{repository_name}"'
        cmd.run(clone_repo)
        print("Successfully Cloned Repository")
        print()

    def git_status(self):
        git_status = 'git status'
        cmd.run(git_status)

        
    def link_remote_repository(self):
        remote_origin = input('Enter your desired remote url (http): ')
        add_origin = f'git remote add origin "{remote_origin}"'
        cmd.run(add_origin)
        print("Successfully linked remote repository to Git")
        print()

    def git_add_all(self):
        git_add = 'git add .'
        cmd.run(git_add)
        print("Successfully Added New changes to Local Repository")
        print()

    def git_status(self):
        '''
        shows the status of the current repository including staged, unstaged, and untracked files.
        '''
        git_status = 'git status'
        cmd.run(git_status)

    
    def git_commit_without_push(self):
        try:
            self.git_add_all()
            
            self.commit_message = input('Enter commit message: ')
            self.commit_message = f'git commit -m "{self.commit_message}"'
            cmd.run(self.commit_message, check=True, shell=True)

            print(f"Successfully Commited Logs")
            self.result = True
            return True
        except:
            print("Error git automation")
            self.result = False
            return False
    
    def git_push_process_only(self):
        try:
        
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


    def git_push_process_with_commit(self):
        try:
            self.git_add_all()
            
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

    def git_config_info(self):
        '''
        returns a list of information about your git configuration including user name and email
        '''
        confg_info = f'git config -l'
        cmd.run(confg_info)
        print(f"Successfully fetched git configuration information")

    def set_git_username(self):
        '''
        returns a list of information about your git configuration including user name and email
        '''
        username = input('Enter git username: ')
        set_username = f'git config --global user.name "{username}"'
        cmd.run(set_username)
        print(f"Successfully set git configuration username")

    def set_git_email(self):
        '''
        returns a list of information about your git configuration including user name and email
        '''
        email = input('Enter git username: ')
        set_username = f'git config --global user.email "{email}"'
        cmd.run(set_username)
        print(f"Successfully set git configuration email")

    def git_add_file(self):
        '''
        Just replace filename_here with the name of the file you want to add to the staging area
        '''
        filename = input('Enter git username: ')
        git_add = f'git add "{filename}"'
        cmd.run(git_add)
        print("Successfully Added New changes to Local Repository")
        print()

    def git_add_wildcard_only(self):
        '''
        With the asterisk in the command below, you can add all files starting with 'fil' in the staging area.
        '''
        wildcard = input('Enter file wildcard type: ')
        git_add_wildcard = f'git add "{wildcard}"*'
        cmd.run(git_add_wildcard)
        print("Successfully Added Wildcard files to Git Repository")
        print()

    def git_history(self):
        '''
            shows the commit history for the current repository        
        '''
        git_add_wildcard = f'git log'
        cmd.run(git_add_wildcard)
        print("Successfully Fetched all git logs")
        print()

    def git_history_extended(self):
        '''
            shows the commit's history including all files and their changes:       
        '''
        git_add_wildcard = f'git log'
        cmd.run(git_add_wildcard)
        print("Successfully Fetched all git logs with more information")
        print()

    def git_delete(self):
        '''
            expects a commit message to explain why the file was deleted.       
        '''
        filename = input('Enter git filename: ')
        delete_file = f'git rm "{filename}"'
        cmd.run(delete_file)
        print("Successfully Deleted File from Git Repository")
        print()



    # def write_git_push_log(self,type="regular"):

    #     if type == "commit":
    #         self.log["commit_message"] = str(self.commit_message)
    #         self.log["branch_name"] = str(self.branch_name)
    #         self.log["output"] = str(self.result)
    #         self.log["timestamp"] =  str(self.date)
    #         log = json.dumps(self.log)

    #     elif type == "regular":
    #         self.log["branch_name"] = str(self.branch_name)
    #         self.log["output"] = str(self.result)
    #         self.log["timestamp"] =  str(self.date)
    #         log = json.dumps(self.log) + ","

    #     file = 'git_push_log.txt'
    #     file = open(file,'a')
    #     file.write(log)
    #     file.close()
    #     print('Message Stored')
    #     return

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
        print('3. Git commit to specific repo stage without push')
        print('4. Git push to specific branch only (without adding and commiting)')
        print('5. Git push to specific branch only (with adding and commiting)')
        print('6. Git pull from specific branch')
        print('7. Get Repository Status')
        print('8. Create a new branch within the repository')
        print('9. Move to specific branch')
        print('10.Change Local Directory into Repository')
        print('11. Link Current Repository to Remote Repository')

        choice = eval(input('Enter Git Program number to run: '))
        if choice == 1:
            print()
            gitBot.welcome_screen()
        elif choice == 2:
            print()
            gitBot.git_add_all()
        elif choice == 3:
            print()
            gitBot.git_commit_without_push()
        elif choice == 4:
            print()
            gitBot.git_push_process_only()
        elif choice == 5:
            print()
            gitBot.git_push_process_with_commit()
        elif choice == 6:
            print()
            gitBot.git_pull_process()
        elif choice == 7:
            print()
            gitBot.git_status()
        elif choice == 8:
            print()
            gitBot.git_new_branch()
        elif choice == 9:
            print()
            gitBot.change_branch()
        elif choice == 10:
            print()
            gitBot.create_git_repository()
        elif choice == 11:
            print()
            gitBot.link_remote_repository()
        else:
            print('Invalid program choice')
        
