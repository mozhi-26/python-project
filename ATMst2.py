import streamlit as st

# Base class for ATM
class ATM:
    def __init__(self, balance=1000):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"${amount} deposited successfully. New balance: ${self.balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        elif amount > self.balance:
            return "Insufficient  balance."
        else:
            self.balance -= amount
            return f"${amount} withdrawn  successfully. Remaining  balance: ${self.balance}"

# Derived class for ATM Simulator
class ATMSimulator(ATM):
    pass  # In Streamlit, we'll handle the UI separately

# Streamlit interface
st.title(" ATM Simulator")

# Initialize ATM instance in session state
if 'atm' not in st.session_state:
    st.session_state.atm = ATMSimulator()

atm = st.session_state.atm

# ATM operations in Streamlit
operation = st.radio("Select Operation:", ["Check Balance", "Deposit", "Withdraw"])

if operation == "Check Balance":
    st.success(f"Your current balance is: ${atm.check_balance()}")

elif operation == "Deposit":
    deposit_amount = st.number_input("Enter amount to deposit:", min_value=0.0, step=1.0)
    if st.button("Deposit"):
        result = atm.deposit(deposit_amount)
        st.success(result)

elif operation == "Withdraw":
    withdraw_amount = st.number_input("Enter amount to withdraw:", min_value=0.0, step=1.0)
    if st.button("Withdraw"):
        result = atm.withdraw(withdraw_amount)
        st.success(result)