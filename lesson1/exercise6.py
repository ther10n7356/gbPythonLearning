proceed = int(input("Enter proceed: "))
cost = int(input("Enter cost: "))

if proceed > cost:
    prof = (proceed - cost)/proceed*100
    cnt_emp = int(input("Enter the number of employees: "))
    proc_emp = (proceed - cost)//cnt_emp
    print("Profitability: {0:.2f}".format(prof))
    print("Net income per employee: ", proc_emp)
else:
    print("Losses")
