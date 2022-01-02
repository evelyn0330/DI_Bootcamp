sentence = input("Please provide a sequence of words separated by a comma: \n")
sentence_list = sentence.split(",")
sentence_list.sort()
print(",".join(sentence_list))