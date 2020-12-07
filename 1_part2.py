input = open('./inputs/1_input.txt','r')
strings = input.read().split('\n')
strings.pop()

for a in strings:
        for b in strings:
                for c in strings: 
                        if a == b:
                                continue
                        if a == c:
                                continue
                        if b == c:
                                continue
                        elif int(a) + int(b) + int(c) == 2020:
                                print(a + ", " + b + ", " + c)
                                print(int(a) * int(b) * int(c))
