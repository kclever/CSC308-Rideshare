import unittest
import stuff
#for commit

class MyTestCase(unittest.TestCase):
    def test_reqOne(self):
        inName = "Bob"
        output = stuff.greetName(inName)
        expectedout = "Hello, Bob."
        self.assertEqual(output, expectedout)

    def test_reqTwo(self):
        input = None
        out = stuff.greetNull(input)
        exout = "Hello, my friend."
        self.assertEqual(out, exout)

    def test_reqThree(self):
        input = "BOB"
        out = stuff.greetYell(input)
        exout = "HELLO BOB!"
        self.assertEqual(out, exout)

    def test_reqFour(self):
        input = ["Bob", "Bobby"]
        out = stuff.greetList(input)
        exout = "Hello, Bob and Bobby"
        self.assertEqual(out, exout)

    def test_reqFive(self):
        input = ["b", "a", "c"]
        out = stuff.greetThree(input)
        exout = "Hello, b, a, and c"
        self.assertEqual(out, exout)

    def test_reqSix(self):
        self.assertEqual("Hello, a and b. AND HELLO CAAA", stuff.greetSome(["a", "b", "CAAA"]))

    def test_reqSeven(self):
        self.assertEqual("Hello, Bob, Charlie, and Dianne", stuff.greet7(["Bob", "Charlie, Dianne"]))

    def test_reqEight(self):
        self.assertEqual("Hello, Bob and Charlie, Dianne", stuff.greetWeird(["Bob", "\"Charlie, Dianne\""]))

if __name__ == '__main__':
    unittest.main()
