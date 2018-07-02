# Rename this file to `settings.py` in deployment
import datetime

# Days until Avengers 4 releases (26th Apr, 2019)
date_format = "%m/%d/%Y" #MM/DD/YYYY
Avengers4_release_date = datetime.date(2019, 4, 26)
today = datetime.date.today()
no_of_days = Avengers4_release_date - today
days_until_a4_releases = no_of_days.days

# reddit app
username = 'yourUsername'
password = 'yourPassowrd'
app_key = 'app_key'
app_secret = 'app_secret'

# bot account
access_token = '3...R'
refresh_token = '3...m'

subreddit = 'thanosdidnothingwrong'
user_agent = ('Gauntlet, v0.1. Brings balance to the sub'
              '(by /u/Arion_Miles)')