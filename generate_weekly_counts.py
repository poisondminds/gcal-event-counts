import gcal_service
import sys
from datetime import datetime
from datetime import timedelta

DATE_FORMAT = '%Y-%m-%d'
OUTPUT_FILE = 'weekly_counts.csv'
start = sys.argv[1]
print('Analyzing events since ' + start + ' ... ')

date_counts = []
start_date = datetime.strptime(start, DATE_FORMAT)

while start_date < datetime.utcnow():
    end_date = start_date + timedelta(days=7)

    events = gcal_service.events(start_date, end_date)

    date_counts.append((start_date, len(events)))
    print(start_date.strftime(DATE_FORMAT) + " - " + end_date.strftime(DATE_FORMAT) + ' -> ' + str(len(events)) + ' events')
    start_date = end_date

output_file = open(OUTPUT_FILE, 'w')

for date_count in date_counts:
    output_file.write(date_count[0].strftime(DATE_FORMAT) + "," + str(date_count[1]) + "\n")

output_file.close()

print('Done! Output written to ' + OUTPUT_FILE)
