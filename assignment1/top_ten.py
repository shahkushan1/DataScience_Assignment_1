import json
import sys
def main():

    tweet_file = open(sys.argv[1])
    data = []
    for line in tweet_file:
       data.append(json.loads(line))
    hash_list = []
    for i in range(len(data)):
        tweet = data[i]
        if len(tweet) > 1 :
            tweet = data[i]['entities']
            hashtag = tweet['hashtags']
            
            if len(hashtag)>0:
                for i in range(0,len(hashtag)):
                    tag = hashtag[i]['text'].encode('utf-8')
                    hash_list.append(tag)
     

    hash_dict = {}
    for i in hash_list:
        if i in hash_dict.keys():
            hash_dict[i] = hash_dict[i]+1
        else :
            hash_dict[i] = 1
    sorted_hash_list = []
    
    for w in sorted(hash_dict, key=hash_dict.get,reverse=True)[0:10]:
        print str(w), float(hash_dict[w]) 


if __name__ == '__main__':
    main()
