
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
fileref = open("project_twitter_data.csv",'r')
contents = fileref.read()
#for punct in punctuation_chars:
sepr = contents.split('\n')
tweets = []
for val in sepr:
    tweets.append(val.split(','))

print(tweets)
