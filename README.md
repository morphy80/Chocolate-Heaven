## Data - Centric Development Project, MS3-Code Institute
# Chocolate Heaven
- description
![site logo]()
[Visit deployed site]()

## Table of Contents

- [**Demo**](#Demo)
- [**UI/UX**](#UI/UX)
  - [Project goals](#Project-goals)
  - [User Stories](#User-Stories)
  - [Developer goals](#Developer-goals)
  - [Design](#Design)
    - [Research](#Research)
    - [Wireframes](#Wireframes)
    - [Color Palette](#Color-Palette)
  - [Defensive design](#Defensive-design)
- [**Features**](#Features)
    - [Notes](#Notes)
    - [Existing features](#Existing-features)
    - [Future features](#Future-features)
- [**Information Architecture**](#Information-Architecture)
- [**Technologies used**](#Technologies-used)
- [**Testing**](#Testing)
    - [Validators and linters](#Validators-and-linters)
    - [Manual testing](#Testing)
    - [Errors](#Errors)
- [**Deployment**](#Deployment)
- [**Credits**](#Deployment)
    - [Code](#Code)
    - [Images](#Images)
- [**Acknowledgements**](#Acknowledgements)
- [**Disclaimer**](#Disclaimer)

## Demo

![demo2]

## UI/UX
### Project goals
Chocolate Heaven is milestone project for Code Institute Data Centric Development module. The goal of this project is to create, store, edit and delete recipes (CRUD). 

### User Stories

As a User I would like to:
- [x] Be able to register to have my own profile.
- [x] Be able to browse and navigate information easily.
- [x] Browse recipes by category
- [x] Submit my own recipes
- [x] Sign up or Sign in with user friendly form
- [x] Edit and delete my own recipes, without others tampering with my submitted recipes.
- [x] Get feedback for submitting/editing/logging in/logging out
- [x] Access a list of all recipes
- [x] Get error messages in case user has done something wrong or there is an issue with database.

As an admin I would like to do all of the above plus:
- [x] Be able to access, edit and delete ALL recipes from admin profile

### Developer goals

 * Provide a simple, easy to use online cookbook where user can browse, post, edit and delete recipes, filter them by categories, search by text, subscribe and have profile.
 * By practice learn Jinja templating, Python, non-relational database MongoDb 
 * Improve Bootstrap and JavaScript knowledge.
 * Learn to use Heroku Pages

### Design

![Demo Picture]()

#### Research

#### Wireframes

#### Color Palette

### Defensive design

## Features
### Notes

### Existing features

- [x] Favicon

### Future features

- [ ] Pagination

### Information Architecture
MongoDB Atlas is used for storing data for this web site.

Current schema: 

![Schema]()

## Technologies used

Below are a list of the programming languages, technologies, frameworks and resources used for this website.

* HTML5
* CSS3
* jQuery
* Python 3.8
    * Flask
    * Jinja
    * Werkzeug security
* MongoDB and MongoDB Compass
* Git & GitHub.com
* Heroku.com pages
* Markdown
* FontAwesome.com
* Google Fonts
* Google Chrome Developer tools
* Cloudinary.com to store all images
* Favicon.io convert favicon

## Testing
Devices and platforms used for testing:

*

### Validators and linters

* [W3C HTML Validator](https://validator.w3.org/#validate_by_input) Passed tests without issues
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
* [JSHint](https://jshint.com) 
* [PEP8](http://pep8online.com) and AUTOPEP8.

### Manual testing

### Errors

## Deployment

This project can be ran locally by following the following steps: 
(Steps may differ in GitPod/Windows/Linux. I used Visual Studio Code on MacOS)

Create a free account on Cloudinary.com download my media or create your own.

Visit this [repository link](https://github.com/morphy80/chocolate-heaven-ms3.git) and click on the Clone or Download button to copy the link provided.

![clone](https://res.cloudinary.com/ddrsbzhmf/image/upload/v1612011028/chocolate-heaven/Screenshot_2021-01-30_123427_di8rah.png)

In your IDE, open a Terminal window and change to the directory where you want to clone this [repository](https://github.com/morphy80/chocolate-heaven-ms3.git) and type:

for macOS:
```
$ cd /Users/user/my_project
```
for Windows:
```
$ cd C:/Users/user/my_project
```
and type:
```
$ git init
```

```
$ git clone https://github.com/morphy80/chocolate-heaven-ms3.git
```
After pressing Enter the project will be created and cloned locally.

(Alternatively you can download the zipped file, decompress it and use your IDE of choice to access it.)

Create a free account on MongoDb and reproduce the 4 collections as described [here](#Information-Architecture).

Make sure to upgrade PIP. 
```
$ pip install -U pip 
```

Install all dependencies
```
$ pip3 install -r requirements.txt
```
Activate virtual environment 
```
$ source env/bin/activate
```
Create .env file with following data
```
MONGO_URI=mongodb+srv://...
SECRET_KEY_FLASK=superdupersecretkey
```
Add your .env file to .gitignore

In the last line of app.py file change from `debug=False` to `debug=True`

You will then be able to run the app locally by typing `python app.py` or  `flask run`. 

### Heroku

Heroku was chosen as the deployment platform for this project. The steps to deploy the local app to Heroku were as follow:

In Heroku, create an app. The app must have a unique name.

Link that app to the GitHub repository by going to the "Deploy" tab in the main app menu.

In the Settings tab, add the corresponding Config Variables as present in local development:

```
MONGO_URI mongodb+srv://...
IP 0.0.0.0
PORT 5000
SECRET_KEY superdupersecretkey
```

Created "Procfile" by typing:
```
$ echo web: python app.py > Procfile
```
Push repo to Heroku
```
$ git push heroku master
```
After these steps the app is live and running remotely in Heroku's servers.

### Heroku

## Credits
### Code

### Images

### Content 

## Acknowledgements

## Disclaimer

This project is for educational purposes only.

Alexander Apostoiu

2021

[Back to top ↑](#Chocolate-Heaven)