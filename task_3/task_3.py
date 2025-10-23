import sys
from pathlib import Path
from colorama import Fore

def tree(path, prefix=""):
    items = list(path.iterdir())
    count = len(items)
    #  loop in folder 
    for index, item in enumerate(items):
        connector = "└── " if index == count - 1 else "├── "
        color = Fore.BLUE if item.is_dir() else Fore.GREEN
        icon = "📂" if item.is_dir() else "📜"
        name = item.name + "/" if item.is_dir() else item.name
        print(prefix + connector + icon + color + name + Fore.RESET)
        # loop in subfolders using recursion
        if item.is_dir():
            next_prefix = "    " if index == count - 1 else "│   "
            tree(item, prefix + next_prefix)

# check if the argument is provided
if len(sys.argv) < 2:
    print(Fore.RED + "[ERROR] " + Fore.RESET + "The argument is missing.")
    sys.exit(1)  

arg_path = Path(sys.argv[1])

if not arg_path.is_absolute():
    print(Fore.RED + "[ERROR] " + Fore.RESET + "Provide an absolute path.")
    sys.exit(1)  

# checks if the directiry exists 
if not arg_path.exists():
    print(Fore.RED + "[ERROR] " + Fore.RESET + f"Path doesn't exist: {arg_path}")
    sys.exit(1)  
if not arg_path.is_dir():
    print(Fore.RED + "[ERROR] " + Fore.RESET + f"Path is not a directory: {arg_path}")
    sys.exit(1)  

#  print header from the arg_path
print("📦" + Fore.BLUE + arg_path.name + "/" + Fore.RESET)
tree(arg_path)
