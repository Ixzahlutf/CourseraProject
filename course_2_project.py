# We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which has the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet. We have also words that express positive sentiment and negative sentiment, in the files positive_words.txt and negative_words.txt.  Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. You will create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets. To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(x):
    for w in punctuation_chars :
        x = str(x).replace('%s'%w,'')
    return x    

# Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered positive words. Use the list, positive_words to determine what words will count as positive. The function should return a positive integer - how many occurrences there are of positive words in the text. Note that all of the words in positive_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.

def strip_punctuation(x):
    for w in punctuation_chars :
        x = str(x).replace('%s'%w,'')
    return x    


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(x):
    p = 0
    x = strip_punctuation(x).split()
    for pos in x :
        s = pos.lower()
        if s in positive_words:
            p += 1
    return p        
  
# Next, copy in your strip_punctuation function and define a function called get_neg which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered negative words. Use the list, negative_words to determine what words will count as negative. The function should return a positive integer - how many occurrences there are of negative words in the text. Note that all of the words in negative_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.

def strip_punctuation(x):
    for w in punctuation_chars :
        x = str(x).replace('%s'%w,'')
    return x  


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(x):
    n = 0
    x = strip_punctuation(x).split()
    for neg in x :
        s = neg.lower()
        if s in negative_words:
            n += 1
    return n  

# Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv which has the fake generated twitter data (the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet). Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. Copy the code from the code windows above, and put that in the top of this code window. Now, you will write code to create a csv file called resulting_data.csv, which contains the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet. The file should have those headers in that order. Remember that there is another component to this project. You will upload the csv file to Excel or Google Sheets and produce a graph of the Net Score vs Number of Retweets. Check Coursera for that portion of the assignment, if you’re accessing this textbook from Coursera.


def strip_punctuation(x):
    for w in punctuation_chars :
        x = str(x).replace('%s'%w,'')
    return x  


def get_neg(x):
    n = 0
    x = strip_punctuation(x).split()
    for neg in x :
        s = neg.lower()
        if s in negative_words:
            n += 1
    return n  


def get_pos(x):
    p = 0
    x = strip_punctuation(x).split()
    for pos in x :
        s = pos.lower()
        if s in positive_words:
            p += 1
    return p 


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

dt = open("project_twitter_data.csv","r")
data = dt.readlines()
rt=[]
rp=[]
ps=[]
ns=[]
net=[]
nb = 0
for d in data[1:]:
    spn = d.replace('\n','')
    sp = spn.split(',')
    #---positive words---#
    ps.append(get_pos(sp[0]))
    #---negative words---#
    ns.append(get_neg(sp[0]))
    #---net score---#
    net.append(int(get_pos(sp[0]))-int(get_neg(sp[0])))
    #---retweet---#
    rt.append(sp[1])
    #---replay---#    
    rp.append(sp[2])
    nb += 1

alldata =[]    
for r in range(nb):
    s = ('{},{},{},{},{}'.format(rt[r],rp[r],ps[r],ns[r],net[r]))
    alldata.append(s)
csvdata = open("resulting_data.csv","w") 
csvdata.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n") 
for csv in alldata:
    w = csvdata.write(csv + "\n")
csvdata.close()

