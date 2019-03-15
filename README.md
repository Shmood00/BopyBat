# Secure Software Assignment 2 - BopyBat

By: Adam and Dyllon

Student IDs: 991451175 and 991447068, respectively

## Setup
We used a fresh Ubuntu 16.04 install and Django 2.1.7 and mysql 5.7

We then followed a tutorial to set up a base for the pastebin app

[The tutorial can be seen here](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)

After completing the tutorial we started to edit the files to meet the requirements.

### Pastebin-like URLs
We first editted the project to work with pastebin-like urls.  We did this by editing 3 files:
* [The models.py file](/software/secbin/pastebin/models.py)
* [The views.py file](/software/secbin/pastebin/views.py)
* [The urls.py file](/software/secbin/pastebin/urls.py)

We also used a python base 62 converter that we got from [here](https://gist.github.com/Biglucky/da106aabab769cf25396262eb72783db)

## Packages Needed
In order for the project to properly be run on your machine there are some packages needed to be installed:
* ```pip install crispy_forms```
* ```pip install django-sslserver```
* ```pip install Pillow```

## Running The Program
To run the Web App on your server, do the following:
* Clone this respository on your local machine
* Once cloned, direct yourself to the ```/software/secbin/``` folder, which contains the [manage.py](/software/secbin/manage.py) file
* Once in the proper directory, run the following to execute the server:```sudo python3 manage.py runsslserver```
* To view the Web App open your preferred browser and direct yourself to: [https://localhost:8000/](https://localhost:8000)
* NOTE: If you would like to test the "Forgot Password" functionality, please open up a new terminal on your machine and run the following command in order run a local SMTP server: ```python -m smtpd -n -c DebuggingServer localhost:1025```

## How Disabling Posts Work
In order to get administrator to be able to disable specific posts, we first had to add a new boolean field (```disable_bopie```) to the Bopie class located in [models.py](/software/secbin/pastebin/models.py). Because this field is only accessible to the administrators, we did not have to add this new field to our ```PostCreateView``` class in [views.py](/software/secbin/pastebin/views.py).

Once the boolean field was added into [models.py](/software/secbin/pastebin/models.py), we had to make sure that disabled posts would not be displayed. In order to do this, we added the ```get_queryset()``` in [views.py](/software/secbin/pastebin/views.py) within our ```PostListView``` class. Within the ```get_queryset()``` function we added a query to grab posts that have the ```disable_bopie``` field set to ```False```. Because this function was in our ```PostListView``` class, it will only show users posts based on whatever the ```get_queryset()``` function returns.
