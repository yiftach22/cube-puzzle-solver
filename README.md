In a little Christmas market in Italy, I found this beautiful hand-made wood cube puzzle.
The kind that each piece is different, and there is only one way to arrange the pieces into a cube.
I bought it already solved, in its original wood box.

The first thing I did when coming back home, was taking everything out, without even taking a picture of the solved cube.
That was a mistake.

The 3*3 or 4*4 versions of this are pretty easy, or at least solvable, and if you get stuck - there are tons of youtubes on this.
But the 5*5 was just too much. whatever I tried, didn't work.

And the worst part - you can't put the pieces back in the box if you can't solve it!

So then I decided - let python do the dirty work for me.



Language and tools: Python, Numpy, Matplotlib for visualization

Algorithmic Approach

The core of the solution is a brute-force approach optimized by key algorithmic and data structure choices, crucial for efficiently navigating the vast search space:

1. Recursive Backtracking: The solve function uses a Depth-First Search (DFS) with recursive backtracking. It attempts to place pieces into the next available empty cell (empty_spots), and if a path leads to a dead-end, it efficiently backtracks to the previous valid state.

2. Symmetry and Rotation Management: The all_rotations function generates all 24 possible spatial rotations for each piece before the search begins. This pre-calculation and removal of duplicate forms minimize the search space during the runtime.

3. Optimized Placement Check: The check_placement function leverages NumPy’s vectorized operations. Instead of slow, explicit Python loops, it performs an element-wise multiplication on the placed piece and the current board state. Overlaps are instantly detected when the result contains a negative value, ensuring near-optimal performance for placement validation.



Key Implementation Highlights
- 3D Array Management: The cube is represented as a CUBE_SIZE x CUBE_SIZE x CUBE_SIZE **NumPy array**, allowing for intuitive indexing and fast manipulation of the 3D grid.
- Vectorized Overlap Detection: Placement verification is highly optimized using NumPy.
- Dynamic Piece Handling: Pieces are dynamically padded (np.zeros) and rotated/rolled (np.roll) to efficiently check every possible placement combination on the board.

Result Visualization
- The final solution is visualized using Matplotlib's voxels function, clearly displaying the solved cube with each of the 13 unique parts rendered in a distinct color .
