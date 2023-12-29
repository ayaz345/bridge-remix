import sys
import os

if len(sys.argv) != 2:
    print("ERROR: Must provide one and only one envvar name to get_env.py", sys.stderr)
    os._exit(0)
envvar = sys.argv[1]
if envvar in os.environ:
    val = os.environ[envvar]
    print(val)
os._exit(0)