#!/usr/bin/env python

from __future__ import print_function

import sys
import logging
import time


# Configure the logger
logging.basicConfig(level=logging.DEBUG)

class MyApp:
    """A toy app based on a fun math trick"""

    def __init__(self):
        self.n_loops = 0
        self.ponder = True

    def run(self):
        """Loop forever"""

        msg = """Let's play a game! Think of a number between 0 and 999, where no digit appears more than once.
For example, '123' is OK, but '121' is not. Got it? Reverse the number (e.g., if you had "123" the reverse is "321"). 
Now, calculate the difference between them. If you enter the last digit of that difference, I'll guess the other(s).
"""
        print(msg)

        try:
            self._run()
            print("Did I get that right? Think it was luck? Keep playing, or hit crtl-c to quit.\n")
            while True:
                self._run()
        except KeyboardInterrupt:
            print("\n\nThanks for playing!\n")

    def _run(self):
        """Run one loop iteration. Return True if we should keep going, or False to quit"""

        # Get the user input
        n = input("round {}) ".format(self.n_loops))
        self.n_loops += 1

        if not self.validate_input(n): return
        n = int(n) # make sure we're not a string

        # Ponder
        if self.ponder:
            print("Let me think on that", end='', flush=True)
            for _ in range(6):
                time.sleep(0.4)
                print('.', end='', flush=True)
            print(" ", end='')

        # Make the guess
        print( self.guess(n) )
        print()

    def validate_input(self, n):
        # Make sure it looks good
        if len(n) != 1:
            logging.error("'{}' should be a single character!".format(n))
            return False
        try:
            n = int(n)
        except ValueError:
            logging.error("'{}' doesn't look like a number!".format(n))
            return False

        return True

    def guess(self, n):
        return (9,) if n == 9 else (9-n, 9)


def main():
    myapp = MyApp()
    myapp.run()
    pass


if __name__ == '__main__':
    sys.exit( main() )