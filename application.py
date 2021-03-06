import os
from wsgiref.simple_server import make_server
import unicodedata
from random import randrange
import requests



quotes = [u'Life isn\u2019t about getting and having, it\u2019s about giving and being.', u'Whatever the mind of man can conceive and believe, it can achieve.', u'Strive not to be a success, but rather to be of value.', u'Two roads diverged in a wood, and I\u2014I took the one less traveled by, And that has made all the difference.', u'I attribute my success to this: I never gave or took any excuse.', u'You miss 100% of the shots you don\u2019t take.', u'I\u2019ve missed more than 9000 shots in my career. I\u2019ve lost almost 300 games. 26 times I\u2019ve been trusted to take the game winning shot and missed. I\u2019ve failed over and over and over again in my life. And that is why I succeed.', u'The most difficult thing is the decision to act, the rest is merely tenacity.', u'Every strike brings me closer to the next home run.', u'Definiteness of purpose is the starting point of all achievement.', u'We must balance conspicuous consumption with conscious capitalism.', u'Life is what happens to you while you\u2019re busy making other plans.', u'We become what we think about.', u'14.Twenty years from now you will be more disappointed by the things that you didn\u2019t do than by the ones you did do, so throw off the bowlines, sail away from safe harbor, catch the trade winds in your sails.  Explore, Dream, Discover.', u'15.Life is 10% what happens to me and 90% of how I react to it.', u'The most common way people give up their power is by thinking they don\u2019t have any.', u'The mind is everything. What you think you become.', u'The best time to plant a tree was 20 years ago. The second best time is now.', u'An unexamined life is not worth living.', u'Eighty percent of success is showing up.', u'Your time is limited, so don\u2019t waste it living someone else\u2019s life.', u'Winning isn\u2019t everything, but wanting to win is.', u'I am not a product of my circumstances. I am a product of my decisions.', u'Every child is an artist.  The problem is how to remain an artist once he grows up.', u'You can never cross the ocean until you have the courage to lose sight of the shore.', u'I\u2019ve learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel.', u'Either you run the day, or the day runs you.', u'Whether you think you can or you think you can\u2019t, you\u2019re right.', u'The two most important days in your life are the day you are born and the day you find out why.', u'Whatever you can do, or dream you can, begin it.  Boldness has genius, power and magic in it.', u'The best revenge is massive success.', u'People often say that motivation doesn\u2019t last. Well, neither does bathing.  That\u2019s why we recommend it daily.', u'Life shrinks or expands in proportion to one\u2019s courage.', u'If you hear a voice within you say \u201cyou cannot paint,\u201d then by all means paint and that voice will be silenced.', u'There is only one way to avoid criticism: do nothing, say nothing, and be nothing.', u'Ask and it will be given to you; search, and you will find; knock and the door will be opened for you.', u'The only person you are destined to become is the person you decide to be.', u'Go confidently in the direction of your dreams.  Live the life you have imagined.', u'When I stand before God at the end of my life, I would hope that I would not have a single bit of talent left and could say, I used everything you gave me.', u'Few things can help an individual more than to place responsibility on him, and to let him know that you trust him.', u'Certain things catch your eye, but pursue only those that capture the heart.', u'Believe you can and you\u2019re halfway there.', u'Everything you\u2019ve ever wanted is on the other side of fear.', u'We can easily forgive a child who is afraid of the dark; the real tragedy of life is when men are afraid of the light.', u'Teach thy tongue to say, \u201cI do not know,\u201d and thous shalt progress.', u'Start where you are. Use what you have.  Do what you can.', u'When I was 5 years old, my mother always told me that happiness was the key to life.  When I went to school, they asked me what I wanted to be when I grew up.  I wrote down \u2018happy\u2019.  They told me I didn\u2019t understand the assignment, and I told them they didn\u2019t understand life.', u'Fall seven times and stand up eight.', u'When one door of happiness closes, another opens, but often we look so long at the closed door that we do not see the one that has been opened for us.', u'Everything has beauty, but not everyone can see.', u'How wonderful it is that nobody need wait a single moment before starting to improve the world.', u'When I let go of what I am, I become what I might be.', u'Life is not measured by the number of breaths we take, but by the moments that take our breath away.', u'Happiness is not something readymade.  It comes from your own actions.', u'If you\u2019re offered a seat on a rocket ship, don\u2019t ask what seat! Just get on.', u'First, have a definite, clear practical ideal; a goal, an objective. Second, have the necessary means to achieve your ends; wisdom, money, materials, and methods. Third, adjust all your means to that end.', u'If the wind will not serve, take to the oars.', u'You can\u2019t fall if you don\u2019t climb.  But there\u2019s no joy in living your whole life on the ground.', u'We must believe that we are gifted for something, and that this thing, at whatever cost, must be attained.', u'Too many of us are not living our dreams because we are living our fears.', u'Challenges are what make life interesting and overcoming them is what makes life meaningful.', u'If you want to lift yourself up, lift up someone else.', u'I have been impressed with the urgency of doing. Knowing is not enough; we must apply. Being willing is not enough; we must do.', u'Limitations live only in our minds.  But if we use our imaginations, our possibilities become limitless.', u'You take your life in your own hands, and what happens? A terrible thing, no one to blame.', u'What\u2019s money? A man is a success if he gets up in the morning and goes to bed at night and in between does what he wants to do.', u'I didn\u2019t fail the test. I just found 100 ways to do it wrong.', u'In order to succeed, your desire for success should be greater than your fear of failure.', u'A person who never made a mistake never tried anything new.', u'The person who says it cannot be done should not interrupt the person who is doing it.', u'There are no traffic jams along the extra mile.', u'It is never too late to be what you might have been.', u'You become what you believe.', u'I would rather die of passion than of boredom.', u'A truly rich man is one whose children run into his arms when his hands are empty.', u'It is not what you do for your children, but what you have taught them to do for themselves, that will make them successful human beings.', u'If you want your children to turn out well, spend twice as much time with them, and half as much money.', u'Build your own dreams, or someone else will hire you to build theirs.', u'The battles that count aren\u2019t the ones for gold medals. The struggles within yourself\u2013the invisible battles inside all of us\u2013that\u2019s where it\u2019s at.', u'Education costs money.  But then so does ignorance.', u'I have learned over the years that when one\u2019s mind is made up, this diminishes fear.', u'It does not matter how slowly you go as long as you do not stop.', u'If you look at what you have in life, you\u2019ll always have more. If you look at what you don\u2019t have in life, you\u2019ll never have enough.', u'Remember that not getting what you want is sometimes a wonderful stroke of luck.', u'You can\u2019t use up creativity.  The more you use, the more you have.', u'Dream big and dare to fail.', u'Our lives begin to end the day we become silent about things that matter.', u'Do what you can, where you are, with what you have.', u'If you do what you\u2019ve always done, you\u2019ll get what you\u2019ve always gotten.', u'Dreaming, after all, is a form of planning.', u'It\u2019s your place in the world; it\u2019s your life. Go on and do all you can with it, and make it the life you want to live.', u'You may be disappointed if you fail, but you are doomed if you don\u2019t try.', u'Remember no one can make you feel inferior without your consent.', u'Life is what we make it, always has been, always will be.', u'The question isn\u2019t who is going to let me; it\u2019s who is going to stop me.', u'When everything seems to be going against you, remember that the airplane takes off against the wind, not with it.', u'It\u2019s not the years in your life that count. It\u2019s the life in your years.', u'Change your thoughts and you change your world.', u'Either write something worth reading or do something worth writing.', u'Nothing is impossible, the word itself says, \u201cI\u2019m possible!\u201d', u'The only way to do great work is to love what you do.', u'If you can dream it, you can achieve it.']

def generate_random_qoute(quotes):
    total_quotes = len(quotes)
    random_index = randrange(0, total_quotes)
    quote = quotes[random_index]
    q = unicodedata.normalize('NFKD', quote).encode('ascii','ignore')
    return q

def they_said_so():
    return '<html><span style="z-index:50;font-size:0.9em;"><img src="https://theysaidso.com/branding/theysaidso.png" height="20" width="20" alt="theysaidso.com"/><a href="https://theysaidso.com" title="Powered by quotes from theysaidso.com" style="color: #9fcc25; margin-left: 4px; vertical-align: middle;">theysaidso.com</a></span>></html>'

def get_quote_api(cat):
    url = 'http://quotes.rest/qod.json?category=' + cat
    response = requests.get(url)
    if response.status_code != requests.codes.ok:
        return generate_random_qoute(quotes)
    data = response.json()
    quote = data['contents']['quotes'][0]['quote']
    q = unicodedata.normalize('NFKD', quote).encode('ascii','ignore')
    return q


def application(environ, start_response):
    path = environ['PATH_INFO']
    response = generate_random_qoute(quotes)
    if path == '/qod':
        response = get_quote_api()
    elif path == '/inspire':
        response = get_quote_api('inspire')
    elif path == '/management':
        response = get_quote_api('management')
    elif path == '/sports':
        response = get_quote_api('sports')
    elif path =='/life':
        response = get_quote_api('life')
    elif path == '/funny':
        response = get_quote_api('funny')
    elif path == '/love':
        response = get_quote_api('love')    
    elif path == '/art':
        response = get_quote_api('art')   
    elif path == '/students':
        response = get_quote_api('students')
    elif path == '/theysaidso':
        response = they_said_so()

    status = '200 OK'
    headers = [('Content-type', 'text/plain')]

    start_response(status, headers)
    return [response]


if __name__ == '__main__':
    httpd = make_server('', 8000, application)
    print("Serving on port 8000...")
    httpd.serve_forever()
