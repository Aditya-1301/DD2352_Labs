"""
IF
    a = [60, 300, 240]
    a_s = [300, 240, 60]
    r = 100
THEN:
    IF
        a_s[i] >= (n-i)*r + 1
    THEN:
    flags[]

f[1] >= (n-1)r + 1

def check():

"""         


"""
My current understanding of the algorithm is as follows:

We want to have restart the machines in descending order of functioning time. This is so that we have the best chance at getting all machines running at the same time. 
After this for the operator to be able to successfully get all machines working simultaneously, the following has to hold true: 

f[1] >= (n-1) * r + 1

This is because the first machine should still be running at least 1 more minute after all other machines have been restarted, so that there is a possibility for all machines to run simultaneously otherwise the last machine doesn't get the opportunity to begin running at the same time as the first machine is running.
To keep track of the machines which have been restarted, I keep a list called flags which just contains the boolean value corresponding to a machine's running status.

I have 2 functions as part of the algorithm:
1. restart_machine(index) -> This function sets the flag corresponding to the machine which has been restarted to true
2. check(index, sorted_list) -> This function first restarts machine at index (i), then checks if all the flags have been set to true, if yes, then it means all the machines are running simultaneously thus its possible for the operator to take a break. If no, then we check if our pre established condition holds true, i.e. if sa[i] < (len(sa) - 1) * r + 1 then we return false, as its not possible in this situation for the last machine to be running at the same time as the current machine which has been restarted.
If neither of the previous conditions are met we can move on to restart the next machine and do this check again until we have gone through all of the machines.
"""


list_of_machines = [60, 300, 240]
sorted_list = sorted(list_of_machines, reverse = True) # This portion takes n(log(n)) time complexity
print(sorted_list)
r = 150 # 150
flags = [False for i in range(len(sorted_list))]

def check(i, sa):
    flags[i] = True # Restart Machine at index i and indicate this by setting corresponding flag to True
    if all(flags) == True:
        return True
    elif sorted_list[i] < (len(sa) - 1) * r + 1:
        return False
    else:
        return check(i+1, sa[1:])


print(check(0, sorted_list))

def machine_check():
    for i in range(len(sorted_list)):
        if sorted_list[i] < (len(sorted_list) - i - 1) * r + 1:
            return False
    return True


print("Machine check: ", machine_check())




