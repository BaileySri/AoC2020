input = open('./inputs/2_input.txt','r')
strings = input.read().split('\n')
strings.pop()
valid = 0

for entry in strings:
    parts = entry.split(' ')
    pos = parts[0].split('-')
    req_letter = (parts[1])[0]
    target = parts[2]
    match = False

    if target[int(pos[0])-1] == req_letter:
        match = not match

    if target[int(pos[1])-1] == req_letter:
        match = not match

    if match:
        valid = valid + 1

print(valid)
