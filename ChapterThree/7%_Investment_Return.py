principal_int = 1000
rate_float = 7/100

for year in range(1, 31):
    amount_nth = principal_int * (1 + rate_float) ** year
    print(f'The amount for year {year:>2} is {amount_nth:>5.2f}')