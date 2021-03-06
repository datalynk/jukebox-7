# Brandon Edens
# 2010-01-21
# Copyright (C) 2009 Brandon Edens <brandon@as220.org>
"""
"""

###############################################################################
## Imports
###############################################################################

from django.test import TestCase


###############################################################################
## Classes
###############################################################################

class SimpleTest(TestCase):

    def setUp(self):
        """
        """
        pass

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)


###############################################################################
## Statements
###############################################################################

__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}

