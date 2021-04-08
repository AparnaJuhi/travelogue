from flask import render_template
from create_app import create_app

app = create_app()

@app.route('/')
def hello_world():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)

