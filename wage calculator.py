name = input('enter your name: ')
hours_worked = int(input('enter the hours worked: '))


def salary(name, hours_worked):

    def gross_pay():
        rate = 200
        gross = hours_worked*rate/100
        return gross

    def tax():
        gross = gross_pay()
        tax = 22
        taxation = gross*tax/100

        return taxation

    def net_pay():
        taxation = tax()
        gross = gross_pay()
        net = gross-taxation
        return net

    print(f'your gross pay is {gross_pay()}')
    print(f'your tax is {tax()}')
    print(f'your net pay is {net_pay()}')


salary(name, hours_worked)
