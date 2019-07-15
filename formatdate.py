import datetime

def return_monthNumber(month):
    switcher = {
        "janeiro": 1,
        "fevereiro": 2,
        "março": 3,
        "abril": 4,
        "maio": 5,
        "junho": 6,
        "julho": 7,
        "agosto": 8,
        "setembro": 9,
        "outubro": 10,
        "novembro": 11,
        "dezembro": 12
    }
    return switcher.get(month, "Invalid month")

def format_date(datefull):
    try:
        dtsplittedByComma = datefull.split(",")
        dtWithPrep = dtsplittedByComma[1].strip()
        dtsplittedByPrep = dtWithPrep.split("de")
        day = dtsplittedByPrep[0].strip()
        month = dtsplittedByPrep[1].strip()
        monthNumber = return_monthNumber(month)
        year = dtsplittedByPrep[2].strip()
        # Sábado, 6 de julho de 2019 de 20:00 a 05:00 UTC-03 vs Domingo, 14 de julho de 2019 às 17:00 UTC-03
        if "às" in year:
            yearSplitted = year.split("às")
            year = yearSplitted[0].strip()
            timeSplitted = yearSplitted[1].strip().split(" ")
            time =  timeSplitted[0]
        else:
            time = dtsplittedByPrep[3]
		# /fix inconsistência na data por extenso
        timeSplitted = time.split("a")
        timeSplitted2 = timeSplitted[0].strip().split(":")
        hour = timeSplitted2[0]
        minute = timeSplitted2[1]

        dateformatted = datetime.datetime(int(year), monthNumber, int(day), int(hour), int(minute), 00)
        return dateformatted
    except:
        return "ERROR"