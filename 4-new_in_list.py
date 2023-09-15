#!/usr/bin/python3
import py_compile
import importlib

if __name__ == "__main__":
    py_compile.compile("hidden_4.pyc")  # Compile the module if not already compiled
    module = importlib.import_module("hidden_4")
    
    names = [name for name in dir(module) if not name.startswith('__')]
    
    for name in sorted(names):
        print(name)

