from flask import Flask, render_template
from app.api.views import json_blueprint
from app.post.views import post_blueprint

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False


app.register_blueprint(post_blueprint)
app.register_blueprint(json_blueprint)


@app.route('/tag')
def home_4():
    return render_template('tag.html')


@app.route('/book')
def home_6():
    return render_template('bookmarks.html')


if __name__ == '__main__':
    app.run(debug=True)