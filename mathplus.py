import math

pi = math.pi


def to_bin(n):
    try:
        return bin(int(n))
    except Exception:
        return "Error: not a valid integer"

def to_hex(n):
    try:
        return hex(int(n)).upper()
    except Exception:
        return "Error: not a valid integer"

def square(n):
    return float(n) * float(n)


def sqrt(n):
    return math.sqrt(float(n))
