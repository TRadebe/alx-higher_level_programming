#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        vis = a / b
    except (TypeError, ZeroDivisionError):
        vis = None
    finally:
        print('Inside result: {}'.format(vis))
    return vis
