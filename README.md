# devjam
this is my project for devjam 2020



## setting up the project on your pc
### 1.First create a virtual environment using following command

```bash
python -m venv whatever_name_you_want
```
### 2.Then start the virtual environment on your system
for window PC use following in cmd


```bash
your_environment_name\Scripts\activate
```
### now clone this repo using following command

```bash
git clone https://github.com/dev-lovedeep/devjam.git .
```
### 3.now install requirement for this project

```bash
 pip install -r requirements.txt
```
### 4.finally run this command 

```bash
 python manage.py migrate
```
if this give some error use 
```bash
 python manage.py makemigrations
 python manage.py migrate
```

## activate the server to view it on browser
```bash
 python manage.py runserver
```
and in browser go to following [URL](http://localhost:8000/) http://localhost:8000/ to see the project

