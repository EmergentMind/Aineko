import settings

class Console:
  def __init__(self):
    self.console_prompt = settings.TEXT_ICON
    self.input = False
    
  def listener(self):
    self.Output(settings.INITIAL_GREETING)
    
    while True:
      self.input = self.getInput()
     
      if (self.ExitCheck(self.input)):
        self.Output("Goodbye.")
        break
      elif (self.input):
        self.Output("Thanks for your input.")
        continue
      else:
        self.Output("Did you say something?")
        continue
        
  def getInput(self):
    userInput = input(self.console_prompt)
    return userInput
     
  def Output(self, response):
    print (response)

  def ExitCheck(self, userInput):
    if (self.input == settings.COMMAND_INITIATOR + "exit"):
      return True
    else:
      return False 

class Core:

  def __init__(self):
    self.Console = Console()  
    self.Console.listener()
