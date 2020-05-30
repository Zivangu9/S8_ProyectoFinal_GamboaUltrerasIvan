import pymysql
class Connection:
   __instance = None
   db = None
   cursor = None
   @staticmethod 
   def getInstance():
      """ Static access method. """
      if Connection.__instance == None:
         Connection()
      return Connection.__instance
   def __init__(self):
      """ Virtually private constructor. """
      self.db = pymysql.connect("localhost","usuario","CjxR9g4QLSxeSps7","book_collection")
      self.cursor = self.db.cursor()
      if Connection.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         Connection.__instance = self