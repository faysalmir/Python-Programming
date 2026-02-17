"""
Conditional Execution Examples
For BS Business Data Analytics Students

This file demonstrates how conditional statements are used
in business and data analytics scenarios.
"""

# 1️⃣ Sales Target Check
def sales_target_check(sales, target):
    if sales > target:
        print("Target achieved!")
    else:
        print("Target not achieved.")


# 2️⃣ Loan Approval System
def loan_approval(credit_score):
    if credit_score >= 700:
        print("Loan Approved")
    else:
        print("Loan Rejected")


# 3️⃣ Customer Segmentation
def customer_segmentation(purchase_amount):
    if purchase_amount >= 10000:
        print("Platinum Customer")
    elif purchase_amount >= 5000:
        print("Gold Customer")
    elif purchase_amount >= 1000:
        print("Silver Customer")
    else:
        print("Regular Customer")


# 4️⃣ Profit or Loss Analysis
def profit_analysis(revenue, cost):
    profit = revenue - cost

    if profit > 0:
        print("Profit:", profit)
    elif profit < 0:
        print("Loss:", profit)
    else:
        print("Break-even")


# 5️⃣ High Sales Day Detection
def high_sales_days(daily_sales):
    for sale in daily_sales:
        if sale > 10000:
            print("High sales day:", sale)


# 6️⃣ Employee Bonus Eligibility
def bonus_eligibility(sales, attendance):
    if sales > 100000 and attendance > 90:
        print("Eligible for Bonus")
    else:
        print("Not Eligible for Bonus")


# 7️⃣ Simple Fraud Detection Logic
def fraud_detection(transaction_amount, country):
    if transaction_amount > 10000 and country == "Foreign":
        print("Flag as suspicious transaction")
    else:
        print("Transaction normal")


# ==============================
# Main Program Execution
# ==============================
if __name__ == "__main__":
    print("---- Sales Target Check ----")
    sales_target_check(120000, 100000)

    print("\n---- Loan Approval ----")
    loan_approval(680)

    print("\n---- Customer Segmentation ----")
    customer_segmentation(7500)

    print("\n---- Profit Analysis ----")
    profit_analysis(50000, 42000)

    print("\n---- High Sales Days ----")
    daily_sales = [5000, 12000, 8000, 15000, 7000]
    high_sales_days(daily_sales)

    print("\n---- Bonus Eligibility ----")
    bonus_eligibility(120000, 95)

    print("\n---- Fraud Detection ----")
    fraud_detection(20000, "Foreign")
