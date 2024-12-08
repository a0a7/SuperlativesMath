import csv
import re
from collections import defaultdict
import math

def clean_and_split_names(cell):
    if not cell.strip():
        return []
    names = [name.lower() for name in cell.split('+')]
    return [name for name in names if name] 

def calculate_prep_contributions(file_path):
    contributions = defaultdict(float)
    
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for cell in row:
                names = clean_and_split_names(cell)
                if names:
                    contribution = 1 / len(names) 
                    for name in names:
                        contributions[name] += contribution
    
    rounded_contributions = {name: math.ceil(total) for name, total in contributions.items()}
    sorted_contributions = sorted(rounded_contributions.items(), key=lambda x: x[1], reverse=True)
    return sorted_contributions

file_path = 'prep.csv'

contributions = calculate_prep_contributions(file_path)
print("Contributions sorted by total prep:")
for name, total in contributions:
    print(f"{name}: {total:.0f}")