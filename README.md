<!--
author:   ModuMath
language: en
version:  1.0.0
comment:  A five-minute probability lesson about replacing a counter, with three predictions and an answer key.
-->

# Two draws, one bag

[हिन्दी में पढ़ें · Read this lesson in Hindi](https://liascript.github.io/course/?https://raw.githubusercontent.com/lmo0317/modumath-probability-lab/main/hi.md)

A bag holds two blue counters and one yellow counter. You draw one without looking. Before you reach in again, someone asks: “What is the chance of blue now?”

One detail is missing. Did the first counter go back in?

This five-minute activity from the [ModuMath team](https://math.hjinlabs.com/?lang=en) works with three scraps of paper. You can also do it entirely on screen. Write **B1**, **B2**, and **Y** to keep the two blues distinguishable.

## Make a prediction

The first counter was blue and stays on the table. What is the chance that the next counter is blue?

[( )] Two thirds, because two of the original counters were blue.
[(X)] One half, because one blue and one yellow are left.
[( )] One third, because one blue is left and we started with three counters.

Put the first blue back and mix the bag. The second draw now has three possibilities again. Two of them are blue, so the probability changes to 2/3.

## Ask about both draws

Start again with B1, B2 and Y. Keep the first counter out. Before either draw, how likely is it that **both** counters will be blue?

[( )] 1/2
[(X)] 1/3
[( )] 4/9

Every ordered pair below is equally likely. Read each row as a first draw followed by a second draw.

| First | Possible second draws |
| ----- | --------------------- |
| B1    | B2 or Y               |
| B2    | B1 or Y               |
| Y     | B1 or B2              |

Only B1 → B2 and B2 → B1 work. That is 2 of the 6 paths, or 1/3. Multiplying along the blue branch gives the same result: (2/3) × (1/2) = 1/3. With replacement the second factor would be 2/3, giving 4/9.

## A related problem

This time you have **three green** counters and **two orange** ones. You want two greens, and the first counter stays out. Which product represents the probability?

[( )] (3/5) × (3/5)
[(X)] (3/5) × (2/4)
[( )] (3/5) + (2/4)

The first green leaves two greens among four counters. The result is 6/20 = 3/10. Change just one rule and put the first counter back: the result becomes 9/25.

## A check you can reuse

1. Say what is in the bag before the first event.
2. Describe what remains **after the event you care about**.
3. For a particular path, multiply the probabilities along it.

If a later line in a different maths question is where you get stuck, [ModuMath](https://math.hjinlabs.com/?lang=en) lets you enter the question, read an explanation of that step and try a related exercise. The lesson above is free to use without signing in. The separate app requires sign-in for its AI features.
