class transaction {
  constructor(type, amount) {
    this.type = type; // deposit | withdraw
    this.amount = amount;
  }
}

class BankAccount {
  constructor() {
    this.balance = 0;
    this.transactions = [];
  }
  deposit(amount) {
    if (amount <= 0) {
      return "Deposit amount must be greater than zero.";
    } else {
      this.transactions.push(new transaction("deposit", amount));
      this.balance += amount;
      return `Successfully deposited $${amount}. New balance: $${this.balance}`;
    }
  }
  withdraw(amount) {
    if (amount <= 0 || amount > this.balance) {
      return "Insufficient balance or invalid amount.";
    } else {
      this.transactions.push(new transaction("withdraw", amount));
      this.balance -= amount;
      return `Successfully withdrew $${amount}. New balance: $${this.balance}`;
    }
  }
  checkBalance() {
    return `Current balance: $${this.balance}`;
  }

  listAllDeposits() {
    let str = "Deposits: ";
    for (const transaction of this.transactions) {
      if (transaction.type === "deposit") {
        str += transaction.amount + ",";
      }
    }
    return str.slice(0, -1);
  }
  listAllWithdrawals() {
    let str = "Withdrawals: ";
    for (const transaction of this.transactions) {
      if (transaction.type === "withdraw") {
        str += transaction.amount + ",";
      }
    }
    return str.slice(0, -1);
  }
}

const myAccount = new BankAccount();
console.log(myAccount.deposit(5000));
console.log(myAccount.deposit(2000));
console.log(myAccount.withdraw(300));
console.log(myAccount.withdraw(1000));
console.log(myAccount.withdraw(500));

console.log(myAccount.listAllDeposits());
console.log(myAccount.listAllWithdrawals());
console.log(myAccount.checkBalance());
