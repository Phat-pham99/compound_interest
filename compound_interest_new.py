from rich import print
import re
def com_int(init: int, n: int, rate: float, time: int):
    Amount = init * ((1 + rate / n) ** (n * time))
    Amount = int(Amount)
    bb = Amount - init
    cc = init * rate * time
    cc = int(cc)
    dd = bb / cc * 100
    dd = round(dd, 2)
    print("+----------------------------+")
    print(f"Initial Principle {'{0:,}'.format(init)}")
    print(f"Total {'{0:,}'.format(Amount)} ")
    print(f"Compound Interest {'{0:,}'.format(bb)}")
    print(">---<")
    print(f"Simple Interest {'{0:,}'.format(cc)}")
    print(f"CI/SI {'{0:,}'.format(dd)} %")
    print("+------------------------------+")
    return Amount

def each_month(init: int, Principal_month: int, rate: float, time: int, verbose = False):
    """
    P : the principal amount you invest each month
    r : Interest per year
    t : number of months
    """
    print("+------------------------------+")
    result = init
    for i in range(1, time + 1):
        result_new = (result + Principal_month) * (1 + rate / 12)
        # result = int(round(result, -3))
        # result1 = '{0:,}'.format(result)
        if verbose == "Y":
            print(f" + Month # [red]{i}[/red]| [green]{ '{0:,}'.format(int(round(result_new, -3)))}[/green]| [blue]{'{0:,}'.format(int(round(result_new - result - Principal_month,-3)))}[/blue]")
        else :
            print(f" + Month # [red]{i}[/red]| [green]{'{0:,}'.format(int(round(result_new, -3)))}[/green]")
        result = result_new

    print("+------------------------------+")
    basse = int(round(init + Principal_month * time))
    diff = result - basse
    basse1 = '{0:,}'.format(basse)
    diff1 = '{0:,}'.format(diff)
    print(f" Total if CI : {'{0:,}'.format(int(round(result_new, -3)))}")
    print(" Total if stack : {}".format(basse1))
    print(" The difference is {}".format(diff1))
    print("+------------------------------+")
    return result

# Common part
if __name__ == "__main__":
    print("If you want to calculate compound interest from initial Principle, press 1")
    print("If you want to calculate CI on investment each month, press 2")
    choice = input("Here : ")
    init = input("Initial Principle : ")
    init = float(init)
    r = input("Interest rate : ")
    r = eval(r)
    r = float(r)
    if choice == "1":
        t= input("Time of investment (YEARS): ")
        n = 365
    if choice == "2":
        P = input("Investment each month : ")
        P = eval(P)
        P = int(P)
        t = input("Time of investment (MONTHS) : ")
        verbose = input("Do you want to show verbose (Y/N) ?")
    t = eval(t)
    t = int(t)
    #########################
    total = 0
    if choice == "1":
        total = com_int(init=init, n=n, rate=r, time=t)
    elif choice == "2":
        total = each_month(init=init, Principal_month=P, rate=r, time=t, verbose=verbose)
        print("Do you want to keep investing ?")
        jj = input("Press y or n :      ")
        print("+------------------------------+")
        if jj == "y":
            #########################
            P1 = input("Investment each month : ")
            P1 = eval(P1)
            P1 = int(P1)
            r1 = input("Interest rate : ")
            r1 = eval(r1)
            r1 = float(r1)
            t1 = input("Time of investment : ")
            t1 = eval(t1)
            t1 = int(t1)
            #########################
            later = each_month(total, P1, r1, t1, verbose='Y')
        else:
            pass
    else:
        print(" +------------------------------+ ")
        print("ERROR")
