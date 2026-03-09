import time

def fibo(n):
    if n <= 1: return n
    return fibo(n-1) + fibo(n-2)

start = time.time()
res = fibo(40)
print(f"Python Result: {res} | Time: {time.time() - start:.4f} s")
