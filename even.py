print("Up to which even number do you want? ", end = "")
n = int(input())
print("Even numbers up to", n, "are: ", end = "")
print(list(range(0,n,2)))
