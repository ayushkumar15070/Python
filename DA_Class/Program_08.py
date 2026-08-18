child_id = (10, 20, 30, 40, 50)
chocolates_received = [12, 5, 3, 4, 6]

def calculate_total_chocolates():
    total = 0
    for chocolates in chocolates_received:
        total += chocolates
    return total

def reward_child(child_id_rewarded, extra_chocolates):
    if extra_chocolates < 1:
        print("Extra chocolates is less than 1")
        return

    found = False
    for i in range(len(child_id)):
        if child_id[i] == child_id_rewarded:
            chocolates_received[i] = chocolates_received[i] +  extra_chocolates
            found = True
            break

    if found:
        print(chocolates_received)
    else:
        print("Child id is invalid")


print(calculate_total_chocolates())
reward_child(20, 2)