# Python Django Tutorial Files
### Setup Anaconda / Django / Atom
Windows Instructions (Linux and Apple may be similar).
1. [Install Anaconda](https://www.anaconda.com/distribution/), which is a set of tools that comes with Python distributions.  Optionally, you can install Python, but keep in mind that the commands below for creating your first project explicitly use 'conda' rather than the equivalen python or django commands.  To make sure that you have correctly installed Anaconda go to the Command Prompt or Terminal and type:  `conda info --all` which should spit out a number of details about your configuration environment.
2. Install the [Atom Integrated Development Environment (IDE)](https://atom.io)
3.    Use the Atom package installer (**File >> Settings >> Install**) to add the following packages:
  + platformio-ide-terminal - this package provides a terminal window to use in Atom
  + language-markdown - this package helps Atom understand and write [Markdown Language](https://daringfireball.net/projects/markdown/syntax)
  + markdown-writer - this package helps Atom write files in the correct .md format
  + markdown-preview (this may already be installed) - this package allows you to preview markdown files in your Atom IDE
1. Install [The Django Framework](https://www.djangoproject.com) by using `pip install django` or alternatively `conda install django` (Anaconda comes with its own package manager).  [Pip](https://pypi.org/project/pip/) is the Default Package Manager for Python.  When complete, you should be able to check the versions of Python `python --version` and Django `python -m django version`.

### Create your First Project
Windows / Mac / Linux Instructions (should use same commands)
1. Using the Command Prompt or Terminal program, Create a new Project `django-admin startproject [mysite]` where **mysite** refers to the name of the project.  The command should create a new directory in which it will write all of your project files.
2. Navigate your Command Prompt or Terminal into your project directory `cd mysite` before setting up a virtual python environment.
3. Set up a virtual environment by calling:  `conda create --name mysite python=3.6` where mysite is the name of your project.
4. Activate your virtual environment by calling:  `conda activate mysite`
5. To begin Running our Default Application in the Virtual Environment, type:  `python manage.py runserver`, this command is equivalent to `npm start` in Node, and instructs the computer to run scripts that will start running a test server at an address local to your machine.
6. To view the server in your web browser, copy and paste the address (yours may differ from mine) into your web browser:  `http://127.0.0.1:8000`
7. Typing `Ctrl + C` into your Command Prompt / Terminal will kill the Server, which can be restarted by repeating the command `python manage.py runserver`
8. The runserver command builds a rapid testing environment which is not intended for production use.


### Follow Tutorial to build Polls App
[Django Tutorials to Build a Polls App](https://docs.djangoproject.com/en/2.2/intro/tutorial01/)

Django is a **Model, View, Template (MVT)** framework.

[The Django 8 Hour Course](https://www.youtube.com/watch?v=JT80XhYJdBw&t) goes through the tutorial at a high level, but can be difficult to follow.  Make sure you have both resources open if you choose to work through the video.
