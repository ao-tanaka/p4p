import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def mainmenu():

    return """
    <html>
    <body>
    <center><h1>Hello World! from AWS CodeDeploy.</h1><br/>
    <h2>Piper, CI/CD Lab11-3</h2>
    <iframe src="https://calendar.google.com/calendar/embed?src=f9ef0c49fac30617cc63be0a1387819006298c747f350ca0650dfd52279d5ea6%40group.calendar.google.com&ctz=Asia%2FTokyo" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>
    </body>
    </html>"""

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=80)
