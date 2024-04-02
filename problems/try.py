def canCompleteCircuit(gas, cost):
    i, j, curr_gas = 0, 0, 0
    while True:
        if j == i - 1:
            return i
        if curr_gas < cost[j]:
            j += 1
            i = j
            curr_gas = 0
            break
        else:
            j %= len(gas)
            if j == len(gas)-1:
                curr_gas += gas[0] - cost[j]
            else:
                curr_gas += gas[j + 1] - cost[j]
            j += 1
        # if j == i:
        #     return -1


gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(canCompleteCircuit(gas, cost))
