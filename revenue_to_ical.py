import csv
from datetime import datetime
import vobject

# Open the CSV file
with open('revenue_events_goldenthinker.csv', 'r') as file:
    # Read the CSV file
    reader = csv.reader(file)

    # Create a new iCalendar object
    cal = vobject.iCalendar()

    # Loop through each row in the CSV file
    for row in reader:
        # Create a new event object
        event = vobject.newFromBehavior('vevent')

        # Set the event properties
        event.add('summary').value = row[1] + ' ' + row[2]

        # Check if the date value is valid
        if row[5] != 'Event Date':
            event.add('dtstart').value = datetime.strptime(row[5], '%d/%m/%Y')
            event.add('dtend').value = datetime.strptime(row[5], '%d/%m/%Y')

        event.add('description').value = 'Registration Number: ' + row[0] + '\n' \
                                          'Period: ' + row[3] + '\n' \
                                          'Amount: ' + row[4] + '\n' \
                                          'Receipt Number: ' + row[6]

        # Add the event to the calendar
        cal.add(event)

# Save the iCalendar file
with open('revenue_events_goldenthinker.ics', 'w') as file:
    file.write(cal.serialize())