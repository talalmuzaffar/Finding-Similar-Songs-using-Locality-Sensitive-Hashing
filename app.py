from flask import Flask

from similar_songs_lsh.views import index, analyse


app = Flask(__name__)

app.add_url_rule('/', view_func=index)
app.add_url_rule('/analyse', view_func=analyse, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)
