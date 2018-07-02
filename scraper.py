import sys
import praw
from settings import *
from database import init_db, db_session
from models import Users

def authenticate(user_agent, app_key, app_secret, username, password):
    print("Authenticating...")
    try:
        reddit = praw.Reddit(user_agent=user_agent, client_id=app_key,
                            client_secret=app_secret, username=username,
                            password=password)
        username = reddit.user.me()
        print(f"Authenticated as {username}")
    except Exception as e:
        print(e)
        sys.exit(1)
    return reddit

def scrape(reddit):
    init_db()
    for submission in reddit.subreddit(subreddit).hot(limit=SEARCH_LIMIT):
        if not Users.query.filter(Users.username == submission.author.name).first():
            record = Users(username=submission.author.name)
            db_session.add(record)

        all_comments = submission.comments.list() #Get all nested comments as well, in a flattened list
        for comment in all_comments:
            try:
                if not Users.query.filter(Users.username == comment.author.name).first():
                    #Spare the authenticated user, because this is a hard choice and they have a strong will
                    if comment.author.name == username:
                        continue
                    record = Users(username=comment.author.name)
                    db_session.add(record)
                    db_session.commit()
            except AttributeError:
                continue

if __name__ == '__main__':
    SEARCH_LIMIT = 10
    reddit = authenticate(user_agent, app_key, app_secret, username, password)
    scrape(reddit)