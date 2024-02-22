import os
import glob
import random

current_dir = os.getcwd()

cnf_files = glob.glob(os.path.join(current_dir,'eval', "*.cnf"))

#print(cnf_files)

for cnf_file in cnf_files:
    with open(cnf_file) as f:
        lines = f.readlines()

    with open(cnf_file.replace('cnf','wcnf'), 'w') as f:
        for line in lines:
            if line.startswith('c'):  # ignore comment lines
                continue
            if line.startswith('p'):  # update 'p' line with 'p wcnf' and top weight
                num_vars = line.strip().split()[-2]
                num_clauses = line.strip().split()[-1]
                f.write(f"p wcnf {num_vars} {num_clauses} 1000\n")  # assuming 1000 as top weight for hard clauses
                continue
            prob = random.randint(1, 100)
            if prob > 75:
                weight = random.randint(1, 100)  # assuming weights are random between 1 and 100
            else:
                weight = 1000
            f.write(f"{weight} {line}")  # append weight before each clause
