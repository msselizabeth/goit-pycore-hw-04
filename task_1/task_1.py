from colorama import Fore


def total_salary(path):
    total = 0
    avg = 0
    valid_count = 0
    
    # try to open the file
    try:
        with open(path, "r", encoding="utf-8") as file:
            # iterate lines starting from index=1
            for idx, line in enumerate(file, 1):
                text = line.strip()
                if not text:
                    continue
                
                parts = text.split(",")
                # check if the line has at least 2 values
                if len(parts) < 2:
                    print(Fore.RED + "[ERROR] " + Fore.RESET + f"Wrong line #{idx}: {text}")
                    continue
                
                # try to convert salary value to integer
                try:
                    salary = int(parts[1])
                except ValueError:
                    print( Fore.RED + "[ERROR] " + Fore.RESET + f"The value {parts[1]} cannot be converted to integer(line #{idx}).")
                    continue
                
                # calc total salary + add count valid value
                total += salary
                valid_count += 1
            
    except (FileNotFoundError, UnicodeDecodeError):
        print(Fore.RED + "[ERROR] " + Fore.RESET + f"File not found or corrupted: {path}")
        return (0, 0)

    # calc average salary
    avg = total // valid_count if valid_count else 0
    return (total, avg)


total, average = total_salary("task_1/employees.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

