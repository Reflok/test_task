from uuid import uuid4

from flask import Flask


app = Flask(__name__)


@app.route('/data')
def data():
    def get_data():
        rows = []
        for _ in range(10_000_000 - 1): # removing unused var. 'i' technically reduces memory usage :D
            yield str(uuid4())+'\n' # send small parts of data instead of loading the entire thing in memory
        yield str(uuid4())

    return app.response_class(get_data(), mimetype='text/plain')


if __name__ == '__main__':
    app.run()
