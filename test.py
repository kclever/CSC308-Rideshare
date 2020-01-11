import pytest

def greet(name):
   if isinstance(name, list) == True:
      shoutNames = []
      regNames = []
      quoteNames= []
      for n in name:
         if n.isupper() == True:
            shoutNames.append(n)
         else:
            if "," in n:
               if "\"" in n:
                  n = n.replace('"', '')
                  regNames.append(n)
               else:
                  listSplit = n.split(', ')
                  for l in listSplit:
                     regNames.append(l)
            else:
               regNames.append(n)
      returnVar = "Hello"

      for n in regNames:
         if (regNames[len(regNames) -1] == n):
            if len(regNames) == 2:
               returnVar = returnVar + " and "
            else:
               returnVar = returnVar + ", and "
         else:
            returnVar = returnVar + ", "
         returnVar = returnVar + n
      returnVar = returnVar + "."
      if len(shoutNames) > 0:
         returnVar = returnVar + " AND HELLO "
         for n in shoutNames:
            returnVar = returnVar + n
         returnVar = returnVar + "!"
      return returnVar
   else:
      if len(name) != 0:
         if name.isupper() == True:
            return "HELLO " + name + "!"
         return "Hello, " + name + "."
      else:
         return "Hello, my friend."


def test_req1():
   assert greet("Bob") == "Hello, Bob."

def test_req2():
   assert greet("") == "Hello, my friend."

def test_req3():
   assert greet("JERRY") == "HELLO JERRY!"

def test_req4():
   assert greet(["Jill", "Jane"]) == "Hello, Jill and Jane."

def test_req5():
   assert greet(["Amy", "Brian", "Charlotte"]) == "Hello, Amy, Brian, and Charlotte."

def test_req6():
   assert greet(["Amy","BRIAN", "Charlotte"]) == "Hello, Amy and Charlotte. AND HELLO BRIAN!"

def test_req7():
   assert greet(["Bob", "Charlie, Dianne"]) == "Hello, Bob, Charlie, and Dianne."

def test_req8():
   assert greet(["Bob", "\"Charlie, Dianne\""]) == "Hello, Bob and Charlie, Dianne."
