from queue import PriorityQueue

class Coffee:
    def __init__(self):
        bob_coffee = int(input("Price of Bob's Coffee: "))
        jeremy_coffee = int(input("Price of Jeremy's Coffee: "))
        coworker1_coffee = int(input("Price of Coworker 1's Coffee: "))
        coworker2_coffee = int(input("Price of Coworker 2's Coffee: "))
        coworker3_coffee = int(input("Price of Coworker 3's Coffee: "))
        coworker4_coffee = int(input("Price of Coworker 4's Coffee: "))
        coworker5_coffee = int(input("Price of Coworker 5's Coffee: "))

        # analyze the total amount of coffee consumed per day
        self.total_per_day = bob_coffee + jeremy_coffee + coworker1_coffee + coworker2_coffee + coworker3_coffee + coworker4_coffee + coworker5_coffee

        self.pq = PriorityQueue()

        self.pq.put((0, "Bob"))
        self.pq.put((0, "Jeremy"))
        self.pq.put((0, "Coworker 1"))
        self.pq.put((0, "Coworker 2"))
        self.pq.put((0, "Coworker 3"))
        self.pq.put((0, "Coworker 4"))
        self.pq.put((0, "Coworker 5"))

    def who_buys_coffee(self):
        payer = self.pq.get()
        print(f"{payer[1]} will buy the coffee today.")
        new_total = payer[0] + self.total_per_day
        self.pq.put((new_total, payer[1]))
        end = input("Do you want to continue? (y/n): ")
        if end == "y":
            self.who_buys_coffee()
        else:
            print("Thank you for using the program!")

if __name__ == "__main__":
    coffee = Coffee()
    coffee.who_buys_coffee()


