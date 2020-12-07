input = open('./inputs/3_input.txt','r')
strings = input.read().split('\n')
strings.pop()

over = int(3)
down = int(1)

pos_x = int(0)
trees = int(0)

for index in range(down, len(strings), down):
        pos_x = (pos_x + over) % len(strings[1])

        try:
                if strings[index][pos_x] == '#':
                        trees += 1
        except:
                print(str(index) + " " + str(pos_x))
                print(strings[index])

print(trees)
