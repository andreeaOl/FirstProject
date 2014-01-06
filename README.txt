Web Page TITLE
=====================================================
A program that prints the title of a given web page.
-----------------------------------------------------
It contains two main files:
	prog.py
	prog_test.py
-----------------------------------------------------
SETUP

>virtualenv --no-site-packages venv
$ git clone git@redmine.platformable.net:fpapplication.git
>cd fpapplication
>venv/Scripts/activate  or  venv/bin/activate
>pip install -r requiements.txt
------------------------------------------------------
RUNNING THE PROGRAM

>python prog.py
Provide a full URL of a website:_
	The url provided must cotain 'http://www....'
------------------------------------------------------
RUNNING THE TEST

>coverage run prog_test.py
>coverage report