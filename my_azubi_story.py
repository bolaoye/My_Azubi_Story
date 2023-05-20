# User is prompted for his/her name
name_hold = input('what is your name: ')

#  Welcome message is provided for the user
print(f'You are welcome, {name_hold}. You are about to embark on a thrilling adventure on a mysterious island.\n ')

# Users provide different inputs
country = input('Which country are you from: ')
city = input('What city do you live in: ') 
institute = input('What is the name of the training Institution? ')
course = input('What course are you being trained for? ')
duration = input('What is the duration of the program? ')
testify = input('In one word, What can you say about their training: ') 

# Display the complete story 

print(f'My name is {name_hold}.I live in {city}, {country}. I am currently running a {course} training program at {institute}.\n{institute} provides a comprehensive {duration} training which prepares me for job search, resume building not leaving out the core technical skills for {course}.\nThe training is {testify}.')





