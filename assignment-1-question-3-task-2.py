#Task 2: Bank Interest If you have a savings account with a particular initial amount\
    #and a fixed yearly interest rate, calculate the total amount in your account after a year. \
        # so if you had $10,000 at a 7% interest write code that would tell us the amount\
            # at the end of the year. For the example the expected outcome would be $10,700.
            
initial_amount = 10000
interest_rate = 0.07
annual_total = initial_amount + (initial_amount * interest_rate) / 100**1
print(annual_total)