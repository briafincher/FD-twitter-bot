import my_markov
import twitter
import os
import sys


def tweet(chains):
    # Use Python os.environ to get at environmental variables
    # Note: you must run `source secrets.sh` before running this file
    # to make sure these environmental variables are set.

    # print (api.GetUserTimeline(count=1)[0]).text
    api.PostUpdate(my_markov.make_text(chains))


def get_tweets():

    statuses = api.GetHomeTimeline(count=100)

    return " ".join([s.text for s in statuses])


chains = {}
input_text = ""
api = twitter.Api(consumer_key=os.environ["TWITTER_CONSUMER_KEY"],
                  consumer_secret=os.environ["TWITTER_CONSUMER_SECRET"],
                  access_token_key=os.environ["TWITTER_ACCESS_TOKEN_KEY"],
                  access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"])

input_text = get_tweets()

# Get a Markov chain
chains = my_markov.make_chains(input_text, int(sys.argv[1]), chains)

tweet(chains)
