with open('Salary.txt', 'r', encoding = 'utf-8') as f:
    # text = f.read()
    e = []
    for line in f:
        e = line.split()
        for i in e:
            for j in i:
                print(i[j])
                #if j == 1:
                    #i[j] = int(i[j])
                    #print(i[j])
            #     if j[1] < 20000:
            #         print(j[0])
        # e[1] = int(e[1])
        # if e[1] < 20000:
        #     print(e[0])
        #print(e)
    # print(text)