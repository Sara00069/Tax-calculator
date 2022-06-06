print("1.Women and Citizens with age > 65")
print("2.Disabled")
print("3.Parents of disabled pay")
print("4.wounded freedom fighters")
print("5.others")
tax = 0.0
choice = int(input('Enter your category: '))
inc = float(input('Enter your income= '))

if choice == 1:
    if inc <= 350000:
        print("Tax = 0%")
    elif inc <= 450000:
        tax = (inc - 350000)*0.05
        print("Tax = ", tax)
elif choice == 2:
    if inc <= 450000:
        print("Tax = 0 TK")
elif choice == 3:
    if inc <= 350000:
        print("Tax = 0 TK")
elif choice == 4:
    if inc <= 4750000:
        print("Tax = 0 TK")
elif choice == 5:
    if inc <= 300000:
        print("Tax = 0 TK")
    elif inc <= 400000:
        tax = (inc - 300000)*0.05
        print("Tax = ", tax)

    elif inc <= 700000:
        tax = 5000 + (inc - 400000)*0.1
        print("Tax = ", tax)

    elif inc <= 1100000:
        tax = 5000+30000+(inc - 700000)*0.15
        print("Tax = ", tax)

    elif inc <= 1600000:
        tax = 5000+30000+60000 + (inc - 1100000)*0.2
        print("Tax = ", tax)
    elif inc > 1600000:
        tax = 5000+30000+60000+100000+(inc - 1600000)*0.25
        print("Tax = ", tax)
