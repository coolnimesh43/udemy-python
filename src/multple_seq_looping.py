a = ["a", "b", "c"]
b = ["1", "2", "3"]
c = ["Mercury", "Venus", "Mars"]
d = [1.1, 1.2, 1.3]

for i, j , k, l in zip(a, b, c, d):
    print(i, j , k , l)
    print(" %s is %s, %s density is %s compare to Earth" % (i, j, k, l))
