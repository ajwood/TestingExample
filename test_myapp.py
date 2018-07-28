import unittest

import myapp

class TestMyApp(unittest.TestCase):

    def setUp(self):
        self.app = myapp.MyApp()


    def test_guess(self):
        # Guess a bunch of numbers
        got = [ self.app.guess(x) for x in range(1,10) ]
        self.assertEqual( self.app.guess(1), (8,9), 'Guess 1' )
        self.assertEqual( self.app.guess(2), (7,9), 'Guess 2' )
        self.assertEqual( self.app.guess(3), (6,9), 'Guess 3' )
        self.assertEqual( self.app.guess(4), (5,9), 'Guess 4' )
        self.assertEqual( self.app.guess(5), (4,9), 'Guess 5' )
        self.assertEqual( self.app.guess(6), (3,9), 'Guess 6' )
        self.assertEqual( self.app.guess(7), (2,9), 'Guess 7' )
        self.assertEqual( self.app.guess(8), (1,9), 'Guess 8' )
        self.assertEqual( self.app.guess(9), (9,),  'Guess 9' )

    def test_validate_input(self):
        for valid in ('1', '3', '7', '4', '8'):
            self.assertTrue( self.app.validate_input(valid), "Input '{}' is valid input".format(valid) )

        for invalid in ('123', 'a', 'xyz'):
            self.assertFalse( self.app.validate_input(invalid), "Input '{}' is invalid input".format(invalid) )

    def tearDown(self):
        pass
