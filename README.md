# Connect 4 AI

Maintainer  - [OnlyCS](https://github.com/onlycs)\
Status      - WIP\
Follows PEP8

## Game GUI - `game.gui`
### Elements - `game.gui.elements.*`
All elements extend `BaseElement`. You can change the attributes of the elements by using
the `set[attrib]()` method. You can then change the render state with `render()`, 
`unRender()`, and `reRender()`. `render()` can only be called when the element is not 
rendered, vice versa for `unRender()`. `reRender()` can be called only when the element 
is already rendered.

### Board - `game.gui.board`
The board is a wrapper containing all elements. The board holds a `list` of items that
should be rendered, and can be changed when using the `render` functions of elements.
Implements `game.internals.board` to tell where and when elements should be rendered.

### Game - `game.gui.game`
The game is a wrapper for `pyglet.window.Window`. All it does is render elements from the
board's `renderList[]`, and forward events (e.g. mouse clicks) to the event handlers in
`game.gui.events.*`.

## Game Internals - `game.internals`
### Board - `game.internals.board`
`class Board(list)`. Contains a list of `column`s. Also implements win detecting.

### Column - `game.internals.column`
`class Column(list)`. Contains a list of `Chip`s. Implements array gravity (or 
antigravity) in this case -- all elements are pushed to the top of the list.

### Chip - `game.internals.chip`
`class Chip(str)`. Contains either `"red"` or `"yellow"`. If initialized with a different
value, throws a `ValueError`.

### Turn - `game.internals.turn`
`class Turn`. Uses method `take()` to flip between `"red"` and `"yellow"`.