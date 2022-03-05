from os.path import exists as fileexists
from os import system as oscmd
import datetime
import memory

cli = None
def connectCLI(package):
	global cli

	cli = package

class ShorttermMemorySystemStatus:
	def __init__(this):
		cli.display("    Assembling short-term memory statuses ...")

		this.cache_0 = None
		tfr = open(__file__[:-13] + "memory/shortterm/memory_cache_0.ke5", "r")
		if tfr.read().strip().split("\n")[0].strip() == "KE5STMC0":
			this.cache_0 = True
			cli.display("        SHORT TERM MEMORY CACHE 0 " + cli.term.lime_on_black("[  OK  ]"))
			tfr.close()
		else:
			this.cache_0 = False
			cli.display("        SHORT TERM MEMORY CACHE 0 " + cli.term.red_on_black("[ WARN ]"))
			tfr.close()

		this.cache_1 = None
		tfr = open(__file__[:-13] + "memory/shortterm/memory_cache_1.ke5", "r")
		if tfr.read().strip().split("\n")[0].strip() == "KE5STMC1":
			this.cache_1 = True
			cli.display("        SHORT TERM MEMORY CACHE 1 " + cli.term.lime_on_black("[  OK  ]"))
			tfr.close()
		else:
			this.cache_1 = False
			cli.display("        SHORT TERM MEMORY CACHE 1 " + cli.term.red_on_black("[ WARN ]"))
			tfr.close()

		this.cache_2 = None
		tfr = open(__file__[:-13] + "memory/shortterm/memory_cache_2.ke5", "r")
		if tfr.read().strip().split("\n")[0].strip() == "KE5STMC2":
			this.cache_2 = True
			cli.display("        SHORT TERM MEMORY CACHE 2 " + cli.term.lime_on_black("[  OK  ]"))
			tfr.close()
		else:
			this.cache_2 = False
			cli.display("        SHORT TERM MEMORY CACHE 2 " + cli.term.red_on_black("[ WARN ]"))
			tfr.close()

		this.cache_3 = None
		tfr = open(__file__[:-13] + "memory/shortterm/memory_cache_3.ke5", "r")
		if tfr.read().strip().split("\n")[0].strip() == "KE5STMC3":
			this.cache_3 = True
			cli.display("        SHORT TERM MEMORY CACHE 3 " + cli.term.lime_on_black("[  OK  ]"))
			tfr.close()
		else:
			this.cache_3 = False
			cli.display("        SHORT TERM MEMORY CACHE 3 " + cli.term.red_on_black("[ WARN ]"))
			tfr.close()

		this.cache_4 = None
		tfr = open(__file__[:-13] + "memory/shortterm/memory_cache_4.ke5", "r")
		if tfr.read().strip().split("\n")[0].strip() == "KE5STMC4":
			this.cache_4 = True
			cli.display("        SHORT TERM MEMORY CACHE 4 " + cli.term.lime_on_black("[  OK  ]"))
			tfr.close()
		else:
			this.cache_4 = False
			cli.display("        SHORT TERM MEMORY CACHE 4 " + cli.term.red_on_black("[ WARN ]"))
			tfr.close()

		this.cache_5 = None
		tfr = open(__file__[:-13] + "memory/shortterm/memory_cache_5.ke5", "r")
		if tfr.read().strip().split("\n")[0].strip() == "KE5STMC5":
			this.cache_5 = True
			cli.display("        SHORT TERM MEMORY CACHE 5 " + cli.term.lime_on_black("[  OK  ]"))
			tfr.close()
		else:
			this.cache_4 = False
			cli.display("        SHORT TERM MEMORY CACHE 5 " + cli.term.red_on_black("[ WARN ]"))
			tfr.close()

		this.cache_6 = None
		tfr = open(__file__[:-13] + "memory/shortterm/memory_cache_6.ke5", "r")
		if tfr.read().strip().split("\n")[0].strip() == "KE5STMC6":
			this.cache_6 = True
			cli.display("        SHORT TERM MEMORY CACHE 6 " + cli.term.lime_on_black("[  OK  ]"))
			tfr.close()
		else:
			this.cache_6 = False
			cli.display("        SHORT TERM MEMORY CACHE 6 " + cli.term.red_on_black("[ WARN ]"))
			tfr.close()

		this.cache_7 = None
		tfr = open(__file__[:-13] + "memory/shortterm/memory_cache_7.ke5", "r")
		if tfr.read().strip().split("\n")[0].strip() == "KE5STMC7":
			this.cache_7 = True
			cli.display("        SHORT TERM MEMORY CACHE 7 " + cli.term.lime_on_black("[  OK  ]"))
			tfr.close()
		else:
			this.cache_7 = False
			cli.display("        SHORT TERM MEMORY CACHE 7 " + cli.term.red_on_black("[ WARN ]"))
			tfr.close()

		this.cache_8 = None
		tfr = open(__file__[:-13] + "memory/shortterm/memory_cache_8.ke5", "r")
		if tfr.read().strip().split("\n")[0].strip() == "KE5STMC8":
			this.cache_8 = True
			cli.display("        SHORT TERM MEMORY CACHE 8 " + cli.term.lime_on_black("[  OK  ]"))
			tfr.close()
		else:
			this.cache_8 = False
			cli.display("        SHORT TERM MEMORY CACHE 8 " + cli.term.red_on_black("[ WARN ]"))
			tfr.close()

		this.cache_9 = None
		tfr = open(__file__[:-13] + "memory/shortterm/memory_cache_9.ke5", "r")
		if tfr.read().strip().split("\n")[0].strip() == "KE5STMC9":
			this.cache_9 = True
			cli.display("        SHORT TERM MEMORY CACHE 9 " + cli.term.lime_on_black("[  OK  ]"))
			tfr.close()
		else:
			this.cache_9 = False
			cli.display("        SHORT TERM MEMORY CACHE 9 " + cli.term.red_on_black("[ WARN ]"))
			tfr.close()

		this.all = [this.cache_0, this.cache_1, this.cache_2, this.cache_3, this.cache_4, this.cache_5, this.cache_6, this.cache_7, this.cache_8, this.cache_9]

def srt_01(): # Check if memory systems are intact
	cli.display("[KE5:SRT:01] Running subroutine 1 ...")
	out = ShorttermMemorySystemStatus()
	cli.display("[KE5:SRT:01] Subroutine finished.")
	return out

def srt_02(): # Reset short-term memory caches
	cli.display("[KE5:SRT:02] Running subroutine 2 ...")
	syscheck = srt_01().all
	for x in range(10):
		cli.display("    Resetting long-term memory cache ...")
		cli.display("        FILE CONTENT: ")
		with open(__file__[:-13] + "memory/shortterm/memory_cache_" + str(x) + ".ke5", "r") as f:
			cli.display(f.read())
		f = open(__file__[:-13] + "memory/shortterm/memory_cache_" + str(x) + ".ke5", "w")
		f.write("KE5STMC" + str(x))
		f.close()
		cli.display("    Memory cache reset.")
	cli.display("[KE5:SRT:02] Subroutine finished.")

def srt_03(day=datetime.datetime.today().day, month=datetime.datetime.today().month, year=datetime.datetime.today().year): # Generate new long-term memory cache
	cli.display("[KE5:SRT:03] Running subroutine 3 ...")
	try:
		with open(__file__[:-13] + "/memory/longterm/" + "d" + str(day) + "m" + str(month) + "y" + str(year) + ".ke5", "x") as f:
			pass
	except FileExistsError:
		pass
	except exception as e:
		raise e
	with open(__file__[:-13] + "/memory/longterm/" + "d" + str(day) + "m" + str(month) + "y" + str(year) + ".ke5", "a") as f:
		if not fileexists(__file__[:-3] + "/longterm/" + "d" + str(day) + "m" + str(month) + "y" + str(year) + ".ke5"):
			pass
		else:
			f.write(memory.breaksentinel)
	cli.display("[KE5:SRT:03] Subroutine finished.")
