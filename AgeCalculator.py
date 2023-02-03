def AgeCalculator(year, month, date):
    import datetime
    todays_date = datetime.datetime.now().date()
    birth_date = datetime.date(year, month, date)
    age_of_person = (todays_date - birth_date)/365.25
    print(age_of_person)

AgeCalculator(2003, 11, 27)
