import discord 
from replit import db


def add_message(message):

  if "messages" in db.keys():
    messages = db["messages"]
    messages.append(message)
    db["messages"] = message
  
  else:
    db["encouragements"] = [message]
    