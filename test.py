#!/usr/bin/env python

from termcolor import colored
import os

docker = os.system("docker build -t benog-belgium/website .")
flake = os.system('flake8 --ignore=E501,F401,E402,F811,E731,F403 .')


if os.system("./manage.py check") == 0:
    print("./manage.py check =>" + colored("passed", "green"))
else:
    print("./manage.py check =>" + colored("failed", "red"))


if flake == 256:
    print("flake8            =>" + colored("passed", "green"))
else:
    print("flake8            =>" + colored("failed", "red"))


if docker == 0:
    print("Docker Build      =>" + colored("passed", "green"))
else:
    print("Docker Build      =>" + colored("failed", "red"))
