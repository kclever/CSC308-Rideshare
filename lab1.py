import pytest 

def greet(name):
    outstr = ""
    normalNames = []
    shoutNames = []
    if(name == None):
        return "Hello, my friend."
    if(isinstance(name,str)):
        if(name.isupper()):
          return "HELLO, {}!".format(name)
        else:
            return "Hello, {}.".format(name)
    splitList = []
    for i in range(len(name)):
        if (name[i][0] == "'"):
            pass
        else:
            split = name[i].split(", ")
            for i in range(len(split)):
                splitList.append(split[i])
    print(splitList)
    for i in range(len(splitList)):
        if (splitList[i].isupper()):
            shoutNames.append(splitList[i])
        else:
            normalNames.append(splitList[i])
    print(shoutNames)
    if(len(normalNames) == 2):
        outstr = "Hello, {} and {}.".format(normalNames[0], normalNames[1])
    else:
        tempstr = "Hello"
        for i in range(len(normalNames)-1):
            tempstr = tempstr + ", " + normalNames[i]
        tempstr = tempstr + ", and " + normalNames[len(normalNames)-1] + "."
        outstr = tempstr

    if (len(shoutNames) > 0):
        tempstr = " AND HELLO"
        if (len(shoutNames) == 1):
            tempstr = tempstr + " " + shoutNames[0]
        else:
            for i in range(len(shoutNames)-1):
                tempstr = tempstr + ", " + shoutNames[i]
            tempstr = tempstr + ", AND " + shoutNames[len(shoutNames)-1] + "."
        outstr = outstr + tempstr + "!"
    return outstr

def test_name():
    greeting = greet("Bob")
    assert greeting == "Hello, Bob."

def test_null():
    val = None
    greeting = greet(val)
    assert greeting == "Hello, my friend."

def test_caps():
    greeting = greet("JERRY")
    assert greeting == "HELLO, JERRY!"

def test_two_names():
    val = ["Jill", "Jane"]
    greeting = greet(val)
    assert greeting == "Hello, Jill and Jane."

def test_multiple_names():
    val = ["Amy", "Brian", "Charlotte"]
    greeting = greet(val)
    assert greeting == "Hello, Amy, Brian, and Charlotte."

def test_mix():
    val = ["Amy", "BRIAN", "Charlotte"]
    greeting = greet(val)
    assert greeting == "Hello, Amy and Charlotte. AND HELLO BRIAN!"

def test_camma():
    val = ["Bob", "Charlie, Dianne"]
    greeting = greet(val)
    assert greeting == "Hello, Bob, Charlie, and Dianne."

