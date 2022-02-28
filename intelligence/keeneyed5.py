import os
import sys

import memory as mem
import subroutine
import commandLineInterface as cli

cli.display("[KE5:RT] Connecting subroutine driver to CLI ...")
subroutine.connectCLI(cli)
cli.display("[KE5:RT] Done.")

def acceptInput(inp):
    # Commit to short-term memory
    pass
