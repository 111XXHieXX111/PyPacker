import sys
import os
import subprocess

if len(sys.argv) > 1:
    file_path = sys.argv[1]
else:
    sys.exit(0)

name = os.path.splitext(os.path.basename(file_path))[0]

proc = subprocess.Popen(['python', 'Packer.py', file_path], stdin=subprocess.PIPE, text=True)
proc.communicate('')

packed_file = f'Packed/{name}.packed'

proc = subprocess.Popen(['python', 'Patcher.py', packed_file], stdin=subprocess.PIPE, text=True)
proc.communicate(f'{name}\n')

if os.path.exists(packed_file):
    os.remove(packed_file)