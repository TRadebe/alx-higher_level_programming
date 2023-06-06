#!/usr/bin/python3

output = ""

for c in range(ord('z'), ord('a') - 1, -1):
    output += "{}".format(chr(c - (32 if c % 64 < 32 else 0)))

print(output, end="")
