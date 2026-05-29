# CHECK SCRIPT
if __name__ == '__main__':
    # MODULES TO INSTALL

    modules = ['pytilsx']

    from importlib import import_module

    # INSTALL ALL MODULES

    for module in modules:
        import_module(module)
    
    # CREATION DIRS

    import os

    os.makedirs('Packed', exist_ok=True)
    os.makedirs('Patched', exist_ok=True)
    os.makedirs('Unpacked', exist_ok=True)