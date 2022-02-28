import os
import datetime

class InvalidMemoryCache(Exception): pass

def parseMemoryCache(num):
    if num > 9 or num < 0:
        raise InvalidMemoryCache

class remember:
    def longterm(day, year, month):
        returnedMemories = []
        for filename in os.listdir(__file__[:-3] + "/longterm/"):
            fdir = os.path.join(__file__[:-3] + "/memory/longterm/", filename)
            if os.path.isfile(fdir):
                if [int(x) for x in filename.split("_")][0] != day or [int(x) for x in filename.split("_")][1] != month or [int(x) for x in filename.split("_")][2] != year:
                    continue
                with open(fdir, "r") as f:
                    returnedMemories.append(f.read())
        return returnedMemories

    def shortterm(*terms):
        for filename in os.listdir(__file__[:-3] + "/shortterm/"):
            fdir = os.path.join(__file__[:-3] + "/memory/shortterm", filename)
            if os.path.isfile(fdir):
                pass

class postto
