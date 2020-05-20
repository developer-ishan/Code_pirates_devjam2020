# MNNIT UTILITIES 
```
MNNIT utilities is used to mark attendence at hostel gates and giving some features like personlised  class and mess time table etc.
```


## How to use

This project is available in both android application and web-site.
#### ``` For gaurds app is availabe so that they can scan qr code at entry of student```
#### ``` For students they have acccess to only the web-site only ```
#### ``` Every Stuent will have to create their own profile and also attching their profile image```

## Features

```To reduce the long wait at the queues, our app will generate a QR code(unique for each student) which the gate guards will scan through their mobile application, same for checking into the hostel. ```
``` There is a lot of mess food wastage, our app will display the current menu, and the student can poll, if they want to eat it or not.```
```This can also be used to register the complaints here, which would be delivered to the caretaker from time to time.```
```It gives features host online communities(such as web, ML and even UPSC aspirants) , where the seniors with a mentor profile can post information stuff to help their juniors with stuff.```
```We have made accessible the timetable of the MNNIT dispensary and the nearby hospitals, so that the accessibility of these facilities.```


## Tech Stack
* HTML
* CSS
* JAVA SCRIPT
* PYTHON
* ANDROID STUDIO 

## Libraries
* Asgiref
* Colorama
* Django
* Pillow
* Pytz
* Qrcode
* Six
* Sqlparse


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


## If the url breaks for any view then populate the database and then run the server.

## Team Details
#Team Name: Code_Pirates
```
Member 1: Mohit Pandey 20194204
Member 2: Lovedeep Singh Kamal 20198042
Member 3: Ishan Gupta 20194175
Member 4: Arun Kumar 20194109

```



