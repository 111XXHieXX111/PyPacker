# CHECK SCRIPT

if __name__ != '__main__':
    import sys
    sys.exit()

import sys

# CHECK INPUT FILE

if len(sys.argv) > 1:
    file_path = sys.argv[1]
else:
    sys.exit(0)

#GET PROJECT NAME

name = input('ProjectName:')

#READING TOOL FOR CREATION

with open('Tools/Runner.py', 'r') as f:
    runnercode = f.read()

#REFACTORING

new = '#Using patcher'
for line in runnercode.split('\n'):
    if line == 'data = """Patch"""':
        with open(file_path, 'rb') as f:
            data = f.read()
        new += f'\ndata = {data}'
    else:
        new += f'\n{line}'

#SAVING

with open('Patched/'+name+'.py', 'w+') as f:
    f.write(new)