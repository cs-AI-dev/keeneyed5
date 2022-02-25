from os.path import exists as fileexists
import memory
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

cli = None
def connectToCLI(package):
	global cli

	cli = package

class ShorttermMemorySystemStatus:
	def __init__(this):
		cli.display("    Assembling short-term memory statuses ...")
		this.cache_0 = fileexists(__file__[:-13] + "/memory/shortterm/memory_cache_0.ke5") and memory.shortterm.cache_0.read().split("\n")[0] == "KE5STMC0"
		if this.cache_0:
			cli.display("        SHORT TERM MEMORY CACHE 0 [  OK  ]")
		else:
			cli.display(".       SHORT TERM MEMORY CACHE 0 [ WARN ]")
		
		
		this.cache_1 = fileexists(__file__[:-13] + "/memory/shortterm/memory_cache_1.ke5") and memory.shortterm.cache_1.read().split("\n")[0] == "KE5STMC0"
		if this.cache_1:
			cli.display("        SHORT TERM MEMORY CACHE 1 [  OK  ]")
		else:
			cli.display(".       SHORT TERM MEMORY CACHE 1 [ WARN ]")
		
		this.cache_2 = fileexists(__file__[:-13] + "/memory/shortterm/memory_cache_2.ke5") and memory.shortterm.cache_2.read().split("\n")[0] == "KE5STMC0"
		if this.cache_2:
			cli.display("        SHORT TERM MEMORY CACHE 2 [  OK  ]")
		else:
			cli.display(".       SHORT TERM MEMORY CACHE 2 [ WARN ]")
		
		this.cache_3 = fileexists(__file__[:-13] + "/memory/shortterm/memory_cache_3.ke5") and memory.shortterm.cache_3.read().split("\n")[0] == "KE5STMC0"
		if this.cache_3:
			cli.display("        SHORT TERM MEMORY CACHE 3 [  OK  ]")
		else:
			cli.display("        SHORT TERM MEMORY CACHE 3 [ WARN ]")
		
		this.cache_4 = fileexists(__file__[:-13] + "/memory/shortterm/memory_cache_4.ke5") and memory.shortterm.cache_4.read().split("\n")[0] == "KE5STMC0"
		if this.cache_4:
			cli.display("        SHORT TERM MEMORY CACHE 4 [  OK  ]")
		else:
			cli.display("        SHORT TERM MEMORY CACHE 4 [ WARN ]")
		
		this.cache_5 = fileexists(__file__[:-13] + "/memory/shortterm/memory_cache_5.ke5") and memory.shortterm.cache_5.read().split("\n")[0] == "KE5STMC0"
		if this.cache_5:
			cli.display("        SHORT TERM MEMORY CACHE 5 [  OK  ]")
		else:
			cli.display("        SHORT TERM MEMORY CACHE 5 [ WARN ]")
		
		this.cache_6 = fileexists(__file__[:-13] + "/memory/shortterm/memory_cache_6.ke5") and memory.shortterm.cache_6.read().split("\n")[0] == "KE5STMC0"
		if this.cache_6:
			cli.display("        SHORT TERM MEMORY CACHE 6 [  OK  ]")
		else:
			cli.display("        SHORT TERM MEMORY CACHE 6 [ WARN ]")
		
		this.cache_7 = fileexists(__file__[:-13] + "/memory/shortterm/memory_cache_7.ke5") and memory.shortterm.cache_7.read().split("\n")[0] == "KE5STMC0"
		if this.cache_7:
			cli.display("        SHORT TERM MEMORY CACHE 7 [  OK  ]")
		else:
			cli.display("        SHORT TERM MEMORY CACHE 7 [ WARN ]")
			
		this.cache_8 = fileexists(__file__[:-13] + "/memory/shortterm/memory_cache_8.ke5") and memory.shortterm.cache_8.read().split("\n")[0] == "KE5STMC0"
		if this.cache_8:
			cli.display("        SHORT TERM MEMORY CACHE 8 [  OK  ]")
		else:
			cli.display("        SHORT TERM MEMORY CACHE 8 [ WARN ]")
		
		this.cache_9 = fileexists(__file__[:-13] + "/memory/shortterm/memory_cache_9.ke5") and memory.shortterm.cache_9.read().split("\n")[0] == "KE5STMC0"
		if this.cache_9:
			cli.display("        SHORT TERM MEMORY CACHE 9 [  OK  ]")
		else:
			cli.display("        SHORT TERM MEMORY CACHE 9 [ WARN ]")
		
class LongtermMemorySystemStatus:
	def __init__(this):
		this.cache_0 = fileexists(__file__[:-13] + "/memory/longterm/memory_cache_0.ke5") and memory.longterm.cache_0.read().split("\n")[0] == "KE5LTMC0"
		if this.cache_0:
			cli.display("        LONG TERM MEMORY CACHE 0  [  OK  ]")
		else:
			cli.display("        LONG TERM MEMORY CACHE 0  [ WARN ]")
		
		this.cache_1 = fileexists(__file__[:-13] + "/memory/longterm/memory_cache_0.ke5") and memory.longterm.cache_1.read().split("\n")[0] == "KE5LTMC0"
		if this.cache_1:
			cli.display("        LONG TERM MEMORY CACHE 1  [  OK  ]")
		else:
			cli.display("        LONG TERM MEMORY CACHE 1  [ WARN ]")
		
		this.cache_2 = fileexists(__file__[:-13] + "/memory/longterm/memory_cache_0.ke5") and memory.longterm.cache_2.read().split("\n")[0] == "KE5LTMC0"
		if this.cache_2:
			cli.display("        LONG TERM MEMORY CACHE 2  [  OK  ]")
		else:
			cli.display("        LONG TERM MEMORY CACHE 2  [ WARN ]")
		
class MemorySystemStatus:
	def __init__(this):
		this.shortterm = ShorttermMemorySystemStatus()
		this.longterm = LongtermMemorySystemStatus()

def srt_01(): # Check if memory systems are intact
	cli.display("[KE5:SRT:01] Running subroutine 1 ...")
	out = MemorySystemStatus()
	cli.display("[KE5:SRT:01] Subroutine finished.")
	return out
	
def srt_02(cachenum, data, delimiter=";"): # Send data to short-term memory cache
	with open(__file__[:-13] + "/memory/shortterm/memory_cache_" + str(cachenum) + ".ke5", "a") as mc:
		cli.display("[KE5:SRT:02] Running subroutine 2 ...")
		cli.display("    Preparing data for caching ...")
		senddata = data.split(delimiter)
		cli.display("    Done.")
		cli.display("    Sending data to cache ...")
		for x in senddata:
			cli.display("        Sending " + x + " ...")
			mc.append("\n" + x)
		cli.display("    Done.")
	cli.display("[KE5:SRT:02] Subroutine finished.")
	return data

def srt_03(cachenum, data, delimiter=";"):
	with open(__file__[:-13] + "/memory/longterm/memory_cache_" + str(cachenum) + ".ke5", "a") as mc:
		cli.display("[KE5:SRT:03] Running subroutine 3 ...")
		cli.display("    Preparing data for caching ...")
		cli.display("        Cutting up data ...")
		senddata = data.split(delimiter)
	cli.display("[KE5:SRT:03] Subroutine finished.")
