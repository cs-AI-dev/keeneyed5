import os
import sys

import memory as mem
import subroutine
import commandLineInterface as cli
import soul

cli.display("[KE5:RT] Connecting subroutine driver to CLI ...")
subroutine.connectCLI(cli)
cli.display("[KE5:RT] Done.")

shorttermMemorySystem = None

def acceptInput(inp):
	# Commit to short-term memory
	pass

def initialize(name):
	global shorttermMemorySystem

	cli.display("[KE5:RT:INIT] Starting up Keeneyed-5 artificial general intelligence system ...\n")
	cli.display("    Checking short-term memory subsystem ...")
	shorttermMemorySystem = subroutine.srt_01()
	status = True
	for x in shorttermMemorySystem.all:
		if not x:
			status = False
	if not status:
		cli.display(cli.term.yellow_on_black("    WARN: Anomaly detected in short-term memory caches. Resetting ..."))
		subroutine.srt_02()
		cli.display("    Short-term memory caches reset. Reloading ...")
		shorttermMemorySystem = subroutine.srt_01()
		cli.display("    Reload complete. Checking subsystem again ...")
		status = True
		for x in shorttermMemorySystem.all:
			if not x:
				status = False
		if not status:
			cli.display(cli.term.red_on_black("    ERROR: Short-term memory subsystem failure. Continue? (y/n)"))
			with term.cbreak(), term.hidden_cursor():
				usr = None
				while True:
					inkey = cli.term.inkey()
					if inkey.lower() == "y":
						usr = True
						break
					elif inkey.lower() == "n":
						usr = False
						break
					else:
						pass
				if usr == False:
					cli.display("    Short-term memory subsystem error detected, user override activated. Continuing ...")
				else:
					cli.display("        Exiting ...")
					return 0
	else:
		cli.display("    Short-term memory subsystem intact and functional. Continuing ...")

	cli.display("    Creating long-term memory cache ...")
	subroutine.srt_03()
	cli.display("    Assembling GUI ...")
	soul.assemble(name)
