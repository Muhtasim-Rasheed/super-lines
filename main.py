import random
import os
import time
from typing import Callable
import colorama

charlist: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;:,.<>?/`~"
wordlist: list[str] = [
  "\"", "\\", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "[", "]", "{", "}", "|", ";", ":", ",", ".", "<", ">", "?", "/", "`", "~",
  "if", "else", "elif", "for", "while", "do", "break", "continue", "return", "def", "class", "import", "from", "as", "try", "except", "finally", "raise", "assert", "pass", "global", "nonlocal", "lambda", "yield", "with", "in", "is", "and", "or", "not", "True", "False", "None",
  "int", "float", "str", "list", "tuple", "dict", "set", "bool", "complex", "range", "len", "type", "print", "input", "open", "close", "read", "write", "append", "split", "join", "strip", "replace", "find", "index", "count", "sort", "reverse", "min", "max", "sum", "abs", "pow", "round", "divmod", "zip", "enumerate", "filter", "map", "reduce", "lambda", "filter", "sorted", "reversed", "any", "all", "next", "iter", "isinstance", "issubclass", "super", "getattr", "setattr", "delattr", "hasattr", "property",
  "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]
string: str = ""

def add_char_to_string() -> None:
  global string
  length: int = random.randint(1, 25)
  string += "".join(random.choices(charlist, k=length)) + " "
  if random.random() < 0.4:
    string += "\n"

def add_word_to_string() -> None:
  global string
  string += random.choice(wordlist) + " "
  if random.random() < 0.1:
    string += "\n"

def print_string(add_mech: Callable, delay: float, color: str) -> None:
  os.system("clear")
  add_mech()
  print(string)
  # Simulate text file size increase
  filesize: float = len(string) / 1000
  print("\n" + "File size: " + '\033[4m' + str(filesize) + colorama.Style.RESET_ALL + color + " KB")
  time.sleep(delay)

def main() -> None:
  os.system("clear")
  print("""\033[1m
  :'######::'##::::'##:'########::'########:'########:::::::::::'##:::::::'####:'##::: ##:'########::'######::
  '##... ##: ##:::: ##: ##.... ##: ##.....:: ##.... ##:::::::::: ##:::::::. ##:: ###:: ##: ##.....::'##... ##
  :##:::..:: ##:::: ##: ##:::: ##: ##::::::: ##:::: ##:::::::::: ##:::::::: ##:: ####: ##: ##::::::: ##:::..::
  . ######:: ##:::: ##: ########:: ######::: ########::'#######: ##:::::::: ##:: ## ## ##: ######:::. ######::
  :..... ##: ##:::: ##: ##.....::: ##...:::: ##.. ##:::........: ##:::::::: ##:: ##. ####: ##...:::::..... ##:
  '##::: ##: ##:::: ##: ##:::::::: ##::::::: ##::. ##::::::::::: ##:::::::: ##:: ##:. ###: ##:::::::'##::: ##:
  . ######::. #######:: ##:::::::: ########: ##:::. ##:::::::::: ########:'####: ##::. ##: ########:. ######::
  :......::::.......:::..:::::::::........::..:::::..:::::::::::........::....::..::::..::........:::......:::       v1.0
  """ + colorama.Style.RESET_ALL)

  print(colorama.Fore.GREEN + "Ethical Hacking or " + colorama.Fore.RED + "\033[1m" + "Hecking" + colorama.Style.RESET_ALL + colorama.Fore.GREEN + " (1 / 2) ?")
  color: int = int(input("==> "))
  if color == 1:
    color_str: str = colorama.Fore.GREEN
  elif color == 2:
    color_str: str = colorama.Fore.RED

  print(colorama.Fore.RED + "EPELEPSY WARNING: This program gets very flashy if used for a long time." + color_str)

  print("Enter mode from options:")
  print("    1. Random characters")
  print("    2. Random words")
  mode: int = int(input("==> "))

  print("Enter delay in seconds: ")
  delay: float = float(input("==> "))

  if mode == 1:
    while 1:
      print_string(add_char_to_string, delay, color_str)
  elif mode == 2:
    while 1:
      print_string(add_word_to_string, delay, color_str)

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    print("\n\nExiting...")
