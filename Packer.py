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

import pytilsx
import os
import lzma

results = []

# TIMER

timer = pytilsx.Timer()
timer.start()

# READ FILE

filename = os.path.basename(file_path)
name_without_ext = os.path.splitext(filename)[0]
with open(file_path, 'r') as f:
    data = f.read()

timer.end()
results.append(timer.get())
timer.reset()

timer.start()

# ENCODE FILE

import base64

encoded_data = base64.b64encode(bytes(data, encoding='utf-8'))

# COMPRESS FILE

compressed_data = lzma.compress(encoded_data, preset=9)
with open('Packed/'+name_without_ext+'.packed', 'wb+') as f:
    f.write(compressed_data)

# STOP TIMER

timer.end()
results.append(timer.get())

# RESULTS

print('='*50)
print(f'Reading time:{results[0]} sec')
print('-'*50)
print(f'Compressing time:{results[1]} sec')
print('-'*50)
print(f'Size:{len(compressed_data)} bytes')
print('='*50)
input('\n')