import csv
from icalendar import Calendar, Event
from datetime import datetime

# Open the CSV file
with open('events.csv', 'r') as csvfile:
    # Parse the CSV file using the csv module
    reader = csv.DictReader(csvfile)

    # Create a new calendar
    cal = Calendar()

    # Iterate over each row in the CSV file
    for row in reader:
        # Split the date range into two dates
        start_date, end_date = row['Period'].split(' - ')

        # Create a new event for the start date
        event = Event()

        # Set the event name to the value in the "Event type" column
        event.add('summary', row['Event type'])

        # Set the event start and end dates to the value in the "Event Date" and start date
        event.add('dtstart', datetime.strptime(row['Event Date'], '%d/%m/%Y'))
        event.add('dtend', datetime.strptime(start_date, '%d/%m/%Y'))

        # Set the event location to the value in the "Reg No/Trader No." column
        event.add('location', row['Reg No/Trader No.'])

        # Add the event to the calendar
        cal.add_component(event)

        # Create a new event for the end date
        event = Event()

        # Set the event name to the value in the "Event type" column
        event.add('summary', row['Event type'])

        # Set the event start and end dates to the end date and the value in the "Event Date" column
        event.add('dtstart', datetime.strptime(end_date, '%d/%m/%Y'))
        event.add('dtend', datetime.strptime(row['Event Date'], '%d/%m/%Y'))

        # Set the event location to the value in the "Reg No/Trader No." column
        event.add('location', row['Reg No/Trader No.'])

        # Add the event to the calendar
        cal.add_component(event)

# Write the calendar to a file
with open('events.ics', 'wb') as f:
    f.write(cal.to_ical())