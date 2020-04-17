def getgdelt(year_start,month_start,day_start,year_end,month_end,day_end):
    import webbrowser

    url1 = 'http://data.gdeltproject.org/events/'
    url2 = '.export.CSV.zip'
    year = year_start
    month = month_start
    day = day_start
    num = 0
    gdeltlist = []
    while year < year_end + 1:
        if year < year_end:
            while month < 13:
                while month < 10:
                    while day < 32:
                        while day < 10:
                            url = url1 + str(year) + '0' + str(month) + '0' + str(day) + url2
                            gdeltlist.insert(num, url)
                            day += 1
                            num += 1
                            print(url)
                        else:
                            url = url1 + str(year) + '0' + str(month) + str(day) + url2
                            gdeltlist.insert(num, url)
                            day += 1
                            num += 1
                            print(url)
                    else:
                        month += 1
                        num += 1
                        day = 1
                else:
                    while day < 32:
                        while day < 10:
                            url = url1 + str(year)+ str(month) + '0' + str(day) + url2
                            gdeltlist.insert(num, url)
                            day += 1
                            num += 1
                            print(url)
                        else:
                            url = url1 + str(year) + str(month) + str(day) + url2
                            gdeltlist.insert(num, url)
                            day += 1
                            num += 1
                            print(url)
                    else:
                        month += 1
                        num += 1
                        day = 1
            else:
                year += 1
                month = 1
                day = 1
                num += 1

        else:
            if month < month_end:
                while month < 10 and month < month_end:
                    while day < 32:
                        while day < 10:
                            url = url1 + str(year) + '0' + str(month) + '0' + str(day) + url2
                            gdeltlist.insert(num, url)
                            day += 1
                            num += 1
                            print(url)
                        else:
                            url = url1 + str(year) + '0' + str(month) + str(day) + url2
                            gdeltlist.insert(num, url)
                            day += 1
                            num += 1
                            print(url)
                    else:
                        month += 1
                        num += 1
                        day = 1
                else:
                    while day < 32 and month < month_end:
                        while day < 10:
                            url = url1 + str(year) + str(month) + '0' + str(day) + url2
                            gdeltlist.insert(num, url)
                            day += 1
                            num += 1
                            print(url)
                        else:
                            url = url1 + str(year) + str(month) + str(day) + url2
                            gdeltlist.insert(num, url)
                            day += 1
                            num += 1
                            print(url)
                    else:
                        month += 1
                        num += 1
                        day = 1
            elif month == month_end:
                while month < 10 and month == month_end:
                    while day < day_end + 1:
                        while day < 10 and day < day_end + 1:
                            url = url1 + str(year) + '0' + str(month) + '0' + str(day) + url2
                            gdeltlist.insert(num, url)
                            day += 1
                            num += 1
                            print(url)
                        else:
                            if day < day_end + 1:
                                url = url1 + str(year) + '0' + str(month) + str(day) + url2
                                gdeltlist.insert(num, url)
                                day += 1
                                num += 1
                                print(url)
                            else:
                                day += 1
                                num += 1
                    else:
                        month += 1
                        num += 1
                        day = 1
                else:
                    while day < day_end + 1 and day < day_end + 1 and month == month_end:
                        while day < 10:
                            url = url1 + str(year) + str(month) + '0' + str(day) + url2
                            gdeltlist.insert(num, url)
                            day += 1
                            num += 1
                            print(url)
                        else:
                            url = url1 + str(year) + str(month) + str(day) + url2
                            gdeltlist.insert(num, url)
                            day += 1
                            num += 1
                            print(url)
                    else:
                        month += 1
                        num += 1
                        day = 1
            else:
                year += 1
                month = 1
                day = 1
                num += 1

    for webpage in gdeltlist:
        webbrowser.open(webpage)