## Problem Fourteen

### Statement

The following iterative sequence is defined for the set of positive integers:
<pre>
	n → n/2 (n is even)
	n → 3n + 1 (n is odd)
</pre>
Using the rule above and starting with 13, we generate the following sequence:

<pre>	13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1</pre>
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?

**Resolve:**
The first step is calculate the sequence collatz, futhermore I calculate the longest chain, If the long chain is the maximum then I am going to save the number.
