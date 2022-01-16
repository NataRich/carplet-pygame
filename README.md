# Carplet
This is a fully configurable card game built by `pygame` that 
allows you to customize game plots as you wish. It builds
a fun card-based strategy game out-of-box and is really 
easy to get started.

We have provided a few sample game plots in `plot.json` 
for you to get familiar with how Carplet works. In this
plot, you become the mayor of a city. You will be 
constantly facing various crises, ranging from 
environmental disasters to social unrest. You need to 
make decisions accordingly. Every decision you make affects 
different stakeholders differently. You are expected to make 
decisions with careful consideration in mind since if one 
party gets really annoyed, your journey as a mayor would 
come to an end.

## Get Started
### Sample Game: I'm the Mayor
To get started with our sample game plots is simple. Running
the provided `main.py` in the correct directory will suffice.

```shell
$ pwd
/your/path/to/carplet

$ python3 main.py
pygame 2.1.2 (SDL 2.0.18, Python 3.8.9)
Hello from the pygame community...
```

### Customization
#### Where to customize?
Customization goes in a `json` file under the project directory.
In our sample, we put it in `plot.json`. You can actually 
name the file whatever you want, e.g.`this_is_my_plot.json`.

#### How to customize?
Customization is parsed in a structured way. At the top level of
the `json` file, there are 5 keys you need to define, i.e. `name`,
`creator`, `success`, `indexes`, and `plots`.

- `name` defines the name of the game
- `creator` defines the creator(s) of the game
- `success` defines the string to be printed on the screen if player succeeds
- `indexes` defines exactly **4** `index`es that are subject to player's decisions
  - `index`defines **4** attributes, i.e. `name`, `start`, `icon`, and `end_str`
    - `name` defines the name of the index, e.g. President
    - `start` defines the initial value, e.g. 50
    - `icon` defines the path to the icon asset
    - `end_str` defines the string to be printed on the screen if player fails this index
- `plots` defines an array of `plot`s that player can go through where they encounter
    different situations and make decisions
  - `plot` defines a list of `event`s 
    - `event` defines **3** attributes, i.e. `title`, `desc`, and `cards`
      - `title` defines the title of the event
      - `desc` defines the description of the event
      - `cards` defines **3** `card`s or decisions that player can make
        - `card` defines **4** attributes, i.e. `title`, `desc`, `effects`, and `cons`
          - `title` defines what the card is called
          - `desc` defines what the card can do
          - `effects` defines a list of numbers that affect indexes' values
          - `cons` defines the consequence string to be printed after player chooses this card
    
    

