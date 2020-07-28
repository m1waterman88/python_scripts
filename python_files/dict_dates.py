# dictionary: key:value pairs

month = str(input("Enter month: ")).casefold()
monthConversions = {
    "January".casefold(): "January",
    "Jan".casefold(): "January",
    "1": "January",
    "01": "January",

    "February".casefold(): "February",
    "Feb".casefold(): "February",
    "2": "February",
    "02": "February",

    "March".casefold(): "March",
    "Mar".casefold(): "March",
    "3": "March",
    "03": "March",

    "April".casefold(): "April",
    "Apr".casefold(): "April",
    "4": "April",
    "04": "April",

    "May".casefold(): "May",
    "5": "May",
    "05": "May",

    "June".casefold(): "June",
    "Jun".casefold(): "June",
    "6": "June",
    "06": "June",

    "July".casefold(): "July",
    "Jul".casefold(): "July",
    "7": "July",
    "07": "July",

    "August".casefold(): "August",
    "Aug".casefold(): "August",
    "8": "August",
    "08": "August",

    "September".casefold(): "September",
    "Sep".casefold(): "September",
    "9": "September",
    "09": "September",

    "October".casefold(): "October",
    "Oct".casefold(): "October",
    "10": "October",

    "November".casefold(): "November",
    "Nov".casefold(): "November",
    "11": "November",

    "December".casefold(): "December",
    "Dec".casefold(): "December",
    "12": "December",
}


day = str(input("Enter day: "))
dayConversions = {}
dayList = str([*range(1, 32)])
if day in dayList:
    dayConversions[day] = day
elif day[0] == "0":
    dayConversions[day] = str(int(day))
    # convert value to integer since leading zeroes are removed, and then
    # back to string since it has to be for concatenation

# Need to program for # days in month

year = str(input("Enter year: "))
yearConversions = {
    "10": "2010", "2010": "2010",
    "11": "2011", "2011": "2011",
    "12": "2012", "2012": "2012",
    "13": "2013", "2013": "2013",
    "14": "2014", "2014": "2014",
    "15": "2015", "2015": "2015",
    "16": "2016", "2016": "2016",
    "17": "2017", "2017": "2017",
    "18": "2018", "2018": "2018",
    "19": "2019", "2019": "2019",
    "20": "2020", "2020": "2020",
}


print("", "Today is: ", sep="\n")
print(f"{monthConversions.get(month, '--Invalid month--')} "
      f"{dayConversions.get(day, '--Invalid day--')}, "
      f"{yearConversions.get(year, '--Invalid year--')}")
