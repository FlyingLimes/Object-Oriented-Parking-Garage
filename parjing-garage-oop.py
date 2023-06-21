
class Parking_Garage():
    
    def __init__(self):
        self.tickets = list(range(1,123))
        self.parkingSpaces = list(range(1,123))
        self.currentTicket = {'paid': False}
    
    def takeTicket(self):
            print(f'Ticket Number: {self.tickets.pop()}\nParking Space: {self.parkingSpaces.pop()}')
            print(f'\nAvailable Tickets: {len(self.tickets)}')
            print(f'Available Spaces: {len(self.parkingSpaces)}')

    def payForParking(self):
        pay_parking = int(input('Please submit payment. \n Parking Fee: $25  '))
        if pay_parking == 25:
            self.currentTicket = {'paid': True}
            print(f'\nThank you for the payment. Please wait for gate to open before exiting')
            increase_tickets = self.tickets[-1] + 1
            self.tickets.append(increase_tickets)
            increase_spaces = self.parkingSpaces[-1] + 1
            self.parkingSpaces.append(increase_spaces)
            print(f'\nAvailable Tickets: {len(self.tickets)}')
            print(f'Available Spaces: {len(self.parkingSpaces)}')
        if pay_parking > 25:
            self.currentTicket = {'paid': True}
            dispense_amount = pay_parking - 25
            print(f'\Printing receipt{dispense_amount} ')
            print(f'Thank you for the payment. Please wait for gate to open before exiting.')
            increase_tickets = self.tickets[-1] + 1
            self.tickets.append(increase_tickets)
            increase_spaces = self.parkingSpaces[-1] + 1
            self.parkingSpaces.append(increase_spaces)
            print(f'\nAvailable Tickets: {len(self.tickets)}')
            print(f'Available Spaces: {len(self.parkingSpaces)}')
        if pay_parking < 25:
            self.currentTicket = {'paid': False}
            balance = 25 - pay_parking
            print(f'\nPlease input {balance}  to complete payment.')
            remaining_balance = int(input('Remaining Balance:'))
            if remaining_balance == balance:
                self.currentTicket = {'paid': True}
                print(f'\nThank you for the payment. Please wait for gate to open before exiting')
                increase_tickets = self.tickets[-1] + 1
                self.tickets.append(increase_tickets)
                increase_spaces = self.parkingSpaces[-1] + 1
                self.parkingSpaces.append(increase_spaces)
                print(f'\nAvailable Tickets: {len(self.tickets)}')
                print(f'Available Spaces: {len(self.parkingSpaces)}')
                
            else:
                self.currentTicket = {'paid': False}
                print('\nTransaction failed. Please try again.')
                
    def leaveGarage(self):
        if self.currentTicket == {'paid': True}:
            print('\nThank you and have a nice day!')
        else:
            print("This ticket has not been paid. Type 'Pay' \nTicket Amount: $25")

usedTicket = Parking_Garage()


def run():
    while True:
        question = input("Welcome to Parker Parking. Event Parking - $25\nPlease type your selection: \n'Ticket': Print Ticket \n'Pay': Pay Ticket \n'Exit': Leave Garage \n'Quit': Quit: ")
        
        if question.lower() == 'ticket':
            usedTicket.takeTicket()
        if question.lower() == 'pay':
            usedTicket.payForParking()
        if question.lower() == 'exit':
            usedTicket.leaveGarage() 
        if question.lower() == 'quit':
            break
run()