class Winner(object):
    """Winner class"""
    def __init__(self):
      self.m_select1 = ""
      self.m_select2 = ""
   
    def getInputFromUsers(self):
      print ("=======================================================")
      print ("Hey Arjun !! , Lets Play Rock Paper and Scissors !!!!")
      print ("=======================================================")
      print ("=============================================================")
      self.m_select1 = input("Arjun, What are you Rock, Paper, Scissor ? : ")
      print ("=============================================================")
      self.m_select2 = input("Harish, What are you Rock, Paper, Scissor ? : ")
      print ("=============================================================")
      self.m_select1 = self.m_select1.upper()
      self.m_select2 = self.m_select2.upper()

    def deterMineWinner(self):
      if ((self.m_select1 == "R" or self.m_select2 == "R") and (self.m_select1 == "S" or self.m_select2 == "S") ):
              if (self.m_select1 == "R"):
                  print("=========================")
                  print("Arjun is the winner!!!!!!")
                  print("=========================")
              else:
                 print("Harish is the winner")
      elif ((self.m_select1 == "P" or self.m_select2 == "P") and (self.m_select1 == "S" or self.m_select2 == "S") ):
              if (self.m_select1 == "S"):
                 print("Arjun is the winner")
              else:
                 print("Harish is the winner")

      elif ((self.m_select1 == "P" or self.m_select2 == "P") and (self.m_select1 == "R" or self.m_select2 == "R") ):
               if (self.m_select1 == "P"):
                  print("Arjun is the winner")
               else:
                  print("Harish is the winner")
   
      else:
          # Since this is a simple game... Value check is not done for RPS.I believe you will give right input.   
          print("It is a Tie !!... ")

