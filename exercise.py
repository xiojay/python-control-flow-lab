# Exercise 0: Example

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()


# Exercise 1: Vowel or Consonant

def check_letter():
    # Your control flow logic goes here
    letter = input("Enter a single letter (a-z or A-Z): ").lower()
    
    if len(letter) == 1 and letter.isalpha():
        if letter in 'aeiou':
            print(f"The letter {letter} is a vowel.")
        else:
            print(f"The letter {letter} is a consonant.")
    else:
        print("Invalid input. Please enter a single alphabetical letter.")


# Call the function
check_letter()


# Exercise 2: Old enough to vote?

def check_voting_eligibility():
    try:
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Invalid input. Please enter a valid age.")
        return
    if age < 0:
        print("Age cannot be negative.")
        return
    voting_age = 18

    if age >= voting_age:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

# Call the function
check_voting_eligibility()



# Exercise 3: Calculate Dog Years

def calculate_dog_years():
    try:
        age = int(input("Input a dog's age: "))
        if age < 0:
            print("Please enter a valid age.")
            return
        
        if age <= 2:
            dog_years = age * 10
        else:
            dog_years = 20 + (age - 2) * 7
        
      
        print(f"The dog's age in dog years is {dog_years}.")
    
    except ValueError:
        print("Invalid age, please enter a whole number!")

# Call the function
calculate_dog_years()


# Exercise 4: Weather Advice

def weather_advice():
    # Your control flow logic goes here
    is_cold = input('Is it cold? (yes/no): ').lower()

    is_raining = input('Is it raining? (yes/no): ').lower()

    if is_cold not in ['yes', 'no'] or is_raining not in ['yes', 'no']:
        print('Invalid input. Answer with "yes" or "no". ')
        return 
    cold = is_cold == 'yes'
    raining = is_raining == 'yes'

    if cold and raining: 
        print('Wear a waterproof coat')
    elif cold and not raining: 
        print('Wear a warm coat.')
    elif not cold and raining: 
        print('Carry and umbrella.')
    elif not cold and not raining: 
        print('Wear light clothing.')

# Call the function
weather_advice()


# Exercise 5: What's the Season?

def determine_season():
    months_of_the_year = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    month = input('Enter the month of the year (Jan-Dec): ').capitalize() 
    if month not in months_of_the_year:
        print('Invalid month entered, please try again.')
        return

    try:
        day = int(input('Enter day of the month: '))
        if day < 1 or day > 31:
            raise ValueError
    except ValueError:
        print('Invalid day. Please enter a number between 1 and 31.')
        return

    if month == 'Dec' and day >= 21 or month in ['Jan', 'Feb'] or (month == 'Mar' and day <= 19):
        season = 'Winter'
    elif month == 'Mar' and day >= 20 or month in ['Apr', 'May'] or (month == 'Jun' and day <= 20):
        season = 'Spring'
    elif month == 'Jun' and day >= 21 or month in ['Jul', 'Aug'] or (month == 'Sep' and day <= 21):
        season = 'Summer'
    else:
        season = 'Fall'

    print(f'{month} {day:02d} is in {season}.')

# Call the function
determine_season()

