test_dite = {'codingal':2,'is':2,'best':2,'for':2,'coding':1}

print("the origen :" + str(test_dite))

k=2

res =0
for key in test_dite:
    if test_dite[key] == k:
        res = res +1

print("ferquncy of k is:"+str(res))
    