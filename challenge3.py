def wordLadder(beginWord,endWord,wordlist):
    word = beginWord
    count=0
    step=0

    if word in wordlist:
        wordlist.remove(word)

    for q in wordlist:
        if word != endWord:
            if compare(word,q) is True:
                word = q
                step += 1
    return step

def compare(word1,word2):
    count = 0
    if len(word1) != len(word2):
        return False
    else:
        for q in range(len(word1)):
            if word1[q] == word2[q]:
                count += 1;
    if count == len(word1) - 1:
        return True
    else:
        return False

a="hit"
b="cog"
c=["hot","dot","dog","lot","log","cog"]
print(wordLadder(a,b,c))
