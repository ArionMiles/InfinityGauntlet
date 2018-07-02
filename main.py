import random
import textwrap
from database import init_db, db_session, connection
from models import Users
from settings import *
from scraper import authenticate
from sqlalchemy import and_

reddit = authenticate(user_agent, app_key, app_secret, username, password)


def snap():
    init_db()
    all_users = []
    user_data = Users.query.filter(Users.saved == False).all()
    user_count = db_session.query(Users).count()
    print(user_count)
    for user in user_data:
        name = user.username
        # print(name)
        all_users.append(name)
    numbers_to_balance = int(user_count / 2)
    print(numbers_to_balance)
    # Select half users at random
    ill_fated = random.sample(all_users, numbers_to_balance)
    db_session.close()
    ban(ill_fated)


def ban(ill_fated):
    ban_message = textwrap.dedent("""
    Hear me and rejoice! You have had the great privilege of being saved by the great titan. 
    You may think this is suffering....no! It is salvation. The subreddit scales...tip toward balance 
    because of your sacrifice. Smile...for even in death, you have become children of Thanos!

    Join the others on /r/SoulWorld

    ^(This action was performed by a bot.)
    ^(for feedback, bug reports or just to say thanks! The code is on )[^github](https://github.com/ArionMiles/InfinityGauntlet))
    """)

    ban_reason = "To bring balance to the sub"

    reddit = authenticate(user_agent, app_key, app_secret, username, password)
    for user in ill_fated:
        reddit.subreddit(subreddit).banned.add(user, ban_message=ban_message, ban_reason=ban_reason,
                                               duration=days_until_a4_releases)
        query = Users.__table__.update().where(and_(Users.username == user, Users.saved == False)).values(saved=True)
        connection.execute(query)
        print(f"{user} was snapped out of existence.")
    connection.close()


if __name__ == '__main__':
    try:
        snap()
        print("This day extracted a heavy toll, but it's done!\nNow you watch the sun rise on a greatful subreddit :)")
    except KeyboardInterrupt:
        connection.close()
