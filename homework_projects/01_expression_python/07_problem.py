
YEARLY_DAYS : int = 365
DAILY_HOURS : int = 24
HOURLY_MIN :int = 60
SEC_IN_MIN : int = 60


def main():

    sec_in_year : int = (SEC_IN_MIN * HOURLY_MIN * DAILY_HOURS * YEARLY_DAYS)
    print(f"there are {sec_in_year} seconds in a year" )


if __name__ == '__main__':
    main()