#open new txt file and write
file = open('concept.txt', 'w')
file.write('this is lexzy concept/n')
file.write('a fashion brand/n')
file.write('we deal fashion wear for men/n')
file.write('we also style/n')
file.write('you can check us out on IG at Lexzyconcept/n')

#read txt file
file = open('concept.txt', 'r')
file = file.read()

#word count
words = file.split()
word_count = len(words)

#uppercase for all words
data_upper = file.upper()

#modified version to a new file 
file = open('twl.txt', 'w')
file.write(data_upper + "\n")
file.write(f"\nWord Count: {word_count}\n")

print("file 'twl.txt'created successfully")
