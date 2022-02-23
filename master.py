# Copyright Jacob Bodell 2022.
# All rights reserved.

# py E:/keeneyed5/master.py

import sys
import math
import blessed
import time
import psutil

from nltk.corpus import wordnet as wn
from nltk.corpus import reader as corpusReader
from nltk.corpus import brown as corpus_brown

import internalUtilities as utils
import commandLineInterface as cli
from commandLineInterface import term

cli.resetCLI()

cli.display("Keeneyed-5 artificial general intelligence system loaded.")
cli.display("Enter any command to begin.")

while True:

    fullcmd = cli.getUserInput("/")
    carg = fullcmd.split(" ")
    cname = carg[0]

    try:
        if cname in ["systemexit", "sysexit", "exit", "e"]:
            print(term.clear())
            break

        elif cname in ["run", "r"]:
            if carg[1] == "diagnostic":
                if carg[2] == "1":
                    cli.display("Running type-1 diagnostic.")
                    cli.display("    Searching open processes for open files.")
                    targetProcessOpenFiles = []
                    for proc in psutil.process_iter():
                        try:
                            cli.display("        " + str(proc.name).split("name=\'")[1].split("\'")[0])
                            for file in proc.open_files():
                                cli.display("            " + str(file.path))
                            if str(proc.name).split("name=\'")[1].split("\'")[0] in ["cmd.exe", "py.exe", "python.exe"]:
                                try:
                                    for file in proc.open_files():
                                        targetProcessOpenFiles.append(file)
                                except psutil.AccessDenied:
                                    display(term.yellow_on_black("WARNING: The system has been denied access to its executing processes."))
                                    display(term.yellow_on_black("         This error could cause undesirable operation. Ensure that all"))
                                    display(term.yellow_on_black("         required permissions are granted to the program prior to more"))
                                    display(term.yellow_on_black("         usage of the Keeneyed-5 system."))

                        except psutil.AccessDenied:
                            cli.display("        Access to process " + str(proc.name).split("name=\'")[1].split("\'")[0] + " is denied.")
                            continue
                    cli.display("    Search complete.")
                    [cli.display(" ") for x in range(3)]
                    cli.display("    Checking used system files ...")
                    nonSystemFilesPresent = False
                    for file in targetProcessOpenFiles:
                        if str(file).split("path=\'")[1].split("\', fd=")[0].split("\\\\")[2] == "System32":
                            cli.display("        SYSTEM FILE: " + str(file).split("path=\'")[1].split("\', fd=")[0])
                        else:
                            cli.display("        NON-SYSTEM FILE: " + str(file).split("path=\'")[1].split("\', fd=")[0])
                            nonSystemFilesPresent = True
                    if nonSystemFilesPresent:
                        cli.display(term.lime_on_black("DIAGNOSTIC COMPLETE"))
                        cli.display(term.yellow_on_black("    Non-system files detected being used by the Keeneyed-5 system. Restart recommended."))
                    else:
                        cli.display(term.lime_on_black("DIAGNOSTIC COMPLETE"))
                        cli.display(term.lime_on_black("    No non-system files detected."))
                else: # diagnostic
                    cli.display(term.red_on_black("Type-" + carg[1] + " diagnostic program not found."))

            elif carg[1] == "query":
                if len(carg) == 2:
                    cli.display("Target a subsystem to query.")
                    cli.display(" 1. Programs")
                    cli.display(" 2. Diagnostic")
                    cli.display(" 3. Intelligence")
                    while True:
                        usr = cli.getUserInput("?")
                        if not usr in ["1", "2", "3"]:
                            cli.display("Invalid subsystem ID number, try again")
                        else:
                            subsystemID = int(usr)
							break
					if subsystemID == 1:
						pass
					elif subsystemID == 2:
						pass
					elif subsystemID == 3:
						pass
                elif len(carg) == 3:
                    pass
                else:
                    pass

            else: # run
                cli.display(term.red_on_black("Unknown program \"" + carg[1] + "\"."))

        elif cname in ["transcript", "t"]:
            if carg[1] in ["print", "printto"]:
                cli.display("Copying transcript ...")
                ft = open(carg[2], "w")
                fo = open(__file__[:-10] + "/executionTranscripts/current.ke5", "r")

                ft.write(fo.read())

                ft.close()
                fo.close()
                cli.display("Transcript copying complete.")
				
            elif carg[1] in ["clear", "c"]:
                cli.display("Clearing transcript ...")
                fo = open(__file__[:-10] + "/executionTranscripts/current.ke5", "w")
                fo.write("\n")
				fo.close()
				cli.display("Transcript cleared.")
            
			else:
                cli.display(term.red_on_black("Unknown transcript option \"" + carg[2] + "\"."))

        else: # Command level
            cli.display(term.red_on_black("Unknown command \"" + cname + "\"."))
			
    except KeyboardInterrupt:
        cli.resetCLI()
        cli.display("Keeneyed-5 process successfully interrupted.")
        cli.display(term.yellow_on_black("WARNING: Keyboard process interruptions can cause glitches to occur in opened files."))
        cli.display(term.yellow_on_black("         If the terminated process contained operations involving opening files, run"))
        cli.display(term.yellow_on_black("         a type-1 system diagnostic."))

print(term.lime_on_black("System exited."))
