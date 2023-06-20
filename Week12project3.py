count = int(input('How many ec2 instance names do you want? ' ))
department = (input( 'What is your department? ' ))
import random
import string
def ec2_name(count,department):
    ec2_name()
for _ in range(count):
    # get random string of length 6 without repeating letters
    random_gen = ''.join(random.sample(string.ascii_lowercase + string.digits,k=4))
    names = f"{department}-{random_gen}"
    ec2_name.append(names)

    return ec2_name

def names(count,department) :
    names = []
    names = ''.join(department(count))
for _ in range (count) :
    print('Here are your randomized instance names',names)
else:
    pass