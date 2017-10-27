# Patrick Kunst
# CSC 241
# Lab 4 Part 1

def parse(name):
    name = name.replace('-', '.')
    element_list = name.split('.')
    return element_list

print(parse('ascii.base 64.module 4.job 6.anterior-distal'))
print(parse('octal.base 8.module 9.job 44.posterior-distal'))
print(parse('hex-decimal.base 16.module 9.job 44.superior'))
print(parse('beta-sigma.binary.sub_module 8.job 4-5-6.medial-thoracic'))
print(parse('one.two.red.blue'))
print(parse('one-two-red-blue'))
