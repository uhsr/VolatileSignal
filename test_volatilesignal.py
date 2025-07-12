# test_volatilesignal.py
"""
Tests for VolatileSignal module.
"""

import unittest
from volatilesignal import VolatileSignal

class TestVolatileSignal(unittest.TestCase):
    """Test cases for VolatileSignal class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VolatileSignal()
        self.assertIsInstance(instance, VolatileSignal)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VolatileSignal()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
