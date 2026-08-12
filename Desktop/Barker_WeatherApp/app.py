#Import libraries
from flask import Flask

#Initializing app
app = Flask(__name__)

#Setting home url and adding post method
@app.route('/', methods = ['GET','POST'])

def yo():
    return "YOOOOO"

if __name__ == "__main__":
    app.run()
