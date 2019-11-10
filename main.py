import praw
import pyttsx3


def get_link():
    print('hello0')


def get_data():
    print('hello')


def get_comments():
    print('hello2')

def master_string(title, body, author, comments):
    if body == '':
        body = 'Not Available'
    string = f"TITLE OF POST: {title}\n AUTHOR: {author}\nBODY: {body}\nCOMMENTS: {comments}"
    return string


def say_post():
    print('hello4')


def main():
    print('hello5')


main()
