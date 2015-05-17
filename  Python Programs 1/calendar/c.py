def get_days(year, month):
    """
    take year and month ,return the days in that month.
    """
    #define a dictionary and the month is key which value is days 
    daydict = dict()    
    daydict = ['january'=31, 'february'=28, 'februaryinleapyear'=29,
                                        'march'=31, 'april'=30,
                                        'may'=31, 'june'=30,
                                        'july'=31, 'august'=31,
                                        'september'=30, 'october'=31,
                                        'november'=30, 'december'=31 ]

    try:
        if month in daydict:
            if month == 'february' and leap_year(year):     
                print daydict[februaryinleapyear] 
            else:
                print daydict[month]
        else:
            print 'The year or month you input is invalid !'
    except:
        print 'error!'
