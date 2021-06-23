# Bellman Ford - Potion Trading
You have come to a new town,
and your goal is to trade with the local people in order to maximise the value of the potion you
have.

Each person in the town is willing to make various trades at various ratios. For example, one
person might trade water for mercury at a rate of 1L water for 0.01L mercury. Since you are
from the big city, you know the prices of each of these potions, and so you can determine which
trades are worthwhile and which are not.

You are only in the town for a limited time, and trading takes time, so you have a maximum
number of trades you can conduct before you need to move on, though you may choose to trade
fewer times than this maximum. You also only have one container (with unlimited capacity!),
and you cannot mix potions or they will become worthless, so you must trade all of your current
potion whenever you make a trade.


## Input
potions each have an ID. There are n potions, and each one has a unique ID from the range
[0..n-1].

**prices** is an array of length n, where prices[i] is the value of 1L of the potion with ID i.

**starting_potion** is the ID of the potion you arrive with. You always start with 1L of this potion.

**townspeople** is a list of lists. Each interior list corresponds to the trades offered by a particular
person. The interior lists contain 3 element tuples, (give, receive, ratio). Each tuple
indicates that this person is willing to be given potion with ID give in exchange for potion with
ID receive at the given ratio. For example, (2,5,1.5) indicates that you can give potion with
ID 2, and receive 1.5 times as much potion with ID 5. Note that people are not necessarily
willing to perform these trades in both directions, i.e. this example does not mean that you
can give potion 5 and receive potion 2.

For each potion, there will be at least one townsperson who is willing to trade for that potion.

## Output
best_trades should return the maximum value that you can obtain after performing at most
max_trades trades.

## Example
```
prices = [10,5,1,0.1]
starting_potion = 0
max_trades = 6
townspeople = [[(0,1,4),(2,3,30)],[(1,2,2.5),(2,0,0.2)]]
best_trades(prices, starting_potion, max_trades, townspeople)
>>>60
max_trades = 2
best_trades(prices, starting_potion, max_trades, townspeople)
>>>20

The solution to the first case is to perform the following trades:

starting value: $10
trade 1L of 0 for 4L of 1: value $20
trade 4L of 1 for 10L of 2: value $10
trade 10L of 2 for 2L of 0: value $20
trade 2L of 0 for 8L of 1: value $40
trade 8L of 1 for 20L of 2: value $20
trade 20L of 2 for 600L of 3: value $60

The solution to the second case is to perform the following trade:

starting value: $10
trade 1L of 0 for 4L of 1: value $20
```

## Complexity
best_trades must run in O(T M) time where
- T is the total number of trades available
- M is max_trades

### Disclaimer
1. This case study derives from my school assignment.
2. Details of the actual case study has been sanitized and changed.

