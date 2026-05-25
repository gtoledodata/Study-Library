import re

patient_info = input("Enter patient's name and birth year (e.g., John Doe, 1980): ")
    
answer = r'(\w+) (\w+), (\d{4})'

result = re.search(answer, patient_info)
while True:
    if result:
        first_name = result.group(1)
        last_name = result.group(2)
        birth_year = result.group(3)
        print(f"Patient's Name: {first_name} {last_name}, Birth Year: {birth_year}")
        break
    else:
        print("Invalid input format. Please enter in the format: Name, Birth Year (e.g., John Doe, 1980).")
        patient_info = input("Enter patient's name and birth year (e.g., John Doe, 1980): ")

