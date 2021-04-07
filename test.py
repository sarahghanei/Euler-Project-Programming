def sort_each_class(clss, base):
    clss = {name: info for name, info in sorted(clss.items()\
                    ,key=lambda x: x[1][base], reverse=True)}

# print name: speed of 3 fastest in each class
def print_tree_tops(clss):
    for name, info in list(clss.items())[:3]:
        print(name, ' : ', info[2])

def get_fastest(Runners):
    # print the fastest runner`s name
    fastest_speed = 0
    fastest_name = ''
    for clss in list(Runners.values()):
        name, speed = list(clss.items())[0][0], list(clss.items())[0][1][2]
        if fastest_speed < speed:
            fastest_speed = speed
            fastest_name = name
    return fastest_name, fastest_speed

Names = input('Enter the runners name?\n').split(',')
Names = set((map(lambda x:x.strip().lower(), Names)))
Runners = {"unfinished" : {}, "marathon" : {}, "half_marathon" : {}, "ultra" : {}}
# Runners = {"unfinished" : {"sima": (1, 3, 4, 7), "ala": (4, 3, 2, 1)}, {"marathon" : {}}, {"half_marathon" : {}}, {"ultra" : {}}}
categorize = lambda x: "unfinished" if x <= 10\
                        else "half_marathon" if 10 < x <= 21.0975\
                            else "marathon" if 21.0975 < x <= 42.195\
                                else "ultra"
for Name in Names:
    distance = float(input(Name + ' distance(km) : '))
    duration_time = float(input(Name + ' duration time(minute) : '))
    speed = round(distance / (duration_time/60), 2)
    pace = round(duration_time / distance, 2)
    Runners[categorize(distance)][Name] = (distance, duration_time, speed, pace)


for key in Runners.keys():
    sort_each_class(Runners[key], base = 2)

for clss in Runners.values():
    print_tree_tops(clss)

fastest_runner = get_fastest(Runners)
print('fastest: ', fastest_runner[0], ' : ', fastest_runner[1])

# print the runnner who passes most distance
sort_each_class(Runners["ultra"], base = 0)
name_highest_distance = list(Runners["ultra"].itemst())[0][0]
info_highest_distance = list(Runners["ultra"].itemst())[0][1][0]
print("the most resilient: " + name_highest_distance + " ran " + str(info_highest_distance) + " kilometer.")