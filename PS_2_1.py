"""
To obtain a set of McNugget packets, and an order quantity. It then calculates the largest quantity that can't be ordered, and prints the 
current order in McNugget packets, which can be ordered. Run only in python 2.6 and above
""" 
set_m = (raw_input('Enter the McNugget package set in\nthe format without braces, e.g.,(6 9 20): ')).split()
buy_x = int(raw_input('\nEnter the number of McNuggets to order: '))
set_m = [int(c) for c in set_m]
table_m = []                            # for storing the multiples of packet set numbers
e_flag = 1                              # error flag if a quantity can't be ordered
order = []                              # to store the values of packets that can be produced
l_chk = []                              # to store generated list of valid order quantities up to a limit (300 here).
no_order = []                           # to store generated list of quantities that can't be ordered

for mul in range(0, 101):               # we're keeping a certain limit here. Increase the range limit if ordering a large number.
    table_m.append([mul * c for c in set_m])

for i in [row[0] for row in table_m]:   # to generate the list of quantities that can be ordered, up to a limit
    for j in [row[1] for row in table_m]:
        for k in [row[2] for row in table_m]:
            l_chk.append(i + j + k)

for it_chk in range(1, 1001):            # to check if a quantity, up to a limit, can't be ordered.
    if it_chk not in l_chk:
        no_order.append(it_chk)

print "\nThe largest quantity that can't be ordered is:", no_order[-1] 

for i in [row[0] for row in table_m]:                                   # to calculate the packet quantities for an order
    for j in [row[1] for row in table_m]:
        for k in [row[2] for row in table_m]:
            if i + j + k == buy_x:
                order.append([i, j, k])
                e_flag = 0
order.sort()
final = []                                  # for storing the actual packet quantities    
for set in order:
    tmp = []
    try:
        tmp.append(set[0]/set_m[0])
        tmp.append(set[1]/set_m[1])
        tmp.append(set[2]/set_m[2])
    except ZeroDivisionError:               # if the calculated packet quantity is zero
        tmp.append(set[0]*set_m[0])
        tmp.append(set[1]*set_m[1])
        tmp.append(set[2]*set_m[2])
    finally:
        final.append(tmp)


    
if e_flag == 0:
    print '\nYou can sell the current order of {0} McNuggets in :-'.format(buy_x)
    for set in final:                           # for final calculated order printing
        print '{0} packets of {1}, {2} packets of {3} and {4} packets of {5}'.format(set[0], set_m[0], 
                                                                                 set[1], set_m[1], 
                                                                                 set[2], set_m[2])
if e_flag == 1:                                                         # if can't be ordered, print
    print '\nCannot be sold with that quantity. Restart and enter a new quantity.'



