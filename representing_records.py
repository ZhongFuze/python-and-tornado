# start python
print("hello world!")

# people
bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 40000, 'hardware']

# fetch name, pay
print(bob[0], sue[2])

# what is bob's last name?
last_name = bob[0].split()[-1]
print(last_name)

# give sue a 25% raise
sue[2] *= 1.25
print(sue)

# reference in list of lists
people = [bob]
