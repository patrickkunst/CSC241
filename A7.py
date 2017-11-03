# Patrick Kunst
# CSC 241
# Assignment 7

def get_file_data(file_name):
    file = open(file_name)
    file_data = file.readlines()
    file.close()
    return file_data[1:]

def process_projects(proj_list, budget_amount):
    used_proj = []
    cost = 0
    index = 0
    
    while cost < budget_amount:
        proj_data = proj_list[index].split(',')
        proj_cost = eval(proj_data[1])
        
        flag = eval(proj_data[3])

        if flag == False:
            index += 1
            continue
        if cost + proj_cost > budget_amount:
            break
        
        cost += proj_cost
        used_proj.append(proj_data)
        index += 1

    return used_proj

def print_report(proj_keep):
    print('Name        Cost')
    print('---------   -------')

    fmt = '{}   ${}'
    index = 0
    cost = 0
    for proj in proj_keep:
        print(fmt.format(proj_keep[index][0], proj_keep[index][1]))
        cost += eval(proj_keep[index][1])
        index += 1
        
    print('---------   -------')
    fmt = 'Total       ${}'
    print(fmt.format(cost))


name = input('Enter file name: ')
budget = eval(input('Enter budget: '))
data = get_file_data(name)
projects = process_projects(data, budget)
print_report(projects)


