![SHAME](https://api.travis-ci.org/BENOG-belgium/website.svg?branch=master)

# beNog Website :
## What :
This is the brand new website of the beNOG. Old one was only static HTML. This one has been planned to be able to plan events.

## How does this repo works :
Master is the head for dev. The running version is in the release on the right (on github)

## Run :
```
virtualenv ve3
source ve3/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver
```

## Todo :
* Event Page (being able to set up events from admin page and register with user name)
* Mailing List
* Wiki
* Sponsors
* Making it all pretty
