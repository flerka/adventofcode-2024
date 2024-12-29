def solve():
    locks, keys = read_input("day25.txt")
    pairs_count = 0

    for lock in locks: 
        for key in keys:
            is_valid_combo = True
            for c in range(5):
                if key[c] > (5 - lock[c]):
                    is_valid_combo = False
                    
            if is_valid_combo:       
                pairs_count += 1

    return pairs_count

def read_input(filename):
    with open(filename, 'r') as file:
        data = file.read()
    
    locks = []
    keys = []
    blocks = data.split('\n\n')
    for block in blocks:
        lines = block.strip().split('\n')
        processed_data = process_block(lines)
        if is_lock(lines):
            locks.append(processed_data)
        else:
            keys.append(processed_data)

    return locks, keys

def process_block(lines):
    result = [0, 0, 0, 0, 0]
    for line_i in range(1, 6):
        for char_i in range(0, 5):
            if lines[line_i][char_i] == '#':
                result[char_i] += 1

    return result

def is_lock(lines):
    return lines[0] == "#####"

result = solve()
print(result)