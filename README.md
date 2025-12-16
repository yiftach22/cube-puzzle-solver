In a little Christmas market in Italy, I found this beautiful hand-made wood cube puzzle.
The kind that each piece is different, and there is only one way to arrange the pieces into a cube.
I bought it already solved, in its original wood box.

The first thing I did when coming back home, was taking everything out, without even taking a picture of the solved cube.
That was a mistake.

The 3*3 or 4*4 versions of this are pretty easy, or at least solvable, and if you get stuck - there are tons of youtubes on this.
But the 5*5 was just too much. whatever I tried, didn't work.

And the worst part - you can't put the pieces back in the box if you can't solve it!

So then I decided - let python do the dirty work for me.



The solver is a classical optimized backtracking algorithm. It find an empty spot in the lowest possible row, and tries to fit different pieces into it.
Once it puts a piece, it moves to the next one, until it is stuck and have to go back - or unil it succeeds.

The program can shows the progress visually every 500 steps.

When finished, it visualises the solution on 3D piece by piece.

I used Numpy for represinting and manipulating the 3D cube and pieces.
