from flask import Flask

from api.prediction import inference


app = Flask(__name__)
app.register_blueprint(inference)

if __name__ == '__main__':
    app.run(debug=True)
