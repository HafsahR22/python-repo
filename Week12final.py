# A simple ec2 unique name generator with department name attached
import random

count = int(input('How many ec2 instance names do you want? ' ))
department = (input( 'What is your department? ' ))


print('Here are your generated names: ')
for n in range (count):
  print(random.randint(2, count), random.randint(2, count), random.randint (2,count), random.randint (2,count), department, sep='-')
