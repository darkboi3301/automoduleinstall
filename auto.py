module="module name"
try:
    importlib.import_module(module)
except ImportError:
    import pip
    print(module," not found installing ... ")
    pip.main(['install',module])
finally:
    importlib.import_module(module)
