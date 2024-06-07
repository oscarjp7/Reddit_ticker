from dotenv import load_dotenv
import os
import praw
from DATACONTEXT.findticker import find_tickers_with_context, find_tickers

not_stocks=['IT','FOR','ON','YOU','SO','BE','UP','GOOD','ARE','DAY','OR','ALL','CAN','ME','DO','BY','GO','OUT',
              'AS','BACK','OPEN','SEE','PUMP','NOW','BIG','HAS','NEXT','EOD','AN','AM','CASH','PLAY','HEAR','SAY',
              'LOW','TOP','LOVE','ANY','HE','TWO','RH','CCL','HOPE','SNOW','GLAD','EVER','AI','LIVE','BILL','NET',
              'IMO','BRO','POST','PR','HUGE','PEP','NICE','CARE','DD','LIFE','GAME','ARE','CARS','ET','APP','SAFE',
              'COP','ELSE','SPOT','MIN','COST','TECH','GROW','VERY','REAL','WELL','PAY','FREE','LOAN','BEST','NOTE',
              'FUND','MIND','RUN','ADD','WAVE']

def reddit_init():
    load_dotenv()
    reddit = praw.Reddit(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("SECRET_KEY"),
        password=os.getenv("PASSWORD"),
        user_agent="testing",
        username=os.getenv("USERNAME"),
    )
    return reddit

def wsb_daily_comms(reddit, count):
    com_dict = {}
    data =[]
    subreddit = reddit.subreddit('wallstreetbets')
    submissions = subreddit.hot(limit = 3)
    submission = None
    for sub in submissions:
        if 'Daily Discussion' in sub.title:
            print(sub.title)
            submission = sub
            break
    if submission:
        submission.comments.replace_more(limit=count)

        for comment in submission.comments.list():
            if isinstance(comment, praw.models.MoreComments):
                continue
            data.extend(find_tickers_with_context(comment.body))

        for word in data:
                    if word.upper() in com_dict:
                        com_dict[word.upper()] += 1
                    else:
                        com_dict[word.upper()] = 1

        return dict(sorted(com_dict.items(), key = lambda item:item[1]))

def title_post_ticker(reddit, sub_list, symbol_list, post_count):
    word_dict ={}
    for sub in sub_list:
        subreddit = reddit.subreddit(sub)
        submissions = subreddit.hot(limit = post_count)

        data = []
        for submission in submissions:
            if submission.title:
                data.extend(find_tickers(submission.title))
            if submission.selftext:
                data.extend(find_tickers(submission.selftext))
            # data.extend(submission.title.split())
            # data.extend(submission.selftext.split())

        for word in data:
            if word.upper() in word_dict:
                word_dict[word.upper()] += 1
            else:
                word_dict[word.upper()] = 1

    return dict(sorted(word_dict.items(), key = lambda item:item[1]))
