# Delaunay-Triangulation 2D

Traingulation is creating a mesh of traingles based on given set of points on rules:
- Each Edge is connected to only and only 2 points.
- edges can't cross each other in different way than in points.

In this example we creating a triangulation of Simple Polygon, so another rules must be added:
- Points must stay the same, No point can be erased nor added.
- All Edges from Polygon must be in triangulation.

The algorythm used is iterative version of Delanuay Triangulation.
