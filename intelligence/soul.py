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

class gui:
	bg = "black"
	fg = "white"
	font = lambda size : ("OCR A Extended", size)

window = Tk()
elements = {}

def add(name, element):
	try:
		elements[name] = element
		return True
	except Exception as e:
		return e
	
def assembleGUI():
	add("titleLbl", Label(window, text="Keeneyed-5 Artificial General Intelligence System", bg=gui.bg, fg=gui.fg, font=gui.font(48)))
	add("messages")
