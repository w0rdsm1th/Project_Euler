#_________________#_________________#_________________#_________________#_________________#_________________
#Q1
'''
calculating 'shortest path' after a series of taxicab geometry directions
shortest path = coordinate difference
start facing north, at origin 0,0
'''
path_dir_list = r"C:\Users\IBM_ADMIN\Documents\2 - Project_Euler\AdventCode_files\q1_direction_list.txt"
with open(path_dir_list, 'r') as f:
        direction_list_string = f.read()
direction_list = direction_list_string.split(",")
direction_list = [str.strip(_) for _ in direction_list]

def q1_taxi_cab_interp(input_dir_list):
    poss_headings = ['N', 'E', 'S', 'W']  # can only walk along the grids of the city
    curr_heading = 'N'  # start by looking north
    curr_position = [0, 0]  # start at the origin, distance to final destination is then

    for each_dir in input_dir_list:
        turn, fwd = each_dir[0], int(each_dir[1:])
        assert turn in ['R', 'L']
        assert isinstance(fwd, int) and fwd >= 1
        if turn == 'R':
            curr_heading = poss_headings[(poss_headings.index(curr_heading)+1)%4]
        elif turn == 'L':
            curr_heading = poss_headings[(poss_headings.index(curr_heading)-1)%4]

        if curr_heading == 'N':
            curr_position[1] += fwd
        if curr_heading == 'S':
            curr_position[1] -= fwd
        if curr_heading == 'E':
            curr_position[0] += fwd
        if curr_heading == 'W':
            curr_position[0] -= fwd
    return {'curr_heading':curr_heading, 'curr_position':curr_position}

#test cases
q1_taxi_cab_interp(['R2', 'R2', 'R2', 'R2'])
q1_taxi_cab_interp(['R2', 'R2', 'R2'])
q1_taxi_cab_interp(['R5', 'L5', 'R5', 'R3'])

q1_taxi_cab_interp(['R2', 'R2', 'R2', 'R2', 'R2'])
q1_taxi_cab_interp(['L2', 'L2', 'L2', 'L2', 'L2', 'L2', 'L2'])

q1_taxi_cab_interp(direction_list)


input_dir_list = direction_list
each_dir = direction_list[1]

def q1_taxi_cab_interp_visit_twice(input_dir_list):
    poss_headings = ['N', 'E', 'S', 'W']  # can only walk along the grids of the city
    curr_heading = 'N'  # start by looking north
    curr_position = [0, 0]  # start at the origin, distance to final destination is then
    visited_locs = [[0,0], ]
    for each_dir in input_dir_list:
        turn, fwd = each_dir[0], int(each_dir[1:])
        assert turn in ['R', 'L']
        assert isinstance(fwd, int) and fwd >= 1
        if turn == 'R':
            curr_heading = poss_headings[(poss_headings.index(curr_heading)+1)%4]
        elif turn == 'L':
            curr_heading = poss_headings[(poss_headings.index(curr_heading)-1)%4]

        if curr_heading == 'N':
            for each_step in range(fwd):
                curr_position[1] += 1
                if curr_position in visited_locs:
                    print(visited_locs)
                    return 'Visited {} twice!'.format(curr_position)
                elif curr_position not in visited_locs:
                    visited_locs.append(curr_position)
        if curr_heading == 'S':
            for each_step in range(fwd):
                curr_position[1] -= 1
                if curr_position in visited_locs:
                    print(visited_locs)
                    return 'Visited {} twice!'.format(curr_position)
                elif curr_position not in visited_locs:
                    visited_locs.append(curr_position)

        if curr_heading == 'E':
            for each_step in range(fwd):
                curr_position[0] += 1
                print(curr_position)
                if curr_position in visited_locs:
                    print(visited_locs)
                    return 'Visited {} twice!'.format(curr_position)
                elif curr_position not in visited_locs:
                    visited_locs.append(curr_position)
        if curr_heading == 'W':
            for each_step in range(fwd):
                curr_position[0] -= 1
                if curr_position in visited_locs:
                    print(visited_locs)
                    return 'Visited {} twice!'.format(curr_position)
                elif curr_position not in visited_locs:
                    visited_locs.append(curr_position)

    return {'curr_heading':curr_heading, 'curr_position':curr_position}

t = [0, ]
t.append(1)

curr = 0
for _ in range(8):
    curr+=1
    print(curr)

q1_taxi_cab_interp_visit_twice(direction_list)

'''
LESSONS LEARNED
good func design, similar to peter norvigs of tracking the grid heading and forward steps
1. main bug for star 1: didnt consider 2 or 3 digit forward steps

2.

'''


#_________________#_________________#_________________#_________________#_________________#_________________
#Q2
'''

'''

'''
LESSONS LEARNED
1.

2.

'''


#_________________#_________________#_________________#_________________#_________________#_________________
#Q
'''

'''

'''
LESSONS LEARNED
1.

2.

'''


#_________________#_________________#_________________#_________________#_________________#_________________
#Q
'''

'''

'''
LESSONS LEARNED
1.

2.

'''


#_________________#_________________#_________________#_________________#_________________#_________________
#Q
'''

'''

'''
LESSONS LEARNED
1.

2.

'''


#_________________#_________________#_________________#_________________#_________________#_________________
#Q
'''

'''

'''
LESSONS LEARNED
1.

2.

'''


#_________________#_________________#_________________#_________________#_________________#_________________
#Q
'''

'''

'''
LESSONS LEARNED
1.

2.

'''


#_________________#_________________#_________________#_________________#_________________#_________________
#Q
'''

'''

'''
LESSONS LEARNED
1.

2.

'''


#_________________#_________________#_________________#_________________#_________________#_________________
#Q
'''

'''

'''
LESSONS LEARNED
1.

2.

'''


#_________________#_________________#_________________#_________________#_________________#_________________
#Q
'''

'''

'''
LESSONS LEARNED
1.

2.

'''


#_________________#_________________#_________________#_________________#_________________#_________________
#Q
'''

'''

'''
LESSONS LEARNED
1.

2.

'''


#_________________#_________________#_________________#_________________#_________________#_________________
#Q
'''

'''

'''
LESSONS LEARNED
1.

2.

'''


#_________________#_________________#_________________#_________________#_________________#_________________
#Q
'''

'''

'''
LESSONS LEARNED
1.

2.

'''


#_________________#_________________#_________________#_________________#_________________#_________________
#Q
'''

'''

'''
LESSONS LEARNED
1.

2.

'''


#_________________#_________________#_________________#_________________#_________________#_________________
#Q
'''

'''

'''
LESSONS LEARNED
1.

2.

'''


#_________________#_________________#_________________#_________________#_________________#_________________
#Q
'''

'''

'''
LESSONS LEARNED
1.

2.

'''


#_________________#_________________#_________________#_________________#_________________#_________________
#Q
'''

'''

'''
LESSONS LEARNED
1.

2.

'''


#_________________#_________________#_________________#_________________#_________________#_________________
#Q
'''

'''

'''
LESSONS LEARNED
1.

2.

'''


#_________________#_________________#_________________#_________________#_________________#_________________
#Q
'''

'''

'''
LESSONS LEARNED
1.

2.

'''


#_________________#_________________#_________________#_________________#_________________#_________________
#Q
'''

'''

'''
LESSONS LEARNED
1.

2.

'''


#_________________#_________________#_________________#_________________#_________________#_________________
#Q
'''

'''

'''
LESSONS LEARNED
1.

2.

'''
