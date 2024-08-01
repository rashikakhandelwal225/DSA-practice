def survivedRobotsHealths(positions, healths, directions):
    start = 0
    end = 1
    status1 = ''
    status2 = ''
    direction = list(directions)

    while end < len(healths):
        # check health
        if healths[start] == healths[end]:
            prev_start = start
            prev_end = end
            del healths[start: end + 1]
            del direction[start: end + 1]
            status1 = "Same health"
        elif healths[start] > healths[end]:
            upper_health_index = start
            lower_health_index = end
            status1 = "Different health"
        else:
            upper_health_index = end
            lower_health_index = start
            status1 = "Different health"

        # check direction
        if status1 == "Different health":
            if direction[start] == direction[end]:
                status2 = "No collision"
                if end < len(healths) - 1:
                    start += 1
                    end += 1
                else:
                    return healths
            elif direction[start] != direction[end]:
                status2 = "collision"
                # update health of upper health
                healths[upper_health_index] -= 1
                end += 1
                healths.pop(lower_health_index)
                direction.pop(lower_health_index)

    return healths

positions = [3,5,2,6]
healths = [10,10,15,12]
directions = "RLRL"
print(survivedRobotsHealths(positions, healths, directions))

positions = [1,2,5,6]
healths = [10,10,11,11]
directions = "RLRL"
print(survivedRobotsHealths(positions, healths, directions))

positions = [5,4,3,2,1]
healths = [2,17,9,15,10]
directions = "RRRRR"
print(survivedRobotsHealths(positions, healths, directions))