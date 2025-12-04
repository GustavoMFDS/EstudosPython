
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total = 0
        for entry in self.ledger:
            total += entry["amount"]
        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0

        for entry in self.ledger:
            desc = entry["description"][:23]
            amt = f"{entry['amount']:.2f}"
            items += f"{desc:<23}{amt:>7}\n"
            total += entry["amount"]

        return title + items + f"Total: {total:.2f}"


def create_spend_chart(categories):
    spent = []
    for category in categories:
        total = 0
        for entry in category.ledger:
            amount = entry["amount"]
            if amount < 0:
                total += -amount
        spent.append(total)

    total_spent = sum(spent)

    percentages = [(s / total_spent * 100) // 10 * 10 for s in spent]

    chart = "Percentage spent by category\n"

    for i in range(100, -10, -10):
        line = f"{i:>3}| "
        for perc in percentages:
            line += "o  " if perc >= i else "   "
        chart += line + "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    names = [cat.name for cat in categories]
    max_length = max(len(name) for name in names)

    for i in range(max_length):
        line = "     "
        for name in names:
            line += (name[i] + "  ") if i < len(name) else "   "
        chart += line
        if i < max_length - 1:
            chart += "\n"

    return chart


