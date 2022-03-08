import os
import datetime
import re
import subroutine

cli = subroutine.cli

memory_strength = 20

breaksentinel = "[BKE5MC]"
splitsentinel = "[MKE5MCBS]"

class InvalidMemoryCache(Exception): pass

def parseMemoryCache(num):
    if num > 9 or num < 0:
        raise InvalidMemoryCache

class remember:
    def longterm(day, month, year, *terms):
        out = []
        for filename in os.listdir(__file__[:-3] + "/longterm/"):
            fdir = os.path.join(__file__[:-3] + "/memory/longterm/", filename)
            if os.path.isfile(fdir):
                if [int(x) for x in filename.split("_")][0] != str(day) or [int(x) for x in filename.split("_")][1] != str(month) or [int(x) for x in filename.split("_")][2] != str(year):
                    continue
                with open(fdir, "r") as f:
					for x in terms:
						if x in f.read().split(""):
                    		out.append(f.read())
						else:
							pass
        return out

    def shortterm(*terms):
        out = []
        for filename in os.listdir(__file__[:-3] + "/shortterm/"):
            fdir = os.path.join(__file__[:-3] + "/memory/shortterm", filename)
            if os.path.isfile(fdir):
                with open(fdir, "r") as f:
                    for data in f.read().split(breaksentinel):
                        for datum in data.split(splitsentinel):
                            if datum in terms:
                                out.append(data)
        return out

class record:
    def longterm(day, month, year, *data):
		cli.display("[KE5:REC:LONG] Recording data to long-term memory ...")
        with open(__file__[:-3] + "/longterm/" + "d" + str(day) + "m" + str(month) + "y" + str(year), "a") as f:
            for datum in data:
				cli.display("    Posting " + str(datum) + " ...")
                f.write("\n" + breaksentinel + datum)
		cli.display("[KE5:REC:LONG] Done.")
        return True

    def shortterm(*data):
		cli.display("[KE5:REC:SHORT] Recording data to short-term memory.")
		cli.display("    Checking short-term memory subsystem status ...")
        # Check memory status
		memstat = subroutine.srt_01()
		for x in memstat.all:
			if not x:
				cli.display(cli.term.yellow_on_black("    Error detected in short-term memory subsystem. Resetting ..."))
				subroutine.srt_02()
				cli.display("    Restarting ...")
				memstat = subroutine.srt_01()
				for x in memstat.all:
					if not x:
						cli.display(cli.term.red_on_black("    Continuous error detected in short-term memory subsystem. User intervention required."))
						return 0
		cli.display(term.lime_on_black("    Check complete, subsystem status is good."))
		cli.display("    Recording data ...")
        
		cli.display("        Getting smallest short-term memory cache ...")
        sizes = [os.path.getsize(__file__[:-3] + "/shortterm/memory_cache_" + str(x)) for x in range(10)]
        cachenum = str(min(sizes))
		cli.display("        " + cli.term.lime_on_black("Done") + ", memory cache number is " + str(cachenum) + ".")

		cli.display("        Posting data to cache ...")
        with open(__file__[:-3] + "/shortterm/memory_cache_" + cachenum, "a") as f:
            for datum in data:
                f.write("\n" + breaksentinel + datum)
		cli.display(cli.term.lime_on_black("        Data posted."))

		cli.display("        Checking for memory drilling ...")
        count = 0
        for alreadyCached in remember.shortterm(*data):
            if alreadyCached in data:
                count += 1
				
		cli.display("            Related data count: " + str(count))

        if count >= 100 - memory_strength:
			cli.display("        Drilling data ...")
            record.longterm(datetime.datetime.today().day, datetime.datetime.today().month, datetime.datetime.today().year, data)
			cli.display(cli.term.lime_on_black("        Done."))
		cli.display("[KE5:REC:SHORT] Done.")

class longterm:
    def record(day, month, year, *data):
        with open(__file__[:-3] + "/longterm/" + "d" + str(day) + "m" + str(month) + "y" + str(year), "a" + ".ke5") as f:
            for datum in data:
                f.write("\n" + breaksentinel + datum)
        return True

    def remember(day, month, year, *terms):
        out = []
        for filename in os.listdir(__file__[:-3] + "/longterm/"):
            fdir = os.path.join(__file__[:-3] + "/memory/longterm/", filename)
            if os.path.isfile(fdir):
                if [int(x) for x in filename.split("_")][0] != str(day) or [int(x) for x in filename.split("_")][1] != str(month) or [int(x) for x in filename.split("_")][2] != str(year):
                    continue
                with open(fdir, "r") as f:
					for x in terms:
						if x in f.read().split(""):
                    		out.append(f.read())
						else:
							pass
        return out

class shortterm:
    def record(*data):
        sizes = [os.path.getsize(__file__[:-3] + "/shortterm/memory_cache_" + str(x)) for x in range(10)]
        cachenum = str(min(sizes))

        with open(__file__[:-3] + "/shortterm/memory_cache_" + cachenum, "a") as f:
            for datum in data:
                f.write("\n" + breaksentinel + datum)

        count = 0
        for alreadyCached in remember.shortterm(*data):
            if alreadyCached in data:
                count += 1

        if count >= 100 - memory_strength:
            record.longterm(datetime.datetime.today().day, datetime.datetime.today().month, datetime.datetime.today().year, data)

    def remember(*terms):
        out = []
        for filename in os.listdir(__file__[:-3] + "/shortterm/"):
            fdir = os.path.join(__file__[:-3] + "/memory/shortterm", filename)
            if os.path.isfile(fdir):
                with open(fdir, "r") as f:
                    for data in f.read().split(breaksentinel)[1:]:
                        for datum in data.split(splitsentinel):
                            if datum in terms:
                                out.append(data)
        return out
