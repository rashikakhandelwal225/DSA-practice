def numRescueBoats( people, limit):
    c = 0
    i = 0
    people.sort()
    n = len(people)
    i = 0
    j = n - 1
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1

        j -= 1
        c += 1
    return c
    # boat = 0
    # start = 0
    # people.sort()
    #
    #
    # while len(people) != 0:
    #     if people[start] <= limit:
    #         rem_weight = abs(limit - people[start])
    #         people.remove(people[start])
    #         if len(people) != 0 and rem_weight != 0 and rem_weight in people:
    #             people.remove(rem_weight)
    #         elif len(people) != 0 and rem_weight != 0 and people[start] <= rem_weight:
    #             people.remove(people[start])
    #         boat += 1
    # return boat
people = [5,1,7,4,2,4]
limit = 7
print(numRescueBoats(people,limit))

