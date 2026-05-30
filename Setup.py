# CHECK SCRIPT
if __name__ == '__main__':
    # MODULES TO INSTALL

    modules = ['pytilsx']

    # INSTALL ALL MODULES

    import subprocess
    import sys
    
    for module in modules:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', module])
    
    # CREATION DIRS

    import os

    os.makedirs('Packed', exist_ok=True)
    os.makedirs('Patched', exist_ok=True)
    os.makedirs('Unpacked', exist_ok=True)