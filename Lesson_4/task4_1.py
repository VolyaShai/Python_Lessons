from sys import argv


def result():
    try:
        hours, rate_per_hour, premium = map(float, argv[1:])
        print("Result:", hours * rate_per_hour + premium)
    except ValueError:
        print("Enter the numbers!")


result()
