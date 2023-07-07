#!/usr/bin/env python3
'''Task 3's module.
'''


def to_str(n: float) -> str:
    '''Converts a floating-point number to a string.
    '''
    return str(n)

if __name__ == '__main__':
    print(f'to_str(3.142)')
    print(to_str(0.00))

    print(to_str.__annotations__)
