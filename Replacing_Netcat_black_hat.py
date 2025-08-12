#for when you are alredy in the server
import argparse
import socket
import threading
import shlex
import subprocess
import sys
import textwrap

def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_outpur(shlex.split(cmd),
                                 stderr=subprocess.STDOUT)
    return output.decode()
