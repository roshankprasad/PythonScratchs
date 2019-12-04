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

def strip_punctuation(txt):
    for punct in punctuation_chars:
        txt = txt.replace(punct,'')
    return txt

def get_pos(string):
    sentencelst = []
    sentencelst = string.strip().split()
    # print(sentencelst)
    pos_count = 0
    neg_count = 0
    for word in sentencelst:
        ext_word = strip_punctuation(word)
        # print(ext_word)
        if ext_word in positive_words:
            pos_count +=1
        elif ext_word in negative_words:
            neg_count +=1
        score = [pos_count,neg_count,pos_count-neg_count]
    return score
# print(get_pos(input()))

with open("project_twitter_data.csv") as fileref:
    contents = fileref.readlines()
    # for lin in contents[1:]:
    #     sentence = lin.strip().split(',')[0]
    #     print(sentence)
    #     scores = get_pos(sentence)
    #     for score in scores:
    #         print(score)


header_row = ['Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score']
with open("resulting_data.csv",'w') as outfile:
    for word in header_row:
        outfile.write(word)
    outfile.write('\n')
    for lin in contents[1:]:
        tweets = lin.strip().split(',')[0]
        print(tweets)
        tweet_infos = lin.strip().split(',')[1:]
        print(tweet_infos)
        for info in tweet_infos:
            outfile.write(info+',')
        scores = get_pos(tweets)
        print(scores)
        for score in scores[0:2]:
            outfile.write(str(score)+',')
        outfile.write(str(scores[-1]))
        outfile.write('\n')




