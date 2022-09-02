from flask import Flask

love = Flask(__name__)

@love.route('/')
def love_note():
    return 'I LOVE YOU SKWINKLE <3'