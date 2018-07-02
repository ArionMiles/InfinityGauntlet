import sys
import praw
from settings import *
from database import init_db, connection
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
    print("Initializing database... (might take some time)")
    init_db()
    print("Database is setup successfully.")
    post_number = 1
    for submission in reddit.subreddit(subreddit).top(limit=SEARCH_LIMIT):
        print(f"Scraping contributors from thread (including all comments) number: {post_number}")
        all_comments = submission.comments.list()  # Get all nested comments as well, in a flattened list
        authors = [submission.author.name]
        for comment in all_comments:
            try:
                authors.append(comment.author.name)
            except AttributeError:
                continue
        unique_authors = list(set(authors))
        data = [{'username': unique_author, 'saved': False} for unique_author in unique_authors]
        query = Users.__table__.insert(prefixes=["OR REPLACE"])
        connection.execute(query, data)
        post_number += 1
    connection.close()

if __name__ == '__main__':
    SEARCH_LIMIT = 5
    reddit = authenticate(user_agent, app_key, app_secret, username, password)
    scrape(reddit)
