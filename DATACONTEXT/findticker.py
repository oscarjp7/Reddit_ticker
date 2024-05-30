import spacy
from DATAPREP.loaddata import get_ticker_and_name, get_nasdaq, get_symbol_list

nlp=spacy.load("en_core_web_sm")

df = get_nasdaq()
ticker_dict = get_ticker_and_name(df)
symbol_list = get_symbol_list(df)
context_keywords = ['stock', 'price', 'buy', 'sell', 'market', 'shares']

not_stocks=['IT','FOR','ON','YOU','SO','BE','UP','GOOD','ARE','DAY','OR','ALL','CAN','ME','DO','BY','GO','OUT',
              'AS','BACK','OPEN','SEE','PUMP','NOW','BIG','HAS','NEXT','EOD','AN','AM','CASH','PLAY','HEAR','SAY',
              'LOW','TOP','LOVE','ANY','HE','TWO','RH','CCL','HOPE','SNOW','GLAD','EVER','AI','LIVE','BILL','NET',
              'IMO','BRO','POST','PR','HUGE','PEP','NICE','CARE','DD','LIFE','GAME','ARE','CARS','ET','APP','SAFE',
              'COP','ELSE','SPOT','MIN','COST','TECH','GROW','VERY','REAL','WELL','PAY','FREE','LOAN','BEST','NOTE',
              'FUND','MIND','RUN','ADD','WAVE','MOVE','TRUE','BIT','MAIN','KIND','FIVE','GAIN','VS','GUT','EU',
              'UK','PRE',' UPS','SELF','PPL','FATS','KEY','FOUR','TALK','MATH','EDIT','LAND','RENT','VIEW','KIDS',
              'CAR','HI','VIEW','MAX','LOT','TOWN','UNIT']

def find_tickers(text):
    tickers = []
    doc = nlp(text)
    for token in doc:
        word = token.text
        if word.upper() in symbol_list and len(word) > 1 and word.upper() not in not_stocks:
            tickers.append(word.upper())
        elif word.lower() in ticker_dict:
            tickers.append(ticker_dict[word.lower()])
    return tickers

def is_financial_context(text):
    for keyword in context_keywords:
        if keyword in text.lower():
            return True
    return False

def find_tickers_with_context(text):
    tickers = []
    sentences = text.split('.')
    # only add if financial context in sentence
    # for sentence in sentences:
    #     if is_financial_context(sentence):
    #         tickers.extend(find_tickers(sentence))
    for sentence in sentences:
        tickers.extend(find_tickers(sentence))
    return tickers
