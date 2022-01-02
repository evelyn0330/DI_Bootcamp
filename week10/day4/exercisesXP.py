import random, json
# Exercise 1

# words = []


# def get_words_from_file():
#     with open("sowpods.txt") as f:
#         for line in f.readlines():
#             words.append(line)


# def get_random_sentence(length: int):
#     sentence = ''.join([random.choice(words) for i in range(length)])
#     print(sentence.lower())


# def main():
#     print("This program will generate a random sentence for you!")
#     length = int(input("Choose how long you want your sentence to be. Between 2-20: "))
#     if 1 < length < 21:
#         get_words_from_file()
#         get_random_sentence(length)
#     else:
#         print("Sorry! Incorrect number!")

# main()
# ---------------------------------------------------------------------------------------------------------------------------------
# Exercise 2

sampleJson = { 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}

print(sampleJson['company']['employee']['payable'])
sampleJson['company']['employee']['birth_date'] = ['3/30/1993']
print(sampleJson['company']['employee'])

json_file = 'file.json'
with open(json_file, 'w') as file_obj:
   json.dump(sampleJson, file_obj, indent=2)