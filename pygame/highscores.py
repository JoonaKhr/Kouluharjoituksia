from pymongo import MongoClient
import passw
password = passw.PASSWORD
cluster = "mongodb+srv://grovetender:"+password+"@faygrove.c0zaa.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(cluster)

class Highscores:
    def __init__(self):
        highscores = client["HighscoresForOpSnowflake"]
        self.highs = highscores.Highscores
        self.col = highscores["Highscores"]

    def insertHighscore(self, name, score):
        self.col.insert_one({"name": name, "score": score})