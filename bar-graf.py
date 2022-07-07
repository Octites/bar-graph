def main():
    prices_list = prices()
    graph(prices_list)
def prices():
    infile = open('1994_Weekly_Gas_Averages.txt','r')
    prices = (infile.readlines())
    infile.close
    for index in range(len(prices)):
        prices[index] = float(prices[index].rstrip('\n'))
    return prices
def graph(prices_list):
    import matplotlib.pyplot as plt
    plt.title('1994 Weekly Gas Graph')
    plt.plot(prices_list)
    plt.xticks(range(0,len(prices_list)+1, 1))
    plt.xlabel('Weeks in 1994')
    plt.ylabel('Average Weekly Gas Price, in $')
    plt.grid(True)
    plt.show()
main()
