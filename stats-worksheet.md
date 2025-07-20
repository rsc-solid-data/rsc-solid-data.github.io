---
layout: default
title: Maths, Statistics, and Programming Worksheet
---

# Linear Algebra

The ability to rotate a molecule in space is an important aspect in computational chemistry. 
Indeed, tools such as machine learning interatomic potentials are build on the use of what are called rotation matrices. 
A rotation matrix is a linear transformation that describes rotation of a series of vectors, the atomic positions of some atoms. 
The rotation matrix for an anti-clockwise rotation in a two-dimensional *xy*-plane is as follows, 

$$
\mathbf{R} = \begin{bmatrix} \cos{\theta} & -\sin{\theta} \\ \sin{\theta} & \cos{\theta} \end{bmatrix}.
$$

A text file with *x* and *y* coordinates of a water molecule is available for download [here](./water.txt). 
This file looks like that shown below. 

```
# water molecule xy
# x y
0 0
-0.82 -0.48
0.82 -0.48
```

After the first two lines, which are comments describing the file, there are three lines of coordinates. 
The first line is the *x* and *y* positions of the oxygen molecule and then the next lines are the same for the two hydrogen atoms. 
Therefore, if plotted on *x* and *y*-axes, the oxygen atom would sit at the origin, $(0, 0)$, and the hydrogen atoms at $(-0.82, -0.48)$ and $(0.82, -0.48)$. 
The atomic positions of the water molecule can be read using [`np.loadtxt`](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt). 

To visualise the water molecule, the [`visualisation.py`](./visualisation.py) module can be downloaded and imported as a module. 
This module includes the `visualisation.show()` function, to which the atomic positions should be passed. 

Create a Python function that will rotate the water molecule using the rotation matrix defined above. 
Use the `visualisation.show` function to check the rotation has worked correctly. 

