# STUDENT NAME: SHRUTI PAGHADAL
# STUDENT ID: 20CE065
# AIM: You are given a string. Your task is to count the frequency of letters of the string and print the letters in descending order of frequency.

print("\n------------------------------------QUESTION 1------------------------------------------------------------\n")
## Count frequency with dictionary and sort by Value from dictionary Items.
string = input()
dictionary = {}
for i in string:
    dictionary[i] = dictionary.get(i,0) + 1

dictionary = sorted(dictionary.items(),key=lambda x: (-x[1],x[0]))
print("Frequency of the letters:\n")
for i in dictionary:
    print(i[0],i[1])
    