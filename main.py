#Firts calculator
import numexpr
from colorama import init
from colorama import Fore, Back, Style
init()

print(Fore.RED)

expr = input("введите математическое выражение")
result = numexpr.evaluate(expr)

print(f"Результат {result}")