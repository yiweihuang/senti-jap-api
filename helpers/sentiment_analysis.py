import sys
import json
from jNlp.jSentiments import *

jp_wn = 'lib/wnjpn-all.tab'
en_swn = 'lib/SentiWordNet_3.0.0.txt'

if len(sys.argv) < 2:
    print('Usage: python [].py sentence')
    sys.exit()
else:
    sentence = sys.argv[1]

def dict_to_arr():
    des_dict = 'lib/Description.txt'
    with open(des_dict) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
    return content

def p_or_n(pScore, nScore):
    if pScore == nScore:
        return 'Text is Neural or Cannot Determine'
    if pScore > nScore:
        return 'Positive'
    else:
        return 'Negative'

def senti(temp_arr):
    classifier = Sentiment()
    clf  = classifier.train(en_swn, jp_wn)

    total_pScore = 0
    total_nScore = 0
    for word in temp_arr:
        try:
            des_pScore, des_nScore = classifier.polarScores_text(word.decode('utf-8'))
            total_pScore += des_pScore
            total_nScore += des_nScore
        except BaseException:
            pass
    sentiment = p_or_n(total_pScore, total_nScore)
    return {'pScore': total_pScore, 'nScore': total_nScore, 'sentiment': sentiment}


temp_arr = []
dict_ = dict_to_arr()
for word in dict_:
    if word in sentence and word not in temp_arr:
        temp_arr.append(word)
print(senti(temp_arr)['pScore'])
print(senti(temp_arr)['nScore'])
print(senti(temp_arr)['sentiment'])
