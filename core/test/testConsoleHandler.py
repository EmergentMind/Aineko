import unittest
import core.settings
from core.console import ConsoleHandler

class ConsoleHandlerTestCase(unittest.TestCase):
  
  def setUp(self):
    self.ConsoleHandler = ConsoleHandler()

  def tearDown(self):
    self.ConsoleHandler.dispose()
    self.ConsoleHandler = None  
    
  def test_init(self):
    self.assertEqual(self.ConsoleHandler.console_prompt,
                     core.settings.PROMPT,
                     'console_prompt is not mapped to ConsoleHandler()')
    self.assertFalse(self.ConsoleHandler.userInput, 'ConsoleHandler.userInput is not initialized as False')
  
  def test_ExitCheckTrue(self):
    command = core.settings.COMMAND_INITIATOR + "exit"
    self.assertTrue( self.ConsoleHandler.ExitCheck(command) )

  def test_ExitCheckFalse(self):
    command = "exit"
    self.assertFalse( self.ConsoleHandler.ExitCheck(command) )

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()