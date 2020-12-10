#DP implementation
import time

def nFib(n):
	if n <= 2:
		f = 1;
	else: 
		f = nFib(n-1) + nFib(n-2)
	return f

def dpFib(n):
	if n in memo:
		return memo[n]
	else:
		if n <= 2:
			f = 1;
		else: 
			f = dpFib(n-1) + dpFib(n-2)
		memo[n] = f
		return f

memo={}

num = input("Enter number:")
num = int(num)

print("Running the DP function!")
dpStart = time.time()
dpresult = dpFib(num)
dpEnd = time.time()
dpTime = dpEnd - dpStart
print("DP fib(n) = " + str(dpresult))
print("DP function finished in " + str(dpTime) + " seconds")
print("\n")

if num <= 50:
    print("Running the naive function!")
else:
    print("Running the naive function... You picked a large n, so this may take a while...")
nStart = time.time()
nresult = nFib(num)
nEnd = time.time()
nTime = nEnd - nStart
print("naive fib(n) = " + str(nresult))
print("naive function finished in " + str(nTime) + " seconds")

if nTime > dpTime:
    print("\n")
    print("the DP function ran " + str(nTime/dpTime * 100) + " times faster than the naive function!")
