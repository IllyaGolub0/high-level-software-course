import sys

print("Python version:", sys.version)

# 1. Цілочисельний та звичайний поділ
print("5 / 2 =", 5 / 2)       # завжди float починаючи з Python 3.x
print("5 // 2 =", 5 // 2)     # цілочисельний поділ

# 2. F-string (з'явилися з Python 3.6, а виклики методів у {} — з 3.8)
name = "World"
print(f"Hello, {name}!")
print(f"Hello in uppercase: {name.upper()}")

# 3. Новий синтаксис match-case (працює тільки з 3.10+)
try:
    match 3:
        case 1:
            print("Matched 1")
        case 3:
            print("Matched 3")
        case _:
            print("Default")
except SyntaxError:
    print("match-case not supported in this Python version")

