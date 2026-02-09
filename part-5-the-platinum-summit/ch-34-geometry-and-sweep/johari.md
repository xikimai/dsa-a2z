# Johari Window: Chapter 34 — Computational Geometry & Sweep Line

Use this worksheet **before** and **after** studying the chapter. Be honest — there are no wrong answers! This is a tool for YOU to track your own growth.

---

## Before This Chapter

Think about what you already know (or think you know) about computational geometry and sweep line algorithms.

### Open (I know well)
> Things I'm confident I understand:
> - [ ] What coordinates are and how to plot points on a 2D plane
> - [ ] The Pythagorean theorem for distance between two points
> - [ ] What "convex" means intuitively (no dents in the shape)
> - [ ] Sorting algorithms and their time complexities (from Ch 8)
> - [ ] Stack data structure and monotone stacks (from Ch 22)
> - [ ] _________________________________

### Hidden (I think I know but I'm not sure)
> Things I've heard of but couldn't explain clearly:
> - [ ] What a "cross product" is and how it relates to geometry
> - [ ] What a "convex hull" is and how to compute one
> - [ ] How sweep line algorithms work
> - [ ] The Shoelace formula for polygon area
> - [ ] _________________________________

### Blind Spot (I know I don't know)
> Things I know exist but have not learned:
> - [ ] How to determine if two line segments intersect using cross products
> - [ ] Divide and conquer approach to closest pair of points
> - [ ] Ray casting algorithm for point-in-polygon queries
> - [ ] Coordinate compression for sweep line problems
> - [ ] _________________________________

### Unknown (I have not even thought about)
> Things I don't know that I don't know — leave blank now, fill in after!
> - [ ] _________________________________
> - [ ] _________________________________
> - [ ] _________________________________

---

## After This Chapter

Come back here after finishing the chapter. Compare with your "Before" answers!

### Open — Expanded (Now I truly understand)
> - [ ] Cross product: (B.x-A.x)*(C.y-A.y) - (B.y-A.y)*(C.x-A.x) — positive=CCW, negative=CW, zero=collinear
> - [ ] Convex hull via Andrew's Monotone Chain: sort, build lower hull, build upper hull, combine
> - [ ] Line segment intersection: check orientations at both endpoints of both segments
> - [ ] Shoelace formula: sum x_i*y_{i+1} - x_{i+1}*y_i, divide by 2, take absolute value
> - [ ] Closest pair: divide and conquer, only check strip of width 2*delta, at most 6-7 comparisons per point
> - [ ] Point in polygon: ray casting — count crossings, odd=inside, even=outside
> - [ ] Sweep line: sort events by x, maintain active structure, process left to right
> - [ ] Rectangle union area: sweep line with coordinate compression on y-values
> - [ ] _________________________________

### Surprised Me! (was Unknown/Blind Spot, now Open)
> - [ ] That the cross product is THE fundamental tool for almost all 2D geometry
> - [ ] That you can compute polygon area with just coordinates and no trigonometry
> - [ ] That the closest pair problem has only 6-7 points to check in the strip (not O(n))
> - [ ] That integer overflow is a major practical concern in geometry (coordinates multiply!)
> - [ ] _________________________________

### Still Working On (honest self-assessment)
> - [ ] Handling all the edge cases in line segment intersection (collinear, touching endpoints)
> - [ ] Implementing convex hull without bugs on the first try
> - [ ] Knowing when to use integers vs. floating point in geometry problems
> - [ ] Recognizing which geometry technique to apply for a given problem
> - [ ] _________________________________

### Questions I Now Have (new curiosity!)
> - [ ] How does 3D convex hull work? Is it fundamentally different from 2D?
> - [ ] What are Voronoi diagrams and Delaunay triangulations used for?
> - [ ] Can sweep line be applied to curved shapes, not just rectangles?
> - [ ] How do real mapping/GIS applications handle geometry at scale?
> - [ ] _________________________________

---

**You have completed the FINAL Johari Window of the entire workbook!** Look back at your very first Johari Window from Chapter 0 and compare. The growth you see is real. You have earned every bit of it.
