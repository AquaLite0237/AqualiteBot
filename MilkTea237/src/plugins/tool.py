import time
from pathlib import Path

STATIC  = str(Path(__file__).parent.parent.joinpath('static'))

def hash(qq: int):
    days = int(time.strftime("%d", time.localtime(time.time()))) + 31 * int(
        time.strftime("%m", time.localtime(time.time()))) + 77
    return (days * qq) >> 8
