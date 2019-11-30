"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
number_set = set()
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    for text in texts:
        number_set.update(str(text[0]))
        number_set.update(str(text[1]))

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for call in calls:
        number_set.update(str(call[0]))
        number_set.update(str(call[1]))

print("There are "+ str(number_set.__len__()) + " different telephone numbers in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
