from dotenv import load_dotenv
import os
import praw

def reddit_init():
    reddit = praw.Reddit(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("SECRET_KEY"),
        password=os.getenv("PASSWORD"),
        user_agent="testing",
        username=os.getenv("USERNAME"),
    )
    return reddit

def daily_comms(reddit, symbol_list):
    com_dict = {}
    data =[]
    subreddit = reddit.subreddit('wallstreetbets')
    submission = next(subreddit.hot(limit = 1))
    submission.comments.replace_more(limit=0)

    for comment in submission.comments.list():
        if isinstance(comment, praw.models.MoreComments):
            continue
        data.extend(comment.body.split())

    for word in data:
            if word.upper() in symbol_list and len(word)>1:
                    if word.upper() in com_dict:
                        com_dict[word.upper()] += 1
                    else:
                        com_dict[word.upper()] = 1

    return dict(sorted(com_dict.items(), key = lambda item:item[1]))
