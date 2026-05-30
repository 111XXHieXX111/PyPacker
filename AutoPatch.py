# CHECK SCRIPT

if __name__ != '__main__':
    import sys
    sys.exit(0)

# CHECK INPUT FILE

import sys

if len(sys.argv) > 1:
    file_path = sys.argv[1]
else:
    sys.exit(0)

# GETTING NAME

import os

name = os.path.splitext(os.path.basename(file_path))[0]

# PACKING

import subprocess

proc = subprocess.Popen(['python', 'Packer.py', file_path], stdin=subprocess.PIPE, text=True)
proc.communicate('')

packed_file = f'Packed/{name}.packed'

# PATCHING

proc = subprocess.Popen(['python', 'Patcher.py', packed_file], stdin=subprocess.PIPE, text=True)
proc.communicate(f'{name}\n')

# DEL PACKED FILE

if os.path.exists(packed_file):
    os.remove(packed_file)