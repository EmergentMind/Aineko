''' Initliaze and launch Aineko. '''

import logging
from optparse import OptionParser

from core.main import Processor
from IOHandlers.console import ConsoleHandler
from IOHandlers.xmpp import xmppHandler
import settings

# Setup the command line arguments.
OptionParser = OptionParser()

# Output verbosity options.
OptionParser.add_option('-q', '--quiet', help='set logging to ERROR',
                        action='store_const', dest='loglevel',
                        const=logging.ERROR, default=logging.INFO)
OptionParser.add_option('-d', '--debug', help='set logging to DEBUG',
                        action='store_const', dest='loglevel',
                        const=logging.DEBUG, default=logging.INFO)
OptionParser.add_option('-v', '--verbose', help='set logging to COMM',
                        action='store_const', dest='loglevel',
                        const=5, default=logging.INFO)

# XMPP options.
OptionParser.add_option('-n', '--noXMPP', help='set to stop Aineko from signing into XMPP',
                        action='store_const', dest='noXMPP',
                        const=True, default=False)
OptionParser.add_option("-j", "--jid", dest="jid",
                        help="JID to use for " + settings.XMPP_SERVER)
OptionParser.add_option("-p", "--password", dest="password",
                        help="password to use for " + settings.XMPP_SERVER)

options, args = OptionParser.parse_args()

# Setup logging.
logging.basicConfig(level=options.loglevel,
                    format='%(levelname)-8s %(message)s')


Processor = Processor()
Console = ConsoleHandler()
xmpp = False

# Start XMPP.
if options.noXMPP is False:
    Console.messageOut("Starting XMPP client.")

    if options.jid is None:
        options.jid = Console.messageIn("JabberID including domain: ", True)
    if options.password is None:
        options.password = Console.passwordIn("Password: ")

    xmpp = xmppHandler(options.jid, options.password)

    if xmpp.connect():
        xmpp.process(threaded=True)
        Console.messageOut("I am signed into " + xmpp.server + " as " + options.jid)
    else:
        Console.messageOut("I was unable to connect")
        xmpp = False

#IO Loop.
while True:
    userInput = Console.messageIn()

    if userInput is None and xmpp:
        userInput = xmpp.messageIn()

    response = Processor.handleInput(userInput)

    if response:
        Console.messageOut(response)
    if xmpp and xmpp.connect():
        xmpp.messageOut("tacollector@gmail.com", response)

    if Processor.shutDown is True:
        if xmpp:
            xmpp.disconnect(wait=True)
        break
