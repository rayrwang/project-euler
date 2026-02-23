


if __name__ == "__main__":
    day = 1 + 365  # 1901 Jan 1 (1900 Jan 1 was Monday)
    count = 0
    for year in range(1901, 2000+1):
        for month in range(1, 12+1):
            if day % 7 == 0:
                count += 1

            if month in [9, 4, 6, 11]:
                days = 30
            elif month == 2:
                is_leap = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
                days = 29 if is_leap else 28
            else:
                days = 31
            day += days
    print(count)  # 171
