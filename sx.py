def perebir(lst):
    a = []
    for i in range(len(lst)- 2):
        for j in range(i+1, len(lst) -1):
            for k in range(j+1, len(lst)):
                a.append([lst[i], lst[j], lst[k]])
    print(a)
perebir([1,2,3,4,5])