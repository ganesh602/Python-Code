import re

def find_start_end_indices(s, substring):
    pattern = re.compile(f'(?=({re.escape(substring)}))')
    matches = pattern.finditer(s)
    flag = False
    for match in matches:
        flag = True
        start_index = match.start(1)
        end_index = match.end(1) - 1
        print(f'({start_index}, {end_index})')
    if flag == False:
        print(f'({-1}, {-1})')

if __name__ == '__main__':
    s = input()
    substring = input()
    
    find_start_end_indices(s, substring)