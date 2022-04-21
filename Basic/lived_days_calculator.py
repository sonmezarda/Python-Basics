currentDay = int(input("Enter the current day: "))
currentMonth = int(input("Enter the current month: "))
currentYear = int(input("Enter the current year: ")) 

birthDay = int(input("Enter the day for your date of birth: "))
birthMonth = int(input("Enter the month for your date of birth: "))
birthYear = int(input("Enter the year for your date of birth: ")) 

passedDays = 0
leftDays = 0
birthPassedDays = 0
countable = 0

leapMonths=   [31,29,31,30,31,30,31,31,30,31,30,31]
regularMonths=[31,28,31,30,31,30,31,31,30,31,30,31]

if (12>currentMonth>0 and  12>birthMonth>0) and (currentYear > 0 and birthYear >0) and (31>currentDay>0 and 31>birthDay>0):
    isLeapCurrent = (currentYear % 4 == 0 and (currentYear % 100 != 0 or currentYear % 400 == 0))
    isLeapBirth = (birthYear % 4 == 0 and (birthYear % 100 != 0 or birthYear % 400 == 0))

    if not isLeapCurrent and not isLeapBirth:
        if currentDay <= regularMonths[currentMonth-1] and birthDay <= regularMonths[birthMonth-1]:
            countable = 1
        else:
            countable = 0
    elif isLeapCurrent and not isLeapBirth:
        if currentDay <= leapMonths[currentMonth-1] and birthDay <= regularMonths[birthMonth-1]:
            countable = 1
        else:
            countable = 0
    elif isLeapCurrent and isLeapBirth:
        if currentDay <= leapMonths[currentMonth-1] and birthDay <= leapMonths[birthMonth-1]:
            countable = 1
        else:
            countable = 0
    else:
        if currentDay <= regularMonths[currentMonth-1] and birthDay <= leapMonths[birthMonth-1]:
            countable = 1
        else:
            countable = 0
        
if countable == 1:
    for i in range(birthYear+1,currentYear):
        isLeap = (i % 4 == 0 and (i % 100 != 0 or i % 400 == 0))
        if isLeap:
            passedDays += 366
        else:
            passedDays += 365

    if isLeapCurrent:
        for i in range(1,currentMonth):
            passedDays += leapMonths[i-1]
        passedDays += currentDay
    else:
        for i in range(1,currentMonth):
            passedDays += regularMonths[i-1]
        passedDays += currentDay

    if isLeapBirth:
        for i in range(1,birthMonth):
            birthPassedDays += leapMonths[i-1]
        birthPassedDays += birthDay
        leftDays = 366-birthPassedDays
    else:
        for i in range(1,birthMonth):
            birthPassedDays += regularMonths[i-1]
        birthPassedDays += birthDay
        leftDays = 365 - birthPassedDays

    if currentYear != birthYear:
        passedDays += leftDays
    else:
        passedDays = passedDays - birthPassedDays

    if passedDays <0 or currentYear<birthYear:
        print("You can not born in the future")
    else:
        print("You have lived",passedDays,"days")
else:
    print("You entered invalid date!")
