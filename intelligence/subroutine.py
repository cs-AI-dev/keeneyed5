from os.path import exists as fileexists
import memory

class ShorttermMemorySystemStatus:
	def __init__(this):
		this.cache_0 = fileexists(__file__[:-13] + "/memory/shortterm/memory_cache_0.ke5") and memory.shortterm.cache_0.read().split("\n")[0] == "KE5STMC0"
		this.cache_1 = fileexists(__file__[:-13] + "/memory/shortterm/memory_cache_1.ke5") and memory.shortterm.cache_1.read().split("\n")[0] == "KE5STMC0"
		this.cache_2 = fileexists(__file__[:-13] + "/memory/shortterm/memory_cache_2.ke5") and memory.shortterm.cache_2.read().split("\n")[0] == "KE5STMC0"
		this.cache_3 = fileexists(__file__[:-13] + "/memory/shortterm/memory_cache_3.ke5") and memory.shortterm.cache_3.read().split("\n")[0] == "KE5STMC0"
		this.cache_4 = fileexists(__file__[:-13] + "/memory/shortterm/memory_cache_4.ke5") and memory.shortterm.cache_4.read().split("\n")[0] == "KE5STMC0"
		this.cache_5 = fileexists(__file__[:-13] + "/memory/shortterm/memory_cache_5.ke5") and memory.shortterm.cache_5.read().split("\n")[0] == "KE5STMC0"
		this.cache_6 = fileexists(__file__[:-13] + "/memory/shortterm/memory_cache_6.ke5") and memory.shortterm.cache_6.read().split("\n")[0] == "KE5STMC0"
		this.cache_7 = fileexists(__file__[:-13] + "/memory/shortterm/memory_cache_7.ke5") and memory.shortterm.cache_7.read().split("\n")[0] == "KE5STMC0"
		this.cache_8 = fileexists(__file__[:-13] + "/memory/shortterm/memory_cache_8.ke5") and memory.shortterm.cache_8.read().split("\n")[0] == "KE5STMC0"
		this.cache_9 = fileexists(__file__[:-13] + "/memory/shortterm/memory_cache_9.ke5") and memory.shortterm.cache_9.read().split("\n")[0] == "KE5STMC0"
		
class LongtermMemorySystemStatus:
	def __init__(this):
		this.cache_0 = fileexists(__file__[:-13] + "/memory/longterm/memory_cache_0.ke5") and memory.longterm.cache_0.read().split("\n")[0] == "KE5LTMC0"
		this.cache_1 = fileexists(__file__[:-13] + "/memory/longterm/memory_cache_0.ke5") and memory.longterm.cache_1.read().split("\n")[0] == "KE5LTMC0"
		this.cache_2 = fileexists(__file__[:-13] + "/memory/longterm/memory_cache_0.ke5") and memory.longterm.cache_2.read().split("\n")[0] == "KE5LTMC0"

class MemorySystemStatus:
	def __init__(this):
		this.shortterm = ShorttermMemorySystemStatus()
		this.longterm = LongtermMemorySystemStatus()

def srt_01():
	# Check if memory systems are intact
	return MemorySystemStatus()
