import sys
import praw
from settings import *
from database import init_db, connection
from models import Users
from praw.models.reddit.comment import Comment
from praw.models.reddit.more import MoreComments
from praw.models.comment_forest import CommentForest


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
        authors = get_all_authors_from_submission(submission)
        authors.append(submission.author.name)
        unique_authors = list(set(authors))
        data = [{'username': unique_author, 'saved': False} for unique_author in unique_authors]
        query = Users.__table__.insert(prefixes=["OR REPLACE"])
        connection.execute(query, data)
        post_number += 1
    connection.close()


total_authors = 0


def get_all_authors_from_submission(submission):
    all_parent_comments = submission.comments.list()  # Get all nested comments as well, in a flattened list
    global total_authors
    total_authors = 0
    all_comments = get_all_nested_replies_from_comment_recursively(all_parent_comments)
    return all_comments


def get_all_nested_replies_from_comment_recursively(comments):
    all_comments = []
    for comment in comments:
        if isinstance(comment, Comment):
            if comment and comment.author and comment.author.name:
                global total_authors
                total_authors += 1
                if total_authors % 100 == 0:
                    print(f"Total authors extracted from this thread: {total_authors}")
                all_comments.append(comment.author.name)
        if isinstance(comment, MoreComments):
            all_comments.extend(get_all_nested_replies_from_comment_recursively(comment.comments()))
        if isinstance(comment, CommentForest):
            all_comments.extend(get_all_nested_replies_from_comment_recursively(comment.list()))
    return all_comments


if __name__ == '__main__':
    SEARCH_LIMIT = 3
    reddit = authenticate(user_agent, app_key, app_secret, username, password)
    scrape(reddit)
