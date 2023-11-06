import colorama
import inspect

ккprint(inspect.getdoc(colorama))
attributes = dir(colorama)
print("Атрибути бібліотеки Colorama:")
for attr in attributes:
    print(attr)
classes_and_functions = inspect.getmembers(colorama, inspect.isclass or inspect.isfunction)
print("Класи та функції в бібліотеці Colorama:")
for name, member in classes_and_functions:
    print(name, ":", member)
