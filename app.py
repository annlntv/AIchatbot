#imports
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

russianBot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(russianBot)
trainer.train("chatterbot.corpus.russian")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")

def get_bot_response():
    userText = request.args.get('msg')
    return str(russianBot.get_response(userText))

if __name__ == "__main__":
    app.run()