# python-OOP

## Project Summary

Conforming to `Object Oriented Programming`, build various `Classes` with a set amount of `Properties`. These will interact with specific `Methods` to obtain and return specific data when the function is invoked. A `TDD` approach will be utilised with `Pytest` to ensure the code functionality is checked and producing the correct assertions.
<br>

## Section One

### Part One

`build_a_northcoder.py` and `test_build_a_northcoder.py`

Create a Class of Northcoder, this class should have the following properties:

-   `name`
-   `location`
-   `course`
-   `graduation_date`


The Northcoder should have the following methods:

-   `greet`

```py
alex.greet('Joe') # Should return 'Hello Joe, my name is Alex'
```

-   `alumni`

```py
alex.alumni() # Should return True as Alex's graduation date has passed.
```

<br>

### Part Two

`high_score_table.py` and `test_high_score_table.py`

-   Create a high score table class that takes one argument to control a `limit` property.

-   This class should hold a `scores` property that returns a list. All scores in the list should be returned in descending order.

```py
high_scores = HighScoreTable(3)
high_scores.scores == [] # Should return True
high_scores.limit # Should return 3
```

-   Add an `update` method to update the scores list with a **dictionary** containing the name of the player and their score.

```py
high_scores.update({'player':'Cat', 'score':95})
high_scores.update({'player':'Verity', 'score':150})
high_scores.scores # Should return [{'player':'Verity', 'score':150},{'player':'Cat', 'score':95}] as the scores are in descending order
```

-   The `update` method should not allow more scores to be added if the `limit` has been reached. If the `limit` has been reached, and the score passed to the `update` method is larger than any of the stored scores, the new high score should be stored.

-   Add a method to return the `average_score` of all the high scores.

-   Add a method that returns the `highest_scorer` in the table.

-   Add a method that returns the `lowest_scorer` in the table.

-   Add a method to `reset` the scores table to remove all high scores.

```py
high_scores.scores # Would return [{'player':'Verity', 'score':150},{'player':'Cat', 'score':95}]
high_scores.reset()
high_scores.scores # After reset method should return []
```


<br>

### Part Three

`build_a_northcoder.py` and `test_build_a_northcoder.py`


-   Create a class of Ghost with the following properties :`name`, `speed` and `colour`

```py
ghost = Ghost('Ducky', 3, 'yellow')
ghost.name # Would return 'Ducky'
ghost.colour # Would return 'yellow'
```

-   Each Ghost also needs a property of `is_scared`. This property will default to False.

```py
ghost.is_scared # Would return False
```

-   When Pac Man eats a fruit, the Ghosts become scared and can be eaten. Add a method called `can_be_eaten`. This method should return `True` if the Ghosts are scared, or `False` if they are not.

```py
mack = Ghost('Mack', 9, 'grey')
mack.colour # Should return 'grey'
mack.is_scared # Should return False
mack.can_be_eaten() # Should return False
```

-   If the Ghosts are scared, their `colour` will change to blue. If a Ghost is blue, they can also be eaten. Create a method called `frighten` to control this change.

```py
mack.is_scared # Should return False
mack.can_be_eaten() # Should return False

mack.frighten()
mack.is_scared # Should return True
mack.can_be_eaten() # Should return True
mack.colour # Should return 'blue'
```

-   As Pac Man's lives reduce, each ghost's `speed` is increased by 10%. Create a method called `speed_up` that updates the ghost's speed with each invocation.

```py
jersey = Ghost('Jersey', 3, 'white')
jersey.speed_up()
jersey.speed # Should return 3.3
jersey.speed_up()
jersey.speed # Should return 3.63
jersey.speed_up()
jersey.speed # Should return 3.993
```

In the original Pac Man game, the four ghosts had set names and colours. Extend your Ghost class for all four ghosts.

-   Blinky is red and has a speed of 3,
-   Pinky is pink and has a speed of 2,
-   Inky is cyan and has a speed of 4,
-   Clyde is yellow and has a speed of 1.

```py
blinky = Blinky('Blinky', 3,'red')
blinky.colour # Should return 'red'

blinky.frighten()
blinky.colour # Should return 'blue'
blinky.is_scared # Should return True
blinky.can_be_eaten # Should return True
```

<br>

All of the class extensions should still have access to the original methods and should show the expected behaviour.

