# CourseraProject
# The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable num.

s = open("travel_plans.txt","r") 
p = s.read()
num = len(p)

# We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words.

s = open('emotion_words.txt','r')
t = s.read()
u = t.split()
num_words = len(u)

# Assign to the variable num_lines the number of lines in the file school_prompt.txt.

s = open("school_prompt.txt","r")
p = s.readlines()
num_lines = len(p)

# Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.

s = open("school_prompt.txt","r")
p = s.read()
beginning_chars = p[:30]

# Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.

s = open("school_prompt.txt","r")
p = s.readlines()
three = []
for w in p :
    v = w.split()
    u = v [2]
    three.append(u)
# Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.

s = open("emotion_words.txt","r")
p = s.readlines()
emotions = []
for w in p :
    v = w.split()
    u = v [0]
    emotions.append(u)
# Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.

s = open("travel_plans.txt","r")
p = s.read()
first_chars = p[:33]

# Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.

p = open('school_prompt.txt','r')
s = p.read()
u = s.split()
p_words = []
for w in u :
    if 'p' in w :
        p_words.append(w)
