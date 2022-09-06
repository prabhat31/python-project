def censor(sentence):
    badwords = 'apple orange banana'.split()
    sentence = sentence.split()

    for i in badwords:
        for words in sentence:
            if i in words:
                pos = sentence.index(words)
                sentence.remove(words)
                sentence.insert(pos, '*' * len(i))

    print (" ").join(sentence)
sentence = "you are an appletini and apple. new sentence: an orange is a banana. orange test."
censor(sentence)