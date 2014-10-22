'''
 This is based on the EchoBot example from sleekxmpp.com/getting_started/echobot.html

 Itended scope:
  This class should simply establish single or MUC sessions and communicate messages to and from core
  Eventually all sessions should be OTR
'''
import pyasn1
import pyasn1_modules
from sleekxmpp import ClientXMPP
from sleekxmpp.exceptions import IqError, IqTimeout

class xmppHandler(ClientXMPP):
  def __init__(self, jid, password):
    ClientXMPP.__init__(self, jid, password)
    
    # Setup and register plugins. Order does not matter.
    self.register_plugin('xep_0030') # Service Discovery
    self.register_plugin('xep_0004') # Data Forms
    self.register_plugin('xep_0060') # PubSub
    self.register_plugin('xep_0199') # XMPP Ping

    # Setup individual handlers
    self.add_event_handler("session_start", self.start)
    self.add_event_handler("message", self.messageIn)

  def start(self, event):
    self.send_presence()
    #TODO add exception handling to get_roster()
    self.get_roster()
    
        # Most get_*/set_* methods from plugins use Iq stanzas, which
        # can generate IqError and IqTimeout exceptions
        #
        # try:
        #     self.get_roster()
        # except IqError as err:
        #     logging.error('There was an error getting the roster')
        #     logging.error(err.iq['error']['condition'])
        #     self.disconnect()
        # except IqTimeout:
        #     logging.error('Server is taking too long to respond')
        #     self.disconnect()
      
  #TODO Expand method to hand additional message types and to pass input to core instead of echoing.
  def messageIn(self, msg):
    if msg['type'] in ('chat', 'normal'):
      return msg
  
  def messageOut(self, recipient, msg):
    self.send_message(recipient , msg)  
