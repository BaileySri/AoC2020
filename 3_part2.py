input = open('./inputs/3_input.txt','r')
strings = input.read().split('\n')
strings.pop()

over = [1,3,5,7,1]
down = [1,1,1,1,2]

for i in range(0,len(over)):
        x = over[i]
        y = down[i]
        pos_x = 0
        trees = 0
        for index in range(y, len(strings), y):
                pos_x = (pos_x + x) % len(strings[1])

                try:
                        if strings[index][pos_x] == '#':
                                trees += 1
                except:
                        print(str(index) + " " + str(pos_x))
                        print(strings[index])
        print(trees)
