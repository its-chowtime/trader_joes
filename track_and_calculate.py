# What is my batting score (per day?, per trade?)
# Green / Red day for month

# TODO: Clean the data up from csv file using regex
# TODO: Write program to build the dataframe and do calculations
# TODO: Store data to database?
# TODO: Display results on a web interface
# TODO: Formula to find out BUY / SELL and OPEN / CLOSE

# * Batting Score Calculations
# 1 = win, 0 = loss
# count(total wins), count(total losses) divided by total
# If Green > Red : "Green Day" Else: "Red Day"

# Date Time > Strike > Exp > Symbol > Side > Qty > Pos Effect
    # Pull price bought from subtracted by price sold = profit/loss


from clean_trade_activity import find_line_number

df = find_line_number()
print(df)
