import argparse
import math


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", type=str)
    parser.add_argument("--payment", type=float)
    parser.add_argument("--principal", type=float)
    parser.add_argument("--periods", type=int)
    parser.add_argument("--interest", type=float)
    return parser.parse_args()


def calculate_annuity_payment(principal, periods, interest):
    i = interest / (12 * 100)
    payment = principal * i * pow(1 + i, periods) / (pow(1 + i, periods) - 1)
    return math.ceil(payment)


def calculate_annuity_principal(payment, periods, interest):
    i = interest / (12 * 100)
    principal = payment / (i * pow(1 + i, periods) / (pow(1 + i, periods) - 1))
    return math.floor(principal)


def calculate_annuity_periods(principal, payment, interest):
    i = interest / (12 * 100)
    periods = math.log(payment / (payment - i * principal), 1 + i)
    return math.ceil(periods)


def calculate_differentiated_payment(principal, periods, interest):
    i = interest / (12 * 100)
    total_payment = 0
    for m in range(1, periods + 1):
        payment = math.ceil(principal / periods + i * (principal - (principal * (m - 1)) / periods))
        total_payment += payment
        print(f"Month {m}: payment is {int(payment)}")
    return int(total_payment - principal)


def main():
    args = parse_arguments()
    type_ = args.type
    payment = args.payment
    principal = args.principal
    periods = args.periods
    interest = args.interest

    if type_ is None or interest is None:
        print("Incorrect parameters")
        return

    if type_ == "diff":
        if payment is not None:
            print("Incorrect parameters")
            return
        else:
            overpayment = calculate_differentiated_payment(principal, periods, interest)
            print(f"Overpayment = {overpayment}")
    elif type_ == "annuity":
        if payment is None:
            if principal is None or periods is None:
                print("Incorrect parameters")
                return
            payment = calculate_annuity_payment(principal, periods, interest)
            print(f"Your annuity payment = {int(payment)}!")
        elif principal is None:
            if periods is None:
                print("Incorrect parameters")
                return
            principal = calculate_annuity_principal(payment, periods, interest)
            print(f"Your credit principal = {int(principal)}!")
        elif periods is None:
            periods = calculate_annuity_periods(principal, payment, interest)
            overpayment = int(payment * periods - principal)
            years = periods // 12
            months = periods % 12
            if years == 0:
                print(f"You need {months} months to repay this credit!")
            elif months == 0:
                print(f"You need {years} years to repay this credit!")
                print(f"Overpayment = {overpayment}")
            else:
                print(f"You need {years} years and {months} months to repay this credit!")
        else:
            print("Incorrect parameters")
            return
    else:
        print("Incorrect parameters")
        return


if __name__ == "__main__":
    main()