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

callingNumbers = set()
callReceivingNumbers = set()
textNumbers = set()
textReceivingNumbers = set()

for call in calls:
    callingNumbers.add(call[0])
    callReceivingNumbers.add(call[1])

for text in texts:
    textNumbers.add(text[0])
    textReceivingNumbers.add(text[1])

print("call_list : ", callingNumbers)
print("text_list : ", textNumbers)

marketingNumbers = sorted(callingNumbers.difference(textNumbers).difference(callReceivingNumbers).difference(textReceivingNumbers))

print("These numbers could be telemarketers:")
for marketing_number in marketingNumbers:
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

