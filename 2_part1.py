input = open('./inputs/2_input.txt','r')
strings = input.read().split('\n')
strings.pop()
valid = 0

for entry in strings:
    parts = entry.split(' ')
    times = parts[0].split('-')
    req_letter = (parts[1])[0]
    count = 0
    for i in parts[2]:
        if i == req_letter:
            count = count + 1
    if count <= int(times[1]) and count >= int(times[0]):
        valid = valid + 1

print(valid)
