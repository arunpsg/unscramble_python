"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
phone_duration = {}
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for call in calls:
        phone_value = 0
        if phone_duration:
            if phone_duration.get(call[0]):
                phone_value = phone_duration.get(call[0])

        phone_value += int(call[3])
        phone_duration[call[0]] = phone_value

        phone_value1 = 0
        if phone_duration.__contains__(call[1]):
            phone_value1 = phone_duration.get(call[1])
            phone_value1 += int(call[3])
        phone_duration[call[1]] = phone_value1
max_phone_number = max(phone_duration, key=phone_duration.get)
print(max_phone_number + " spent the longest time, " + str(phone_duration[max_phone_number]) + " seconds, on the phone during September 2016.")

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

