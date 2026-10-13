import sys

print("=== Python 3 demo ===")
print("Версія:", sys.version)

# print тепер функція з дужками
print("1. print: обов'язкові круглі дужки")

# Звичайне ділення повертає float
a = 5 / 2
print("2. 5 / 2 =", a, "(а для цілого використовуємо //:", 5 // 2, ")")

# Рядок це завжди юнікод, а для байтів є bytes
s = "привіт"
b = b"hello"
print("3. тип рядка:", type(s), "тип байтів:", type(b))

# range тепер окремий тип (як старий xrange), xrange прибрали
print("4. range:", type(range(3)))

# raw_input прибрали, лишився тільки input()
print("5. тільки input(), який повертає str")

# Винятки перехоплюються через 'as'
try:
    x = 10 / 0
except ZeroDivisionError as err:
    print("6. помилка через as:", err)

# keys() повертає view (dict_keys), а не готовий список
d = {"a": 1, "b": 2}
print("7. d.keys():", type(d.keys()))

# long прибрали, все тепер int
num = 999999999999999999999999999999999
print("8. тип великого числа:", type(num))

# Не можна порівнювати різні типи, кидає TypeError
try:
    print(1 < "2")
except TypeError as err:
    print("9. 1 < '2' викликає помилку:", type(err).__name__)

# Замість .next() використовується функція next()
it = iter([10, 20, 30])
print("10. ітератор:", next(it))