from os.path import exists as fileexists
from os import system as oscmd
import memory

cli = None
def connectCLI(package):
	global cli

	cli = package

class ShorttermMemorySystemStatus:
	def __init__(this):
		cli.display("    Assembling short-term memory statuses ...")
		this.cache_0 = fileexists(__file__[:-13] + "/memory/shortterm/memory_cache_0.ke5") and open(__file__[:-13] + "memory/shortterm/memory_cache_0.ke5", "r").read().split("\n")[0] == "KE5STMC0"
		if this.cache_0:
			cli.display("        SHORT TERM MEMORY CACHE 0 [  OK  ]")
		else:
			cli.display("        SHORT TERM MEMORY CACHE 0 [ WARN ]")

		this.cache_1 = fileexists(__file__[:-13] + "/memory/shortterm/memory_cache_1.ke5") and open(__file__[:-13] + "memory/shortterm/memory_cache_1.ke5", "r").read().split("\n")[0] == "KE5STMC1"
		if this.cache_1:
			cli.display("        SHORT TERM MEMORY CACHE 1 [  OK  ]")
		else:
			cli.display("        SHORT TERM MEMORY CACHE 1 [ WARN ]")

		this.cache_2 = fileexists(__file__[:-13] + "/memory/shortterm/memory_cache_2.ke5") and open(__file__[:-13] + "memory/shortterm/memory_cache_2.ke5", "r").read().split("\n")[0] == "KE5STMC2"
		if this.cache_2:
			cli.display("        SHORT TERM MEMORY CACHE 2 [  OK  ]")
		else:
			cli.display("        SHORT TERM MEMORY CACHE 2 [ WARN ]")

		this.cache_3 = fileexists(__file__[:-13] + "/memory/shortterm/memory_cache_3.ke5") and open(__file__[:-13] + "memory/shortterm/memory_cache_3.ke5", "r").read().split("\n")[0] == "KE5STMC3"
		if this.cache_3:
			cli.display("        SHORT TERM MEMORY CACHE 3 [  OK  ]")
		else:
			cli.display("        SHORT TERM MEMORY CACHE 3 [ WARN ]")

		this.cache_4 = fileexists(__file__[:-13] + "/memory/shortterm/memory_cache_4.ke5") and open(__file__[:-13] + "memory/shortterm/memory_cache_4.ke5", "r").read().split("\n")[0] == "KE5STMC4"
		if this.cache_4:
			cli.display("        SHORT TERM MEMORY CACHE 4 [  OK  ]")
		else:
			cli.display("        SHORT TERM MEMORY CACHE 4 [ WARN ]")

		this.cache_5 = fileexists(__file__[:-13] + "/memory/shortterm/memory_cache_5.ke5") and open(__file__[:-13] + "memory/shortterm/memory_cache_5.ke5", "r").read().split("\n")[0] == "KE5STMC5"
		if this.cache_5:
			cli.display("        SHORT TERM MEMORY CACHE 5 [  OK  ]")
		else:
			cli.display("        SHORT TERM MEMORY CACHE 5 [ WARN ]")

		this.cache_6 = fileexists(__file__[:-13] + "/memory/shortterm/memory_cache_6.ke5") and open(__file__[:-13] + "memory/shortterm/memory_cache_6.ke5", "r").read().split("\n")[0] == "KE5STMC6"
		if this.cache_6:
			cli.display("        SHORT TERM MEMORY CACHE 6 [  OK  ]")
		else:
			cli.display("        SHORT TERM MEMORY CACHE 6 [ WARN ]")

		this.cache_7 = fileexists(__file__[:-13] + "/memory/shortterm/memory_cache_7.ke5") and open(__file__[:-13] + "memory/shortterm/memory_cache_7.ke5", "r").read().split("\n")[0] == "KE5STMC7"
		if this.cache_7:
			cli.display("        SHORT TERM MEMORY CACHE 7 [  OK  ]")
		else:
			cli.display("        SHORT TERM MEMORY CACHE 7 [ WARN ]")

		this.cache_8 = fileexists(__file__[:-13] + "/memory/shortterm/memory_cache_8.ke5") and open(__file__[:-13] + "memory/shortterm/memory_cache_8.ke5", "r").read().split("\n")[0] == "KE5STMC8"
		if this.cache_8:
			cli.display("        SHORT TERM MEMORY CACHE 8 [  OK  ]")
		else:
			cli.display("        SHORT TERM MEMORY CACHE 8 [ WARN ]")

		this.cache_9 = fileexists(__file__[:-13] + "/memory/shortterm/memory_cache_9.ke5") and open(__file__[:-13] + "memory/shortterm/memory_cache_9.ke5", "r").read().split("\n")[0] == "KE5STMC9"
		if this.cache_9:
			cli.display("        SHORT TERM MEMORY CACHE 9 [  OK  ]")
		else:
			cli.display("        SHORT TERM MEMORY CACHE 9 [ WARN ]")

def srt_01(): # Check if memory systems are intact
	cli.display("[KE5:SRT:01] Running subroutine 1 ...")
	out = ShorttermMemorySystemStatus()
	cli.display("[KE5:SRT:01] Subroutine finished.")
	return out

def srt_02(): # Reset short-term memory caches
	cli.display("[KE5:SRT:02] Running subroutine 2 ...")
	for x in range(10):
		with open(__file__[:-13] + "memory/longterm/memory_cache_" + str(x) + ".ke5", "w") as f:
			f.write("KE5LTMC" + str(x))
	cli.display("[KE5:SRT:02] Subroutine finished.")
