import sys
import random
import datetime
import os
os.system("py -m pip install nltk -q")
os.system("py -m pip install tk -q")

import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import brown as browncorpus
from nltk.corpus import words as wordtk
import tkinter as tk
from tkinter import Tk
from tkinter import Label
from tkinter import Frame
from tkinter import Entry
from tkinter import Button

import memory
import subroutine

def sendData():
	pass

class gui:
	bg = "black"
	fg = "white"
	font = lambda size : ("OCR A Extended", size)

window = Tk()

def terminateConnection():
	window.destroy() # Terminates connection, since the beginConnection() function
	                 # calls the mainloop which ends when the window is closed

elements = {}

def add(name, element):
	try:
		elements[name] = element
		return True
	except Exception as e:
		return e

def assembleGUI():
	add("titlelbl", Label(window, text="Keeneyed-5 Artificial General Intelligence System", bg=gui.bg, fg=gui.fg, font=gui.font(48)))
	elements["titlelbl"].grid(row=1, column=1, columnspan=3)
	add("right", Frame(window, bg=gui.bg))
	elements["right"].grid(row=2, column=1, columnspan=1)
	add("left", Frame(window, bg=gui.bg))
	elements["left"].grid(row=2, column=3, columnspan=1)
	add("center", Frame(window, bg=gui.bg))
	elements["center"].grid(row=2, column=2, columnspan=1)
	
	add("interface", Label(center, text="", bg=gui.bg, fg=gui.fg, font=gui.font(12), height=80, width=150))
	elements["interface"].grid(row=1, column=1, columnspan=3)
	add("datainput", Entry(center, text="", bg=gui.bg, fg=gui.fg, font=gui.font(12), height=20, width=100))
	elements["datainput"].grid(row=2, column=1, columnspan=1)
	add("sendbutton", Button(center, text="INPUT DATA", bg="lime", fg="black", font=gui.font(18), height=20, width=20, command=sendData))
	elements["sendbutton"].grid(row=2, column=2, columnspan=1)
	add("terminateconnectionbutton"), Button(center, text="TERMINATE CONNECTION", bg="red", fg="black", height=20, width=30, command=terminateConnection))

	
def startConnection():
	assembleGUI()
	window.mainloop()
