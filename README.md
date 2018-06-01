# Matrix-Determinant
Solution to algorithm challenge posted here (https://www.codewars.com/kata/52a382ee44408cea2500074c) by user pjfranzini.  Coded in Python 3 by Cj Maxwell in May 2017.


Write a function that accepts a square matrix (n x n 2D array) and returns the determinant of the matrix.

How to take the determinant of a matrix -- it is simplest to start with the smallest cases: A 1x1 matrix |a| has determinant a. A 2x2 matrix [[a, b], [c, d]] or

|a b|
|c d|

has determinant ad - bc.

The determinant of an n x n sized matrix is calculated by reducing the problem to the calculation of the determinants of n n-1 x n-1 matrices. For the 3x3 case, [[a, b, c], [d, e, f], [g, h, i]] or

|a b c|
|d e f|
|g h i|

the determinant is: a * det(a_minor) - b * det(b_minor) + c * det(c_minor) where det(a_minor) refers to taking the determinant of the 2x2 matrix created by crossing out the row and column in which the element a occurs, or

|e f|
|h i|

Note the alternation of signs.

The determinant of larger matrices are calculated analogously, e.g. if M is a 4x4 matrix with first row [a, b, c, d], det(M) = a * det(a_minor) - b * det(b_minor) + c * det(c_minor) - d * det(d_minor)
