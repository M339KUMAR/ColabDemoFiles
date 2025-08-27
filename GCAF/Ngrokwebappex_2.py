!pip install flask pyngrok

#!mkdir ./templates/
#templates/index.html
#%%writefile templates/index.html

from flask import Flask, render_template
from pyngrok import ngrok, conf
import threading

# Create Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!🙂👍😊 This is running from Google Colab'
    #render_template("index.html")

def run_app():
    app.run(host="0.0.0.0", port=5000)

conf.get_default().auth_token = "2yIOvcZEaVwrAIECmtUofV0csZg_7XwsyKaB9TRqCGTQDfYvf"

import threading
thread = threading.Thread(target=run_app)
thread.start()

public_url = ngrok.connect(5000)
print(" * ngrok tunnel:", public_url)
