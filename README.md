# ML_Project_deployment
## Start Machine Learning Project

### Software and Accout Requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code](https://code.visualstudio.com/download)
4. [GIT CLI](https://git-scm.com/downloads)

### Steps
1. ` git add ` 
2. ` git commit -m "message" `
3. ` git push origin main `

### 
Creating conda virtual env
```
conda create -p <env_name> python==3.7 -y  (-p to create venv in project folder itself)
```
Activate venv
```
conda activate <env_name>/
```
OR
```
conda activate <env_name>
```
Creating requirement.txt file
```
pip freeze > requirements.txt
```
To install requirements.txt
```
pip install -r requirements.txt
```