

from typing import Union

def process_value(value: Union[int,float, str,bool]):
    if isinstance(value, int):
        print(f"Integer: {value}")
    elif isinstance(value, float):
        print(f"Floating: {value}")
    elif isinstance(value, str):
        print(f"String: {value}")
    else:
        print(f"Boolen: {value}")

# Using union
process_value(10)   # Integer
process_value(25.9)     #float 
process_value("Hello")  # String
process_value(True)      # boolean