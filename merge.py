import os


def iterbrowser(path):
    for home, dirs, files in os.walk(path):
        for filename in files:
            yield os.path.join(home, filename)


stopwords = set()
for fullname in iterbrowser('data'):
    with open(fullname) as f:
        tokens = [line.strip() for line in f.readlines()]
        stopwords = stopwords.union(set(tokens))

stopwords = list(stopwords)
print('word count:{}'.format(len(stopwords)))

with open('stopwords_all.txt', 'w') as f:
    f.writelines([word+"\n" for word in stopwords])
