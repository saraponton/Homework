from matplotlib import pylab as plt
import pandas

df1 = pandas.read_csv("/Users/saraponton/Downloads/AMZN.csv")
print(df1.head())
df1['Date'] = pandas.to_datetime(df1.Date)

df2 = pandas.read_csv("/Users/saraponton/Downloads/AAPL.csv")
print(df2.head())
df2['Date'] = pandas.to_datetime(df2.Date)

df3 = pandas.read_csv("/Users/saraponton/Downloads/NFLX.csv")
print(df3.head())
df3['Date'] = pandas.to_datetime(df3.Date)

plt.title("Stock Comparison: IBM vs Apple vs Microsoft")

plt.plot(df1.Date, df1.Open, "r:", label="Amazon", linewidth=0.5, ms=0.5)
plt.plot(df2.Date, df2.Open, "b:", label="Apple", linewidth=0.5, ms=0.5)
plt.plot(df3.Date, df3.Open, "y:", label="Netflix", linewidth=0.5, ms=0.5)
plt.legend(loc="upper left")
plt.xlabel("Year")
plt.ylabel("Price in US Dollars")
plt.show()