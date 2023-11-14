import string
import random


def random_username(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_signup(app):
    username = random_username("user_", 5)
    password = "test"
    app.james.ensure_user_exists(username, password)
    app.