import csv
from datetime import datetime
from vobject import iCalendar, Event

# Open the CSV file
with open('revenue_events.csv', 'r') as file:
    # Read the CSV file
    reader = csv.reader(file)

    # Create a new iCalendar object
    cal = iCalendar()

    # Loop through each row in the CSV file
    for row in reader:
        # Create a new event object
        event = Event()

        # Set the event properties
        event.add('summary').value = row[1] + ' ' + row[2]
        event.add('dtstart').value = datetime.strptime(row[5], '%d/%m/%Y')
        event.add('dtend').value = datetime.strptime(row[5], '%d/%m/%Y')
        event.add('description').value = 'Registration Number: ' + row[0] + '\n' \
                                            'Period: ' + row[3] + '\n' \
                                            'Amount: ' + row[4] + '\n' \
                                            'Receipt Number: ' + row[6]

        # Add the event to the calendar
        cal.add_component(event)

# Save the iCalendar file
with open('revenue_events.ics', 'w') as file:
    file.write(cal.serialize())
```
