from eventbrite import Eventbrite
from tok import secret
import pprint

token = secret()
eventbrite = Eventbrite(token)
pp = pprint.PrettyPrinter(indent=4)

def eb_api_query():
    # dictionary keys of argument are the fields we care about
    argument = {}

    # do something like this...
    # argument["location.address"] =


    #this line is to expand the venue field (necessary to retrieve address)
    argument["expand"] = "venue"

    eventbrite.event_search(**arguments)
    #populate this dictionary with info from the search
    dict = {}

    

eb_api_query()
