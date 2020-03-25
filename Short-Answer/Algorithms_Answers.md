#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(a * n)



b) O(n^2)


c) O(2^n)

## Exercise II
(step 1)
Go to the floor that is in the middle of the building (if n == 100, go to floor 50).

(step 2)
Drop the egg.

(step 3)
Do one or the other:
-->If it breaks, go to the floor that is the halfway point between you and the ground. If we're on our first cycle and n == 100, floor 25.
-->If it DOESNT break, go to the floor that is the halfway point between you and the top of the building. If we're on our first cycle and n == 100, floor 75.

Repeat steps 2 through 3, continually halving what floor your on until f == broken egg and f-1 == unbroken egg

I think this is something akin to binary search, so the worst case would run in logarithmic time being O(log n)