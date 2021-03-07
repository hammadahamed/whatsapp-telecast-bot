val = input()
x,y = val.split(" ")

x = int(x)
y = int(y)
# print(x)
# print(y)
count = 0

for n in range (x,y+1):
    for h in range(0,24):
        if h>=0 and h < 10:
            h = '0'+str(h)
        for m in range(0,60):
            if m >= 0 and m < 10:
                m = '0'+str(m)
            for s in range(0,60):
                if s >= 0 and s < 10:
                    s = '0'+str(s)
                # print("{}{}{}{}".format(n,h,m,s))
                data = str(n)+str(h)+str(m)+str(s)
                data = data.strip()

                # data = "".join([n,h,m,s])
                revdata = data[::-1]
                data = int(data)
                revdata = int(revdata)

                # print(data)
                # print(revdata)
                # print(type(data))
                # print(type(revdata))

                # break
                # break
                # break
                if (int(data) == int(revdata)):
                    # print(data)
                    # print("matched !!!!!!!!!!!! ")
                    count+=1

print(count)

