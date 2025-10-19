from colorama import Fore


def get_cats_info(path):
    cats = []
    # try to open the file
    try:
        with open(path, "r", encoding="utf-8") as file:
            # iterate lines starting from index=1
            for idx, line in enumerate(file, 1):
                text = line.strip()
                if not text:
                    continue
                parts = text.split(",")
                # check if the line has at least 3 values
                if len(parts) < 3:
                    print(Fore.RED + "[ERROR] " + Fore.RESET + f"Wrong line #{idx}: {text}")
                    continue
                cat = {
                    "id": parts[0],
                    "name": parts[1],
                    "age": parts[2]
                }
                cats.append(cat)
    except (FileNotFoundError, UnicodeDecodeError):
        print(Fore.RED + "[ERROR] " + Fore.RESET + f"File not found or corrupted: {path}")
        return []
    
    return cats


cats_info = get_cats_info("task_2/cats.txt")
print(cats_info)

