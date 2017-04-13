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


print(compare("uno","ubo"))


hello=["uno","dos","tres"]

for i in hello:
    bye = i
    print (bye)
'''
q=1
bye = hello[q]
print(bye)
'''
