import re

regex = {'byr':re.compile('byr:([\w]+)'),
         'iyr':re.compile('iyr:([\w]+)'),
         'eyr':re.compile('eyr:([\w]+)'),
         'hgt':re.compile('hgt:([\w]+)'),
         'hcl':re.compile('hcl:#([0-9a-f]+)'),
         'ecl':re.compile('ecl:(amb|blu|brn|gry|grn|hzl|oth)\w*'),
         'pid':re.compile('pid:([\w]+)')
         #'cid':re.compile('cid:([\w]+)') Unused
        }


input = open('./inputs/4_input.txt','r')
strings = input.read().split('\n\n')

invalid = int(0)
for line in strings:
        for key, reg in regex.items():
                res = reg.search(line)
                if res:
                        if key == 'byr':
                                target = int(res.group(1))
                                if len(res.group(1)) != 4:
                                        invalid += 1
                                        break
                                if 1920 > target or target > 2002:
                                        invalid += 1
                                        break
                        elif key == 'iyr':
                                target = int(res.group(1))
                                if len(res.group(1)) != 4:
                                        invalid += 1
                                        break
                                if 2010 > target or target > 2020:
                                        invalid += 1
                                        break
                        elif key == 'eyr':
                                target = int(res.group(1))
                                if len(res.group(1)) != 4:
                                        invalid += 1
                                        break
                                if 2020 > target or target > 2030:
                                        invalid += 1
                                        break
                        elif key == 'hgt':
                                target = res.group(1)
                                if target.endswith('cm'):
                                        target = int(target[:-2])
                                        if 150 > target or target > 193:
                                                invalid += 1
                                                break
                                elif target.endswith('in'):
                                        target = int(target[:-2])
                                        if 59 > target or target > 76:
                                                invalid += 1
                                                break
                                else:
                                        invalid += 1
                                        break
                        elif key == 'hcl':
                                target = res.group(1)
                                if len(target) != 6:
                                        invalid += 1
                                        break
                        elif key == 'ecl':
                                target = res.group(1)
                                if len(target) != 3:
                                        invalid += 1
                                        break
                        elif key == 'pid':
                                target = re.sub("[^0-9]", "", res.group(1))
                                if len(target) != 9:
                                        invalid += 1
                                        break
                else:
                        invalid += 1
                        break
                

print('valid = ' + str(len(strings) - invalid))
