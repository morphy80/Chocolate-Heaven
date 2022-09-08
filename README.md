## Data - Centric Development Project, MS3-Code Institute
# Chocolate Heaven

![site logo](https://res.cloudinary.com/ddrsbzhmf/image/upload/v1612475355/chocolate-heaven/favicon-32x32_cev9j6.png)
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

![demo2](https://res.cloudinary.com/ddrsbzhmf/image/upload/v1612474916/chocolate-heaven/ezgif.com-gif-maker_v6pwth.gif)

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
- [x] Be able to access, edit and delete ALL recipes and categories from admin profile

### Developer goals

 * Provide a simple, easy to use online cookbook where user can browse, post, edit and delete recipes, filter them by categories, search by text, subscribe and have profile.
 * By practice learn Jinja templating, Python, non-relational database MongoDb 
 * Improve Bootstrap and JavaScript knowledge.
 * Learn to use Heroku Pages

### Design

![Demo Picture](https://res.cloudinary.com/ddrsbzhmf/image/upload/v1612473338/chocolate-heaven/rsz_screenshot_2021-02-04_221344_kclhzh.png)

Main inspiration for the page design comes from [purdys](https://www.purdys.com/) which has an extraordinary selection of chocolates and the variety is well documented and illustrated.


Fonts used: [Bubblegum Sans](https://fonts.google.com/specimen/Bubblegum+Sans?query=bubb&preview.text_type=custom), [Emilys Candy](https://fonts.google.com/specimen/Emilys+Candy?query=Emilys+Candy&preview.text_type=custom), [Rye](https://fonts.google.com/specimen/Rye?query=Rye&preview.text_type=custom),
 [Special Elite](https://fonts.google.com/specimen/Special+Elite?query=Special+Elite&preview.text_type=custom) imported from Google Fonts.
#### Research

#### Wireframes

I created my wireframes during the Scope Plane of this project.
I made wireframes for each page of the site from three different type of devices:

* [home_page](https://res.cloudinary.com/ddrsbzhmf/image/upload/v1612476832/chocolate-heaven/Screenshot_2021-02-04_231017_xpigdh.png)
* [recipes_page](https://res.cloudinary.com/ddrsbzhmf/image/upload/v1612476834/chocolate-heaven/Screenshot_2021-02-04_231046_n0nn70.png)
* [recipe_page_front](https://res.cloudinary.com/ddrsbzhmf/image/upload/v1612476836/chocolate-heaven/Screenshot_2021-02-04_231112_kqair8.png)
* [recipe_page_reveal](https://res.cloudinary.com/ddrsbzhmf/image/upload/v1612476838/chocolate-heaven/Screenshot_2021-02-04_231138_wiouja.png)
* [log_in](https://res.cloudinary.com/ddrsbzhmf/image/upload/v1612476839/chocolate-heaven/Screenshot_2021-02-04_231156_x86hba.png)
* [register](https://res.cloudinary.com/ddrsbzhmf/image/upload/v1612476842/chocolate-heaven/Screenshot_2021-02-04_231223_h8otfl.png)
* [add_recipe_form](https://res.cloudinary.com/ddrsbzhmf/image/upload/v1612476843/chocolate-heaven/Screenshot_2021-02-04_231242_rffs3v.png)

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
* Not as a footnote but as a first mention: due to the limited time at hand (less than a week!) I had to structure everything to a bare minimum of functionality and layout.
* Admin features will not be available publicly for security reasons. Admin is able to browse, edit and delete all recipes and categories.
* Only as admin can view, edit or delete categories.
* Recipes can be viewed publicly by every user, but only can be edited by the user who created the recipe, specificaly.
* The use of JavaScript is limited only as Jquery to permit Materialize framework to take actions for the componets used.
* Materialize uses activator for cards so I've chosen to leave it without a proper intuitive button.
* Media queries are not all set for larger screens so the cards may overflow from their margins.

### Existing features

- [x] Favicon
- [x] Navbar with submenu for the profile user;
- [x] User logged in can view the edit function of the recipes;
- [x] Admin can add, edit and delete categories and recipes;
- [x] Title of the recipe;
- [x] List of ingredients formatted with split() method;
- [x] The recipe's Instructions;
- [x] The picture of the recipe;
- [x] The category of the recipe;
- [x] More options with:-- Edit
                        -- Delete
- [x] Register;
- [x] Login;
- [x] Search on both home and recipes page;
- [x] Links as shortcuts for smother navigation;

### Future features

- [ ] Pagination
- [ ] Scroll back to top button
- [ ] Recipe image url validation
- [ ] Tooltips
- [ ] Add reviews
- [ ] Add prep and cooking time
- [ ] Ingredients and Instructions listed in arrays instead of strings
- [ ] Lazy loading images 
- [ ] Calories calculations
- [ ] Server side credential validation
- [ ] SSL certificate
- [ ] Contact form and admin to be able to see all recieved messages directly in the admin console

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
* EZGIF to convert demo video to gif

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
* Searching function as a query for recipes might land to the error 404 page. It's a function in progress not yet perfectly implemented.
* Most of the errors I encountered along the way were simply syntax mistakes.

Current issues:
* Some of the text or image may overflow due to the unfinished Css.
* Seach function as mentioned is a 'work in progress'.
* Images uploaded may not have the standardized size or may render unevenly.

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

## Credits
### Code

### Images
Images are mostly taken from [Unsplash](https://unsplash.com/) and Google Images.

### Content 
* Recipes taken from various websites, some of them linked in the Tips section.

## Acknowledgements
Big thansk to tutor support team : Code Institute Tutor support (especially [
Tim Nelson](https://github.com/TravelTimN) for tutorial and tips), Igor, Kevin, Scott and Miklos and all Slack community.

Special thanks to my coding budy and friend Sabine M.

## Disclaimer

This project is for educational purposes only.

Alexander Apostoiu

2021

[Back to top ↑](#Chocolate-Heaven)