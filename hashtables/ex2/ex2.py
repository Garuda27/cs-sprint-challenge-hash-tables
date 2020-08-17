#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here 
    ticket_dict = {}
    route = []
   
    
    for ticket in tickets:
        ticket_dict[ticket.source] = ticket.destination

    
    curr_city = ticket_dict['NONE']
    route.append(curr_city)

    while curr_city != 'NONE':
        curr_city = ticket_dict[curr_city]
        route.append(curr_city)

    return route
