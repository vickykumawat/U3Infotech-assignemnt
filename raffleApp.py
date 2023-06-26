import random

# Data Structures
class Ticket:
    def __init__(self, numbers):
        self.numbers = numbers

class User:
    def __init__(self, name):
        self.name = name
        self.tickets = []

class Draw:
    def __init__(self):
        self.pot = 100
        self.users = []
        self.winning_ticket = None
        self.winners = {
            "Group 2": [],
            "Group 3": [],
            "Group 4": [],
            "Group 5": []
        }

# Raffle App
class RaffleApp:
    def __init__(self):
        self.draw = None

    def start_new_draw(self):
        self.draw = Draw()
        print("New Raffle draw has been started. Initial pot size: $100")

    def buy_tickets(self):
        name, num_tickets = input("Enter your name, number of tickets to purchase: ").split(",")
        user = User(name.strip())
        for _ in range(int(num_tickets.strip())):
            ticket_numbers = random.sample(range(1, 16), 5)
            ticket = Ticket(ticket_numbers)
            user.tickets.append(ticket)
        self.draw.users.append(user)
        self.draw.pot += 5 * int(num_tickets.strip())

        print(f"Hi {name.strip()}, you have purchased {num_tickets.strip()} ticket(s)")
        for i, ticket in enumerate(user.tickets, start=1):
            print(f"Ticket {i}: {' '.join(str(num) for num in ticket.numbers)}")

    def run_raffle(self):
        self.draw.winning_ticket = Ticket(random.sample(range(1, 16), 5))

        print("Running Raffle..")
        print("Winning Ticket is:", ' '.join(str(num) for num in self.draw.winning_ticket.numbers))

        for user in self.draw.users:
            for i, ticket in enumerate(user.tickets):
                num_matches = len(set(ticket.numbers) & set(self.draw.winning_ticket.numbers))
                if num_matches >= 2:
                    self.draw.winners[f"Group {num_matches}"].append((user.name, ticket))

        for group, winners in self.draw.winners.items():
            if winners:
                reward = self.calculate_reward(group)
                print(f"\n{group} Winners:")
                for winner in winners:
                    print(f"{winner[0]} with {len(winners)} winning ticket(s) - ${reward}")

    def calculate_reward(self, group):
        pot = self.draw.pot
        if group == "Group 2":
            return round(pot * 0.1 / len(self.draw.winners[group]), 2)
        elif group == "Group 3":
            return round(pot * 0.15 / len(self.draw.winners[group]), 2)
        elif group == "Group 4":
            return round(pot * 0.25 / len(self.draw.winners[group]), 2)
        elif group == "Group 5":
            return round(pot * 0.5 / len(self.draw.winners[group]), 2)

    def display_menu(self):
        print("\nWelcome to My Raffle App")
        if self.draw:
            print(f"Status: Draw is ongoing. Raffle pot size is ${self.draw.pot}")
        else:
            print("Status: Draw has not started")
        print("[1] Start a New Draw")
        print("[2] Buy Tickets")
        print("[3] Run Raffle")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.start_new_draw()
            elif choice == "2":
                self.buy_tickets()
            elif choice == "3":
                self.run_raffle()
            else:
                print("Invalid choice. Please try again.")


# Main program
if __name__ == "__main__":
    app = RaffleApp()
    app.run()
