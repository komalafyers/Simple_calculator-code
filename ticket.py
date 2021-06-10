tickets = []
airline=str('Enter the airline:') 
source= str('Enter the source:')[:3]
destination=str('Enter the destination')
no_of_passengers =int(input('Enter the total number of passengers:'))
for ticket_number in range(101,101+no_of_passengers):

   tickets.append('%s:%s:%s:%d'%(airline,source,destination,ticket_number))

if no_of_passengers > 5:

   print(tickets[-5:])  

else:  

   print(tickets) 
