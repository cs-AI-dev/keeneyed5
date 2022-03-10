import os
import commandLineInterface as cli

cli.display("Installing PIP upgrade ...")
os.system("py -m pip install --upgrade pip -q --no-warn-script-location")
cli.display("done.")
cli.display("Installing psutil process management system ...")
os.system("py -m pip install psutil -q --no-warn-script-location")
cli.display("done.")
cli.display("Installing TKinter GUI module ...")
os.system("py -m pip install tk -q --no-warn-script-location")
cli.display("done.")
cli.display("Installing NLTK natural language processing system ...")
os.system("py -m pip install nltk -q --no-warn-script-location")
cli.display("done.")
