# Coin Exchange
Compares the Greedy and Dynamic Programming implementations of a coin exchange algorithm based on the number of errors in 1000 trials.

The Dynamic Programming implementation should always return the fewest number of coins in order to make change for a given amount. The Greedy algorithm does not if we use the Roman Republic currency, which is the coin set [1,4,5,9]. For instance, for returning 8 cents, the Greedy approach would return [1,1,1,5] whereas the Dynamic Programming approach, the correct solution, returns [4,4]. This program counts the number of errors in the Greedy implementation by change amounts from 0-1000 cents.
