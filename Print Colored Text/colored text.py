import colorama
from colorama import Fore, Back, Style

# Initialize colorama with autoreset enabled
colorama.init(autoreset=True)

# Print a line with blue text on a yellow background
print(Fore.BLUE + Back.YELLOW + "Hi My name is Prachit Pandit" + Fore.YELLOW + Back.BLUE + " I'm a Software Developer")

# Print a line with cyan text on a magenta background
print(Back.CYAN + "Hi My name is Rohan Das" + Back.MAGENTA + " I'm a Full Stack Developer")

# Print a line with red text on a green background
print(Fore.RED + Back.GREEN + "Hi My name is Aashish Kumar" + Fore.GREEN + Back.RED + " I'm a.NET Developer")
