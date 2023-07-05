class mpesatransaction:
    def __init__(self, transaction_id, amount):
        self.transaction_id = transaction_id
        self.amount = amount

    def process_transaction(self):
        raise NotImplementedError("subclass to use this method")


class deposittransaction(mpesatransaction):
    def process_transaction(self):
        print(f"deposit transaction with ID {self.transaction_id}processed. amount{self.amount}")


class withdrawaltransaction(mpesatransaction):
    def process_transaction(self):
        print(f"withdrawal transaction with ID {self.transaction_id}processed. amount{self.amount}")


class paymenttransaction(mpesatransaction):
    def __init__(self, transaction_id, amount, recipient):
        super().__init__(transaction_id, amount)
        self.recipient = recipient

    def process_transaction(self):
        print(
            f"payment transaction with ID {self.transaction_id}processed. amount{self.amount}. recipient{self.recipient}")


deposit = deposittransaction("DHTY ", 2000)
deposit.process_transaction()
withdrawal=withdrawaltransaction("UFMI ", 6987)
withdrawal.process_transaction()
