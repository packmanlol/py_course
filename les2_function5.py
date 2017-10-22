def averanger():
    sum = 0
    kol = 0
    def coun(val):
        nonlocal sum, kol
        sum += val
        kol += 1
        print(sum / kol)
    return coun
func = averanger()

for i in range(1,43,11):
    func(i)

