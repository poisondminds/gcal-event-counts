# gcal-event-counts
A handy little tool that shows you how many events you have on a weekly basis

## Setup
* Python 3.x
* `pip`
* Google Calendar Python API Tools (Step 1 and 2 [here](https://developers.google.com/calendar/quickstart/python)). Make sure to save `credentials.json` file in the same directory as this tool.
* Install the following required Python libraries
```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install google-auth-oauthlib
pip install python-dateutil
```
* Run tool once to get logged in with Google

## Usage
```bash
python generate_weekly_counts.py <start_date>
```
where `start_date` is in the format `yyyy-mm-dd`.

You'll then get a CSV output that you can do whatever you'd like with. Chart it out in Excel or Google Sheets.
