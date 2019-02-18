<center><img src="https://i.postimg.cc/02fKKCFt/art-2968627-1920.jpg"></center>

[Heisenberg](https://github.com/emre/heisenberg) is a Python command line application and a library to play drugwars without using the website. 

Drugwars is a blockchain based game. That makes it possible for the blockchain accounts to play the game using off-site transactions. 

# Installation

```
$ pip install heisenberg
```

# Usage

```
from heisenberg.core import Heisenberg

h = Heisenberg(
    'emrebeyler',
    '<private_posting_key>'
)
```

# Investing to heist

```
tx_data = h.heist(1000)
print(tx_data)
```

# Recruting Units

```
tx_data = h.unit("bouncer", 1)
print(tx_data)
```

# Upgrades with in-game resources

```
tx_data = h.upgrade("headquarters")
print(tx_data)
```

# Attack to other players

```
 tx_data = h.attack(
     "<defender_username>",
     [{'unit': 'knifer', 'amount': 3}, {'unit': 'bouncer', 'amount': 2}]
))
```

# Creating a char

Only once in the beginning.

```
h.char("1", referer="emrebeyler")
```

