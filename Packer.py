if __name__ != '__main__':
    import sys
    sys.exit(0)

import sys

if len(sys.argv) > 1:
    file_path = sys.argv[1]
else:
    sys.exit(0)

import pytilsx
import os
import lzma

results = []

timer = pytilsx.Timer()
timer.start()

filename = os.path.basename(file_path)
name_without_ext = os.path.splitext(filename)[0]
with open(file_path, 'r') as f:
    data = f.read()

timer.end()
results.append(timer.get())
timer.reset()

timer.start()

compressed_data = lzma.compress(bytes(data, encoding='utf-8'), preset=9)
with open('Packed/'+name_without_ext+'.packed', 'wb+') as f:
    f.write(compressed_data)

timer.end()
results.append(timer.get())

print('='*50)
print(f'Reading time:{results[0]} sec')
print('-'*50)
print(f'Compressing time:{results[1]} sec')
print('-'*50)
print(f'Size:{len(compressed_data)} bytes')
print('='*50)
input('\n')