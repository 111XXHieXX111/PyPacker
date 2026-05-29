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

# READING FILE

filename = os.path.basename(file_path)
name_without_ext = os.path.splitext(filename)[0]
with open(file_path, 'rb') as f:
    data = f.read()

timer.end()
results.append(timer.get())
timer.reset()

timer.start()

# DECOMPRESS FILE

decompressed_data = lzma.decompress(data)

# DECODED FILE

import base64

decoded_data = base64.b64decode(decompressed_data).decode()

# SAVE FILE

with open('Unpacked/'  + name_without_ext + '.py', 'w+') as f:
    f.write(decoded_data)

timer.end()
results.append(timer.get())

# RESULTS

print('='*50)
print(f'Reading time:{results[0]}sec')
print('-'*50)
print(f'Compressing time:{results[1]}sec')
print('-'*50)
print(f'Bytes:{len(decompressed_data)}')
print('='*50)
input('\n')