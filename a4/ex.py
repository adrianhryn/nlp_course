sents = [["hi", "my", "friend", "nice", "to", "meet", "you"], [1, 2, 3, 4], ["1"]]
pad_token = "1"
padded = []
length = max([len(i) for i in sents])
for i in sents:
    l_i = len(i)
    padded.append(i + [pad_token]*(length-l_i))

    ### END YOUR CODE
print(padded)