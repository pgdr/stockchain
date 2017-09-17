# stockchain

This is a stock game on the block chain.

Users can trade stocks using very basic smart contracts, exchanging money and
stocks.


## The blockchain

Each element on the block chain is either
* adding a user, username and public key, and initial amount of money
* a buy (sell, resp.) option, which is a transaction containing a five
  tuple (a message)
  * A buy (sell) message: stock, amount, price, creation date and
    expiration date
  * Signed message by first part (buyer, or seller, respectively)
  * Double-signed message by second part
* Initialization of a new stock, containing stock name, amount and owner

Every block has a timestamp (between creation and expiration date), at least one
of the above, and a users signature.  In addition, it of course has a nonce and
a pointer back to a previous block.


## Transactions

A transaction is either
* `Buy (STOCK, amount, price_per_stock, creation, expiration)`, or
* `Sell(STOCK, amount, price_per_stock, creation, expiration)`,
each comes with a signature by the originator, and with the implicit promise
that the originator either has the necessary amount of money, or the necessary
amount of stocks, respectively.

A transaction is _completed_ when a second part signs the transaction, with an
implicit promise that this part has the necessary amount of stocks, or money,
respectively.

A completed transaction is _accepted_ when a block is created with a timestamp
(between creation and expiration date).  The miner should take care to verify
that the users have the necessary amount of goods, and that the Message is not
already present in the blockchain, lest it will be rejected by the clients.


## The client

The client blockchain should reject any block that does not satisfy the above
conditions for transactions, re-registering users, or re-registering stocks.


## Future work

* Rewards for mining
* Fees to miners
* Difficulty instead of fixed
