input = open('./inputs/5_input.txt','r')
strings = input.read().split('\n')
strings.pop()
IDs = []

for line in strings:
        row_l = 0
        row_u = 127
        col_l = 0
        col_u = 7
        row = 0
        col = 0

        for idx in range(0,7):
                if idx == 6:
                        if line[idx] == 'F':
                                row = row_l
                        else:
                                row = row_u
                elif line[idx] == 'F':
                        row_u = (row_u + row_l)// 2
                elif line[idx] == 'B':
                        row_l = -(-(row_u + row_l) // 2)
        for idx in range(7,10):
                if idx == 9:
                        if line[idx] == 'L':
                                col = col_l
                        else:
                                col = col_u
                elif line[idx] == 'L':
                        col_u = (col_u + col_l) // 2
                elif line[idx] == 'R':
                        col_l = -(-(col_u + col_l) // 2)

        IDs.append((row * 8) + col)

IDs.sort()

for idx in range(1, len(IDs)):
        if IDs[idx - 1] != (IDs[idx] - 1):
                print("Seat ID: " + str(IDs[idx] - 1))
                break
        elif IDs[idx + 1] != (IDs[idx] + 1):
                print("Seat ID: " + str(IDs[idx] + 1))
                break
