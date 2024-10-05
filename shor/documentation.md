# Shor's Algorithm

Shor's Algorithm is one built for factoring a number in sub-exponential time - the current best of classical computation. The quantum part of the algorithm is the order-finding circuit introduced in [hod.py](hod.py), in step 5 of the algorithm. The remaining steps rely largely on a lemma from number theory which we state but do not prove.

Before doing so we recall that classical algorithms are efficient for:
- computing hcf of two integers ([Euclid's Alogrithm](euclid.py))
- determining if an integer is prime ([Miller-Rabin primality test](primality.py))
- determining if an integer is even (last digit is 0 in binary expansion)
- determining if an integer can be written as a perfect power (power ≥2, [powerCheck.py](powerCheck.py)).

Now the lemma we will use is as follows:

> Let $y$ and $R$ be natural numbers such that
> - $R$ is not prime;
> - the order $r$ of $y$ modulo $R$ is even;
> - $y^{r/2}>R$.
> Then either $y^{r/2}+1$ is divisible by $R$, or both $\text{hcf}(y^{r/2}-1,R)$ and $\text{hcf}(y^{r/2}+1,R)$ are non-trivial factors of $R$.

Another important result to be aware of is:

> Let $R$ be an odd natural number with $m\geq2$ distinct prime factors. If $y$ is chosen uniformly at random from the set of natural numbers coprime to and smaller than $R$, then the probability that the order $r$ of $y$ modulo $R$ is even and satisfies  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $y^{r/2} \not\equiv-1 \text{ mod }R$  
> is at least  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $1-\frac{1}{2^m-1}$.

With these in mind, we can see that if $R$ is odd then a random number chosen from those coprime and less than it will, with high probability, have easily constructible factors of $R$ produced by it.

With all of this in mind we move to the algorithm.

> ### Shor's Algorithm (factoring the natural number $R$)
> 1. Check that $R$ is not prime.  
> *If so, stop and return* $R$.
> 2. Check if $R$ is even.  
> *If so, stop and return* $2$.
> 3. Check if $R=a^b$ for some integers $a\geq1$ and $b\geq2$.  
> *If so, stop and return* $a$.
> 4. Uniformly at random pick an integer $1<y<R$ and evaluate $\text{hcf}(y,R)$.  
> *If* $\text{hcf}(y,R)>1$, *we can stop and return this factor.*
> 5. Compute the order $r$ of $y$ modulo $R$ via [hidden-order determination](hod.py).
> 6. Check if $r$ is odd.  
> *If so, return to step 4.*
> 7. Check if $y^{r/2}\equiv-1\text{ mod }R$.  
> *If so, return to step 4.*
> 8. Compute $\text{hcf}(y^{r/2}-1,R)$ and $\text{hcf}(y^{r/2}+1,R)$.  
> *Stop and return these factors.*

Steps 1 to 3 are easy preliminary checks, steps 4, 6 and 7 are checking the necessary conditions of the first lemma above in order to apply 8, and step 5 is where we use quantum circuits to calculate the order of $y$ modulo $R$. Due to the fact that steps 6 and 7 will pass with probability $1-1/(2^m-1)$, we can be assured of not getting stuck in an infinite loop.