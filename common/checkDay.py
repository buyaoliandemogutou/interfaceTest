b = 0
date=4540
while date > 0:
    date = date - date * 0.002
    b = b + 1
    if date <=0:
        break
print('/n',b)