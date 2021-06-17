from uuid import uuid4

from flask import Flask


app = Flask(__name__)


@app.route('/data')
def data():
    def get_data():
        rows = []
        for i in range(10_000_000):
            rows.append(str(uuid4()))
        return '\n'.join(rows)

    res = get_data()
    return app.response_class(res, mimetype='text/plain')


if __name__ == '__main__':
    app.run()
