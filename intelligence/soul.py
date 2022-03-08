import sys
import random
import datetime
import os
os.system("py -m pip install nltk -q") # Ensure NLTK is installed
os.system("py -m pip install tk -q")   # Ensure TKinter is installed

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

import memory								 # Memory subsystem
import subroutine							 # Subroutines

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
		post("USER", elements["datainput"].get())
		memory.record.shortterm([x + "." for x in elements["datainput"].get().split(".")])
		output = "..."
		
		memcheck = subroutine.srt_01()
		for x in memcheck.all:
			if not x:
				subroutine.srt_02()
				break
		ctxShort = memory.remember.shortterm(*[x for x in elements["datainput"].get().split(" ")])
		ctxLong = memory.remember.longterm(*[x for x in elements["datainput"].get().split(" ")])
		# KE5 process
		
		post(intelligenceName, output)
	
	add("sendbutton", Button(elements["center"], text="INPUT DATA", bg="lime", fg="black", font=gui.font(12), width=10, command=receive))
	elements["sendbutton"].grid(row=2, column=2, columnspan=1)
	add("terminateconnectionbutton", Button(elements["center"], text="TERMINATE CONNECTION", bg="red", fg="black", font=gui.font(12), width=20, command=window.destroy))
	elements["terminateconnectionbutton"].grid(row=2, column=3, columnspan=1)

	window.mainloop()
