# The dictionary Junior shows a schedule for a junior year semester. The key is the course name and the value is the number of credits. Find the total number of credits taken this semester and assign it to the variable credits. Do not hardcode this – use dictionary accumulation!

Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits = 0
for credit in Junior.values() :
    credits = credits + credit
    
# Create a dictionary, freq, that displays each character in string str1 as the key and its frequency as the value.

str1 = "peter piper picked a peck of pickled peppers"
freq = {}
for nfreq in str1 :
    if nfreq not in freq :
        freq[nfreq] = 0
    freq[nfreq] = freq[nfreq] + 1    
    
# Provided is a string saved to the variable name s1. Create a dictionary named counts that contains each letter in s1 and the number of times it occurs.

s1 = "hello"
counts = {}
for dic in s1 :
    if dic not in counts :
        counts[dic] = 0
    counts[dic] = counts[dic] + 1
# Create a dictionary, freq_words, that contains each word in string str1 as the key and its frequency as the value.

str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
str_low = str1.split()
freq_words = {}
for dic in str_low :
    if dic not in freq_words :
        freq_words[dic] = 0
    freq_words[dic] = freq_words[dic] + 1   
# Create a dictionary called wrd_d from the string sent, so that the key is a word and the value is how many times you have seen that word.

sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
sentuh = sent.split()
wrd_d = {} 
for dic in sentuh :
    if dic not in wrd_d :
        wrd_d[dic] = 0
    wrd_d[dic] = wrd_d[dic] + 1    
    
# Create the dictionary characters that shows each character from the string sally and its frequency. Then, find the most frequent letter based on the dictionary. Assign this letter to the variable best_char.

sally = "sally sells sea shells by the sea shore"
characters = {}
for dic in sally :
    if dic not in characters :
        characters[dic] = 0
    characters[dic] = characters[dic] + 1
    
key = list(characters.keys())
best_char = key[0]
for bchar in key :
    if characters[bchar] > characters[best_char]:
        best_char = bchar
    
# Find the least frequent letter. Create the dictionary characters that shows each character from string sally and its frequency. Then, find the least frequent letter in the string and assign the letter to the variable worst_char.

sally = "sally sells sea shells by the sea shore and by the road"
characters = {}
for dic in sally :
    if dic not in characters :
        characters[dic] = 0
    characters[dic] = characters[dic] + 1
    
key = list(characters.keys())
worst_char = key[0]
for bchar in key :
    if characters[bchar] < characters[worst_char]:
        worst_char = bchar
    
# Create a dictionary named letter_counts that contains each letter and the number of times it occurs in string1. Challenge: Letters should not be counted separately as upper-case and lower-case. Intead, all of them should be counted as lower-case.

string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
string_low = string1.lower()
letter_counts = {}
for dic in string_low :
    if dic not in letter_counts :
        letter_counts[dic] = 0
    letter_counts[dic] = letter_counts[dic] + 1    

# Create a dictionary called low_d that keeps track of all the characters in the string p and notes how many times each character was seen. Make sure that there are no repeats of characters as keys, such that “T” and “t” are both seen as a “t” for example.

p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
p_low = p.lower()
low_d = {}
for dic in p_low :
    if dic not in low_d :
        low_d[dic] = 0
    low_d[dic] = low_d[dic] + 1    
