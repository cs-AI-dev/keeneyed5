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

elements = {}

def add(name, element):
	try:
		elements[name] = element
		return True
	except Exception as e:
		return e

def assembleGUI():
	window = Tk()

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
	add("datainput", Entry(elements["center"], text="", bg=gui.bg, fg=gui.fg, font=gui.font(12), width=70))
	elements["datainput"].grid(row=2, column=1, columnspan=1)
	add("sendbutton", Button(elements["center"], text="INPUT DATA", bg="lime", fg="black", font=gui.font(12), width=10, command=sendData))
	elements["sendbutton"].grid(row=2, column=2, columnspan=1)
	add("terminateconnectionbutton", Button(elements["center"], text="TERMINATE CONNECTION", bg="red", fg="black", font=gui.font(12), width=20, command=window.destroy))
	elements["terminateconnectionbutton"].grid(row=2, column=3, columnspan=1)

	window.mainloop()
