import os
import datetime

memory_strength = 20

breaksentinel = "[BKE5MC]"
splitsentinel = "[MKE5MCBS]"

class InvalidMemoryCache(Exception): pass

def parseMemoryCache(num):
    if num > 9 or num < 0:
        raise InvalidMemoryCache

class remember:
    def longterm(day, month, year):
        out = []
        for filename in os.listdir(__file__[:-3] + "/longterm/"):
            fdir = os.path.join(__file__[:-3] + "/memory/longterm/", filename)
            if os.path.isfile(fdir):
                if [int(x) for x in filename.split("_")][0] != str(day) or [int(x) for x in filename.split("_")][1] != str(month) or [int(x) for x in filename.split("_")][2] != str(year):
                    continue
                with open(fdir, "r") as f:
                    out.append(f.read())
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
        with open(__file__[:-3] + "/longterm/" + "d" + str(day) + "m" + str(month) + "y" + str(year), "a") as f:
            for datum in data:
                f.write("\n" + breaksentinel + datum)
        return True

    def shortterm(*data):
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

class longterm:
    def record(day, month, year, *data):
        with open(__file__[:-3] + "/longterm/" + "d" + str(day) + "m" + str(month) + "y" + str(year), "a") as f:
            for datum in data:
                f.write("\n" + breaksentinel + datum)
        return True

    def remember(day, month, year):
        out = []
        for filename in os.listdir(__file__[:-3] + "/longterm/"):
            fdir = os.path.join(__file__[:-3] + "/memory/longterm", filename)
            if os.path.isfile(fdir):
                with open(fdir, "r") as f:
                    for data in f.read().split(breaksentinel)[1:]:
                        for datum in data.split(splitsentinel):
                            if datum in terms:
                                out.append((, data))
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
