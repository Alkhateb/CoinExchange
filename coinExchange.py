__author__ = "Michael Racine"
__email__ = "mrracine23@gmail.com"

# Gets the greatest common factor of change and standard
# change: the amount of change required
# coins: the coins available
def getGCF(change, coins):

    gcf = 0

    for i in coins:
        if change - i >= 0:
            gcf = i
            break

    return gcf

# Returns the number of the fewest coins needed (greedy approach)
# change: the change required
# coins: the coins available
def fewestCoinsGreedy(change, coins):

    numCoins = 0
    current = change
    
    while current > 0:
        current_gcf = getGCF(current, coins)
        # print("{} {}".format(current, current_gcf))
        current -= current_gcf
        numCoins += 1

    return numCoins

# Returns the number of the fewest coins needed (dynamic programming approach)
# change: the change required
# coins: the coins available
def fewestCoinsDP(change, coins):

    table = [0 for x in range(change + 1)]

    # Start at index 1
    for i in range(1, change + 1):
        optValues = []

        # Check if each coin is less than i
        for coinAmt in coins:
            if coinAmt <= i:
                optValues.append(1 + table[i - coinAmt])
                
        table[i] = min(optValues)

    return table[change]

def main():

    rrCurrency = [9,5,4,1]
    errors = 0

    # Do from range 0-1000 (inclusive)
    for i in range(0, 1001):
        
        greedyCoins = fewestCoinsGreedy(i, rrCurrency)

        # Need different algorithm for this (Dynamic Programming)
        dpCoins = fewestCoinsDP(i, rrCurrency)

        if greedyCoins != dpCoins:
            errors += 1

    #print("G: {}".format(greedyCoins))
    #print("DP: {}".format(dpCoins))
    print("Errors: {}".format(errors))

if __name__ == "__main__":
    main()
