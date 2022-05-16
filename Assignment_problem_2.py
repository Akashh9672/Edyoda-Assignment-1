# for taking word from user
word=str (input())
print("Entered word:",word)
reverse_word="" # empty variable for storing reverse word
for i in word:
    reverse_word=i+reverse_word
print("Reversed word:",reverse_word)