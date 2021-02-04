## Data - Centric Development Project, MS3-Code Institute
# Chocolate Heaven
- description
![site logo](https://res.cloudinary.com/ddrsbzhmf/image/upload/v1612466158/chocolate-heaven/logo_krumdn.png)
[Visit deployed site](https://chocolate-heaven.herokuapp.com/)

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
Chocolate Heaven is milestone project for Code Institute Data Centric Development module. The goal of this project is to create, store, edit and delete recipes (CRUD operations). 

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


Fonts used: [Bubblegum Sans](https://fonts.google.com/specimen/Bubblegum+Sans?query=bubb&preview.text_type=custom), [Emilys Candy](https://fonts.google.com/specimen/Emilys+Candy?query=Emilys+Candy&preview.text_type=custom), [Rye](https://fonts.google.com/specimen/Rye?query=Rye&preview.text_type=custom),
 [Special Elite](https://fonts.google.com/specimen/Special+Elite?query=Special+Elite&preview.text_type=custom) imported from Google Fonts.
#### Research

#### Wireframes

I created my wireframes during the Scope Plane of this project.
I made wireframes for each page of the site from three different type of devices:

1. [Desktop]()

2. [Tablet]()

3. [Mobile]()
The implementation ended up slightly different.

#### Color Palette
With this color scheme I've tried to match as much as possible all the sites with the same theme and products.
These standard [Materialize Colors](https://materializecss.com/color.html) work quite well for my project.
![Color Palette](https://res.cloudinary.com/ddrsbzhmf/image/upload/v1612056886/chocolate-heaven/color-scheme-materialize_vypl9a.png)

### Defensive design

* User is not able to break the site by clicking buttons out of the expected order.
* All forms handle empty input fields by warning the user and not permitting recipe submission.
* Navigating between pages via the back/forward buttons does not break the site. 
* User errors do not cause database errors.
* User is given feedback for actions/errors by a 404 error page.

## Features
### Notes
* Admin features will not be available publicly for security reasons. Admin is able to browse, edit and delete all recipes and categories.
* Only as admin can view, edit or delete categories.
* Recipes can be viewed publicly by every user, but only can be edited by the user who created the recipe, specificaly.
* The use of JavaScript is limited only as Jquery to permit Materialize framework to take actions for the componets used.
* Materialize uses activator for cards so I've chosen to leave it without a proper intuitive button.
* Media queries are not all set for larger screens so the cards may overflow from their margins.

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

* [HTML](https://en.wikipedia.org/wiki/HTML5);
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets);
* [Jquery](https://jquery.com/);
* [Python](https://www.python.org/download/releases/3.8/);
    * [Flask](https://flask.palletsprojects.com/en/1.1.x/);
    * [Jinja](https://jinja.palletsprojects.com/en/2.10.x/);
    * Werkzeug security
* [MongoDB](https://www.mongodb.com/);
* [Materialize](https://materializecss.com/)
* [GitHub](https://github.com/);
* [GitPod](https://gitpod.io/);
* [Heroku](https://dashboard.heroku.com/);
* [MarkDownLit](https://dlaa.me/markdownlint/);
* [GoogleFonts](https://fonts.google.com/);
* [FontAwesome](https://fontawesome.com/)
* [Favicon](https://www.favicon-generator.org/);
* Google Chrome Developer tools
* Cloudinary.com to store all images

## Testing
Devices and platforms used for testing:

* Google Chrome.
* Mozilla Firefox.
* Opera.

- [x] laptop, laptop with touch (width 1440px);

- [x] Galaxy S5;

- [x] Pixel2, Pixel 2XL;

- [x] Iphone 5/SE, Iphone 6/7/8;

- [x] Iphone 6/7/8 Plus, IphoneX;

- [x] Ipad and Ipad Pro;

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