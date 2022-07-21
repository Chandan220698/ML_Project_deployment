# ML_Project_deployment
## Start Machine Learning Project

### Software and Accout Requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code](https://code.visualstudio.com/download)
4. [GIT CLI](https://git-scm.com/downloads)

### Steps
1. `git status`
2. ` git add ` 
3. ` git commit -m "message" `
4. ` git push origin main `

### Virtual environment and requirements.txt
1. Creating conda virtual env
` conda create -p <env_name> python==3.7 -y  (-p to create venv in project folder itself)`
2. Activate venv
` conda activate <env_name>/ `
OR
` conda activate <env_name> `
3. Creating requirement.txt file
` pip freeze > requirements.txt `
4. To install requirements.txt
` pip install -r requirements.txt `