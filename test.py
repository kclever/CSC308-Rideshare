import pytest

def greet(name):
   if isinstance(name, list) == True:
      returnVar = "Hello"
      for n in name:
         if (name[len(name) -1] == n):
            if len(name) == 2:
               returnVar = returnVar + " and "
            else:
               returnVar = returnVar + ", and "
         else:
            returnVar = returnVar + ", "
         returnVar = returnVar + n
      returnVar = returnVar + "."
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
