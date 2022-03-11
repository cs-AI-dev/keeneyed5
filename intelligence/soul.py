import sys
import random
import datetime
import os
os.system("py -m pip install nltk -q")  # Ensure NLTK is installed
os.system("py -m pip install tk -q")    # Ensure TKinter is installed
os.system("py -m pip install regex -q") # Ensure regular expressions module is installed

import nltk
from nltk.corpus import wordnet as wn        # WordNet language tree parser
from nltk.corpus import brown as browncorpus # Brown Corpus
from nltk.corpus import words as wordtk      # Word tokenizer
import tkinter as tk						 # TKinter GUI
from tkinter import Tk						 # TK Window
from tkinter import Label					 # TK Label
from tkinter import Frame					 # TK Frame
from tkinter import Entry					 # TK Entry
from tkinter import Button					 # TK Button
import re

import memory								 # Memory subsystem
import subroutine							 # Subroutines

cli = keeneyed5.cli

class gui:
	bg = "black"
	fg = "white"
	font = lambda size : ("OCR A Extended", size)

elements = {}

def add(name, element):
	try:
		elements[name] = element
		return True
	except Exception as e:
		return e

def assemble(intelligenceName):
	# Startup
	subroutine.srt_01()
	subroutine.srt_02()
	subroutine.srt_03()

	window = Tk()
	window.configure(bg=gui.bg)

	add("titlelbl", Label(window, text="Keeneyed-5 Artificial General Intelligence System", bg=gui.bg, fg=gui.fg, font=gui.font(24)))
	elements["titlelbl"].grid(row=1, column=1, columnspan=3)
	add("right", Frame(window, bg=gui.bg))
	elements["right"].grid(row=2, column=1, columnspan=1)
	add("left", Frame(window, bg=gui.bg))
	elements["left"].grid(row=2, column=3, columnspan=1)
	add("center", Frame(window, bg=gui.bg))
	elements["center"].grid(row=2, column=2, columnspan=1)

	add("interface", Label(elements["center"], text="", bg=gui.bg, fg=gui.fg, font=gui.font(12), height=25, width=100))
	elements["interface"].grid(row=1, column=1, columnspan=3)

	def post(usr, data):
		elements["interface"].config(text = f"[{usr}] {data}")

	add("datainput", Entry(elements["center"], text="", bg=gui.bg, fg=gui.fg, font=gui.font(12), width=70))
	elements["datainput"].grid(row=2, column=1, columnspan=1)

	def receive():
		cin = elements["datainput"].get()

		post("USER", cin)
		memory.record.shortterm([x + "." for x in cin.split(".")])
		output = "..."

		memcheck = subroutine.srt_01()
		for x in memcheck.all:
			if not x:
				subroutine.srt_02()
				break
		shorttermContext = memory.remember.shortterm(*[x for x in cin.split(" ")])
		longtermContext = memory.remember.longterm(*[x for x in cin.split(" ")])
		# KE5 process

		sent = []
		full = [] # list of lists
  		for word in cin.split(" "):
    		if word.endswith("~"):
				cli.display("[KE5:NLP:PUNCT] " + word + " ends with tilde")
				sent.append(word[:-1])
				sent.append("KE5:TILDE")
				full.append(sent)
				sent = []
    		elif word.endswith("..."):
				cli.display("[KE5:NLP:PUNCT] " + word + " ends with triple ellipsis")
				sent.append(word[:-3])
				sent.append("KE5:ELLIPSIS:TRIPLE")
				full.append(sent)
				sent = []
    		elif word.endswith(".."):
				cli.display("[KE5:NLP:PUNCT] " + word + " ends with double ellipsis")
				sent.append(word[:-2])
				sent.append("KE5:ELLIPSIS:DOUBLE")
				full.append(sent)
				sent = []
    		elif word.endswith("."):
				cli.display("[KE5:NLP:PUNCT] " + word + " ends with period")
				sent.append(word[:-1])
				sent.append("KE5:PERIOD")
				full.append(sent)
				sent = []
    		elif word.endswith(","):
				cli.display("[KE5:NLP:PUNCT] " + word + " ends with comma")
				sent.append(word[:-1])
				sent.append("KE5:COMMA")
				full.append(sent)
				sent = []
    		elif word.endswith(";"):
				cli.display("[KE5:NLP:PUNCT] " + word + " ends with semicolon")
				sent.append(word[:-1])
				sent.append("KE5:SEMICOLON")
				full.append(sent)
				sent = []
    		elif word.endswith(":"):
				cli.display("[KE5:NLP:PUNCT] " + word + " ends with colon")
				sent.append(word[:-1])
				sent.append("KE5:COLON")
				full.append(sent)
				sent = []
			elif word.endswith("?"):
				cli.display("[KE5:NLP:PUNCT] " + word + " ends with question")
				sent.append(word[:-1])
				sent.append("KE5:QUESTION_MARK")
				full.append(sent)
				sent = []
   			elif word.endswith("!"):
				cli.display("[KE5:NLP:PUNCT] " + word + " ends with exclamation")
				sent.append(word[:-1])
				sent.append("KE5:EXCLAMATION_MARK")
				full.append(sent)
				sent = []
    		elif word.endswith("?!") or word.endswith("!?"):
				cli.display("[KE5:NLP:PUNCT] " + word + " ends with interrobang")
				sent.append(word[:-2])
				sent.append("KE5:INTERROBANG")
				full.append(sent)
				sent = []
   			else:
				cli.display("[KE5:NLP:PUNCT] " + "appending raw " + word)
				sent.append(word)

		for sent in [x.strip() for x in re.split("; |, |\. |\? |\! |\:", cin)]: # Split text into sentence entities through the punctuation
			pass

		elements["datainput"].config(text="")

		post(intelligenceName, output)

	add("sendbutton", Button(elements["center"], text="INPUT DATA", bg="lime", fg="black", font=gui.font(12), width=10, command=receive))
	elements["sendbutton"].grid(row=2, column=2, columnspan=1)
	add("terminateconnectionbutton", Button(elements["center"], text="TERMINATE CONNECTION", bg="red", fg="black", font=gui.font(12), width=20, command=window.destroy))
	elements["terminateconnectionbutton"].grid(row=2, column=3, columnspan=1)

	window.mainloop()
