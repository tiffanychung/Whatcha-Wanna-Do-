from eventbrite import Eventbrite
from tok import secret
import pprint

token = secret()
eventbrite = Eventbrite(token)
pp = pprint.PrettyPrinter(indent=4)
user = eventbrite.get_user()
print(user['id'])
print(user['name'])

def eb_api_query(*args):
    # dictionary keys of argument are the fields we care about
    # argument = {}
    #
    argument['start_date.range_start'] = args[0]
    argument['location.address'] = args[1]
    argument['price'] = args[2]
    argument['location.within'] = args[3]
    argument['categories'] = args[4]
    # # do something like this...
    # # argument["location.address"] =
    # argument['location.address'] = 'Berkeley'
    # argument['location.within'] = '5mi'
    # argument['start_date.range_start'] = "2019-09-29T00:00:00"
    # argument['categories'] = "104"
    # #this line is to expand the venue field (necessary to retrieve address)
    # argument["expand"] = "venue"
    # argument['price'] = "free"

    #print("dictionary:", eventbrite.event_search(**argument)) #calling thes earch function on the arguments
    #you have declared? either print or set to variable. this return a dictionary that returns all the events
    #populate this dictionary with info from the search
    nonrelevantdict = eventbrite.event_search(**argument)

    events = []
    print(len(nonrelevantdict['events']))
    for i in range(5):#len(nonrelevantdict)
        dict  = {}
        #retrieve name
        dict['name'] = nonrelevantdict['events'][i]['name']['text']
        #retrieve url
        dict['url'] = nonrelevantdict['events'][i]['url']
        #retrieve description
        dict['description'] = nonrelevantdict['events'][i]['description']['text']
        #retrieve date
        dict['date'] = nonrelevantdict['events'][i]['start']['local']
        #retrieve image
        #dict['image'] =
        print(nonrelevantdict['events'][i]['logo']['original']['url'])
        #retrive location
        dict['location'] = nonrelevantdict['location']['augmented_location']['city']
        events.append(dict)
    return events
