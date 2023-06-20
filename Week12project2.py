#Several departments share an AWS environment. You need to ensure that the EC2s are properly named and are unique so team members can easily tell who the EC2 instances belong to. Use Python to create your unique EC2 names that the users can then attach to the instances. The Python Script should:
#All the user to input how many EC2 instances they want names for and output the same amount of unique names.
#Allow the user to input the name of their department that is used in the unique name.
#Generate random characters and numbers that will be included in the unique name.

#create subclasses of random? maybe thats what i need to combine the input they give me into a random generator
#input+random? like i first ask for their department and then i add the random to it
#for instance
#_random ( instances * k,counts=None + department)
#for i in instances:

instances = int(input('How many ec2 instance names do you want?' ))
department = (input( 'What is your department?' ))
import random
names = department + random
new_name = names + department
for num in instances(instances):
    print('Here are your randomized instance names',new_name)
else:
    pass