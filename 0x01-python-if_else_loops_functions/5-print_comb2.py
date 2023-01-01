#!/usr/bin/python3
for num in range(100):
    if num == 99:
        print(F"{num}", end="")
        continue
    print(F"{num:02d}", end=", ")
