# Patrick Kunst
# CSC 241
# Midterm Part 1

def load_file(file_name):
    file = open(file_name)
    data = file.readlines()

    return(data)

def convert_line(line):
    data_list = line.split(', ')

    import time
    time_obj = time.localtime(eval(data_list[0]))
    time_string = time.strftime('%m/%d/%Y %I:%M %p', time_obj)
    exhibit = str(data_list[1])
    habitat = str(data_list[2])
    temperature = eval(data_list[3])
    ph = eval(data_list[4])
    nh4 = eval(data_list[5])

    return [time_string, exhibit, habitat, temperature, ph, nh4]

def check_warning(temp_val, ph_val, nh4_val):
    warnings = []

    if (temp_val < 76) or (temp_val > 80):
        warnings.append('Temperature Warning')

    if (ph_val < 5.4) or (ph_val > 6.8):
        warnings.append('pH Warning')

    if (nh4_val < 0) or (nh4_val > 1):
        warnings.append('NH4 Warning')

    warn_string = ''
    
    for x in warnings:
        if x != warnings[-1]: #To prevent commas at the end
            warn_string += (x + ', ')
        else:
            warn_string += x

    return warn_string

name = input('Please enter the file path and name: ')

file_lines = load_file(name)

print('''
Timestamp             Exhibit   Habitat                  Temp    pH     NH4
-------------------   -------   --------------           ----   ----   -----''')

for x in file_lines:
    file_data = convert_line(x)
    data_warnings = check_warning(file_data[3], file_data[4], file_data[5])

    fmt = '{:22}{:10}{:21}{:8.1f}{:7.2f}{:8.3f}    {}'
    print(fmt.format(file_data[0], file_data[1], file_data[2], file_data[3], file_data[4], file_data[5], data_warnings))
