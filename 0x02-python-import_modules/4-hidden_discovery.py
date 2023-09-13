#!/usr/bin/python3
import dis

if __name__ == "__main__":
    module_code = __import__("hidden_4").__doc__
    names = [name for name in dir(module_code) if not name.startswith('__')]

    for name in sorted(names):
        print(name)

