input = open('./inputs/1_input.txt','r')
strings = input.read().split('\n')
strings.pop()

for a in strings:
        for b in strings:
                if a == b:
                        continue
                elif int(a) + int(b) == 2020:
                        print(a + ", " + b)
                        print(int(a) * int(b))
