# CHECK SCRIPT

if __name__ != '__main__':
    import sys
    sys.exit(0)

import lzma

# DONT TOUCH THIS CODE LINE:

data = """Patch"""

# DECOMPRESS DATA

dedata = lzma.decompress(data)

# SHOW WATERMARK

def showlbl():
    print('='*50)
    print('STARTED WITH CODE RUNNER!')
    print('VERSION 0.0.1')
    print('BY XXHIEXX')
    print(f'SIZE:{len(data)} BYTES')
    print('='*50)

showlbl()

import os

# CLEAN TERMINAL

if sys.platform.startswith('win'):
    os.system('cls')
else:
    os.system('clear')

# RUN PROCESS

def thproc():
    compiled = compile(dedata, '<string>', 'exec')
    exec(compiled, globals())

import threading

t = threading.Thread(target=thproc)
t.start()
t.join()