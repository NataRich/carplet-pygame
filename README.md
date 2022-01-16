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
##### A general view
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

For example,

```json
{
  "name": "...",
  "creator": "...",
  "success": "...",
  "indexes": [
    {
      "name": "President",
      "start": 50,
      "asset": "Assets/icon/gov.png",
      "end": "The president FIRED you!"
    },
    ...
  ],
  "plots": [
    [
      {
        "title": "Smoke in the Woods",
        "desc": "...",
        "cards": [
          {
            "title": "Do Nothing",
            "desc": "Probobaly kids BBQ",
            "effects": [0, 0, -20, 0],
            "cons": "..."
          },
          ...
        ]
      },
      ...
    ],
    ...
  ]
}
```

##### A detailed view
###### `Card` in`card.py`
`Card` is the most elementary object that manages a card. It has **4**
attributes, `title`, `desc`, `effects`, and `cons`. As the attribute
names suggest, `title` specifies a short name of a card; `desc` is a
fairly long description of what this card can do; `effects` indicate
how this card can affect the corresponding indexes, meaning **the 
length of `effects` must be equal to the length of `indexes`; finally,
`cons` is short for consequence, which is the string to be displayed in
a short-lived popup after player selects the card.

For example,
```json
{
  "title": "Do Nothing",
  "desc": "Probobaly kids BBQ",
  "effects": [0, 0, -20, 0],
  "cons": "You think it's not a big deal and decide not to worry about it"
}
```

###### `Event` in`event.py`
`Event` is the core object that manages plots. It has **3** attributes, 
`title`, `desc`, and `cards`. Similarly, `title` specifies a short name
of the event; `desc` is a longer description of the event; `cards` is a
list of `card`s that player can choose from when facing this event.

For example,
```json
{
  "title": "Smoke in the Woods",
  "desc": "Someone reports observing unusual smoke coming out of the woods",
  "cards": [...]
}
```

###### Plot
Plot is simply a list of events, used to manage different plots.

###### Plots
Plots is a list of plot, i.e. a 2D array of `Event` objects.

###### `Index` in `index.py`
`Index` is the object that manages an index. It has **4** attributes, 
`name`, `start`, `icon`, and `end_str`. `name` specifies a short name
of the index; `start` sets the initial value and reset value of the index;
`icon` specifies the path to the icon asset; `end_str` is the string to be 
printed on the screen if player fails this index, i.e. when value <= 0.

For example,
```json
{
  "name": "President",
  "start": 50,
  "asset": "Assets/icon/gov.png",
  "end": "The president FIRED you!"
}
```

###### Indexes
Indexes is simply a list of (**4** of) `index`es.

## Contributors
@Ashley, @Mike, @Jaylan