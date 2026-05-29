if __name__ == '__main__':
    modules = ['pytilsx']

    from importlib import import_module

    for module in modules:
        import_module(module)