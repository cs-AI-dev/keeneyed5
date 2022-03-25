import sys
import random
import datetime
import os
os.system("py -m pip install nltk -q")  # Ensure NLTK is installed
os.system("py -m pip install tk -q")    # Ensure TKinter is installed
os.system("py -m pip install regex -q") # Ensure regular expressions module is installed

# Make sure all required NLTK modules are downloaded!

import memory					 # Memory subsystem
import subroutine				 # Subroutines
import commandLineInterface as cli               # Command line interface

cli.display("[KE5:STARTUP] Importing NLTK packages ...")
import nltk
from nltk.corpus import wordnet as wn            # WordNet language tree parser
from nltk.corpus import brown as browncorpus     # Brown Corpus
from nltk.corpus import words as wordtk          # Word tokenizer
from nltk.corpus import words as all_words # All words
cli.display("[KE5:STARTUP] Importing Tkinter packages ...")
import tkinter as tk			         # TKinter GUI
from tkinter import Tk		                 # TK Window
from tkinter import Label		         # TK Label
from tkinter import Frame		         # TK Frame
from tkinter import Entry		         # TK Entry
from tkinter import Button		         # TK Button
cli.display("[KE5:STARTUP] Importing regular expression packages ...")
import re				         # Regular expression parsing

cli.display("[KE5:STARTUP] Importing all words ...")
all_words = all_words.words()

class gui:
	bg = "black"
	fg = "white"
	font = lambda size : ("OCR A Extended", size)

elements = {}

class SemanticLanguage:
	def __init__(self, word):
		self.word = word
		if word in all_words:
			self.is_registered_word = True
			self.synsets = wn.synsets(word)
			self.lemmas = [ss.lemmas() for ss in self.synsets]
			self.hypernyms = [ss.hypernyms() for ss in self.synsets]
			self.hyponyms = [ss.hyponyms() for ss in self.synsets]
			self.member_holonyms = [ss.member_holonyms() for ss in self.synsets]
			self.root_hypernyms = [ss.root_hyperynms() for ss in self.synsets]
			self.antonyms = [lemma.antonyms() for lemma in self.lemmas]
			self.pertainyms = [lemma.pertainyms() for lemma in self.lemmas]
			self.derivations = [lemma.derivationally_related_forms() for lemma in self.lemmas]
			self.frame_ids = [lemma.frame_ids() for lemma in self.lemmas]
			self.self_similarities = [ [ss1, [ss1.path_similarity(ss2) for ss2 in self.synsets if not ss1 == ss2] ] for ss1 in self.synsets ] # I don't like it but it works
		else:
			self.is_registered_word = False
			self.synsets = None
			self.lemmas = None
			self.hypernyms = None
			self.hyponyms = None
			self.member_holonyms = None
			self.root_hypernyms = None
			self.antonyms = None
			self.pertainyms = None
			self.derivations = None
			self.frame_ids = None
			self.self_similarities = None

def add(name, element):
	try:
		elements[name] = element
		return True
	except Exception as e:
		return e

def assemble(intelligenceName):
	cli.display("[KE5:GUI:ASSEMBLE] Assembling GUI ...")
	# Startup
	subroutine.srt_01()
	subroutine.srt_02()
	subroutine.srt_03()

	window = Tk()
	window.configure(bg=gui.bg)

	cli.display("    Assembling gridding ...")

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

	cli.display("    Assembling receiver ...")

	def receive():
		cin = elements["datainput"].get()

		post("USER", cin)
		# memory.record.shortterm([x + "." for x in cin.split(".")])
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
		conv = [] # list of SemanticLanguage
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
				cli.display("[KE5:NLP:PUNCT] appending raw " + word)
				sent.append(word)

		for sent in full:
			convsent = []
			for word in sent:
				if type(word) == type(""):
					convsent.append(word)
				else:
					convsent.append(SemanticLanguage(word))
			conv.append(convsent)

		memory.record.shortterm(full)

		elements["datainput"].config(text="")

		post(intelligenceName, output)

	cli.display("    Assembling receiver GUI and terminator ...")

	add("sendbutton", Button(elements["center"], text="INPUT DATA", bg="lime", fg="black", font=gui.font(12), width=10, command=receive))
	elements["sendbutton"].grid(row=2, column=2, columnspan=1),	add("terminateconnectionbutton", Button(elements["center"], text="TERMINATE CONNECTION", bg="red", fg="black", font=gui.font(12), width=20, command=window.destroy))
	elements["terminateconnectionbutton"].grid(row=2, column=3, columnspan=1)

	cli.display(cli.term.lime_on_black("    Done."))

	cli.display("[KE5:GUI] Starting connection ...")

	window.mainloop()
