# https://www.bloomberg.com/news/articles/2018-06-18/google-is-training-machines-to-predict-when-a-patient-will-die
import collections

maxlen=1000
MAX_FEATURES = 10
stop_words=['\n', 'the', 'to', 'a', 'and', 'of', 'in', 'on', 'for', 'that', 'with', 'is', 'as', 'could', 'its', 'this', 'other','an', 'have', 'more', 'at',]

word_freqs = collections.Counter()
with open('./news.txt','r+', encoding='UTF-8') as f:
    for line in f:
        words = line.lower().split(' ')
        if len(words) > maxlen:
            maxlen = len(words)
        for word in words:
            if not (word in stop_words):
                word_freqs[word] += 1

print('max_len ',maxlen)
print('nb_words ', len(word_freqs))
print(word_freqs.most_common(MAX_FEATURES))
