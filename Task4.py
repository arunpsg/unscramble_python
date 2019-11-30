"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

calling_numbers = set()
texting_numbers = set()

for call in calls:
    calling_numbers.add(call[0])

for text in texts:
    texting_numbers.add(text[0])

print("call_list : ", calling_numbers)
print("text_list : ", texting_numbers)

print("These numbers could be telemarketers:")
for marketing_number in sorted(calling_numbers.difference(texting_numbers)):
    print(marketing_number)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

