
from flask import Flask, jsonify

application = Flask(__name__)

actions = [
    {
        'id': 1,
        'title': u'Assets created',
        'description': u'A CC Assets has been created.',
        'done': False
    },
    {
        'id': 2,
        'title': u'Assets modified',
        'description': u'A CC Assets has been modified.',
        'done': False
    },
    {
        'id': 3,
        'title': u'Assets removed',
        'description': u'A CC Assets has been removed.',
        'done': False
    }
]

@application.route('/actions', methods=['GET'])
def get_actions():
    return jsonify({'actions': actions})

@application.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    application.run()
