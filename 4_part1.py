import re

regex = {'byr':re.compile('byr:'),
         'iyr':re.compile('iyr:'),
         'eyr':re.compile('eyr:'),
         'hgt':re.compile('hgt:'),
         'hcl':re.compile('hcl:'),
         'ecl':re.compile('ecl:'),
         'pid':re.compile('pid:')
         #'cid':re.compile('cid:') Unused
        }


input = open('./inputs/4_input.txt','r')
strings = input.read().split('\n\n')

valid = int(0)

for line in strings:
        count = int(0)
        for reg in regex.values():
                if reg.search(line):
                        count = count + 1
                else:
                        break
        if count == len(regex):
                valid = valid + 1
                
print(valid)
