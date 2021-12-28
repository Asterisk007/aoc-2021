import sys, operator, copy
from typing import List
from tqdm import tqdm

def find_match(min, max, template, formulas, occurences) -> List[str]:
    print(f"{min}, {max}")
    if min+1 > len(template):
        return []
    if min == max:
        formula_str = template[min] + template[min+1]
        if formulas[formula_str]:
            new_elem = formulas[formula_str]
            try:
                occurences[new_elem] += 1
            except KeyError:
                occurences[new_elem] = 1
        return [template[min], new_elem, template[min+1]]
    else:
        return_arr = []
        return_arr.extend(find_match(min, int(max/2), template, formulas, occurences))
        return_arr.extend(find_match(int(max/2)+1, max, template, formulas, occurences))
        return return_arr
        

if len(sys.argv) < 2:
    print("Need input file")
    quit()

f = open(sys.argv[1])
lines = f.readlines()

template = []
formula = {}
occurences = {}

for line in lines:
    line = line.rstrip()
    if line != "":
        if "->" not in line:
            template = list(line)
        else:
            recipe = line.split(" -> ")
            formula[recipe[0]] = recipe[1]

for i in template:
    try:
        occurences[i] += 1
    except KeyError:
        occurences[i] = 1

template_p1 = copy.deepcopy(template)
template_p2 = copy.deepcopy(template)

occurences_p1 = dict(occurences)
occurences_p2 = dict(occurences)

for i in range(10):
    j = 0
    while j < len(template_p1):
        #print(f"At character {template[j]}")
        if j+1 < len(template_p1):
            formula_str = template_p1[j] + template_p1[j+1]
            #print(formula_str)
            if formula[formula_str]:
                new_elem = formula[formula_str]
                template_p1.insert(j+1, new_elem)
                try:
                    occurences_p1[new_elem] += 1
                except KeyError:
                    occurences_p1[new_elem] = 1
                j += 2
            else:
                j += 1
        else:
            break;

lce_p1 = min(occurences_p1, key=occurences_p1.get)
mce_p1 = max(occurences_p1, key=occurences_p1.get)

# Part 2 needs a recursive strategy
for i in range(40):
    find_match(0, len(template_p2), template_p2, formula, occurences_p2)

            
lce_p2 = min(occurences_p2, key=occurences_p2.get)
mce_p2 = max(occurences_p2, key=occurences_p2.get)

print(f"Part 1: Most common element: {mce_p1}; Least common element: {lce_p1}")
print(occurences_p1[mce_p1]-occurences_p1[lce_p1])

print(f"\nPart 2: Most common element: {mce_p2}; Least common element: {lce_p2}")
print(occurences_p2[mce_p2]-occurences_p2[lce_p2])
