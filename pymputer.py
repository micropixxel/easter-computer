import math

def checkEasterDate(year):
    a = year % 19
    b = math.floor(year/100)
    c = year % 100
    d = math.floor(b/4)
    e = b % 4
    f = math.floor((b+8)/25)
    g = math.floor((b-f+1)/3)
    h = (19*a + b - d - g + 15) % 30
    i = math.floor(c/4)
    k = c % 4
    l = (32+2*e+2*i-h-k) % 7
    m = math.floor((a+11*h+22*l) / 451)
    n = math.floor((h+l-7*m+114) / 31)
    p = (h+l-7*m+114) % 31
    #print("Langfredag er %d.%d.%d" % (p-1, n, year))
    return [n, p]
    #return p-1

def findNextJason(jasonYear):
    y = 0
    for x in range(20):
        if y == 7:
            break
        if y > 7:
            y -= 7
        jasonYear += 1
        y += 1
        #print("y: %d, year: %d" % (y, jasonYear))
        if jasonYear % 4 == 0:
            y += 1
            #print("4 evoked")
        if jasonYear % 100 == 0:
            y -= 1
            #print("100 evoked")
        if jasonYear % 400 == 0:
            y += 1
            #print("400 evoked")
    return jasonYear

def findNextLongJason(jasonYear):
    x = 0
    while x < 1:
        jasonYear = findNextJason(jasonYear)
        #longFriday = checkEasterDate(jasonYear)
        longFriday = checkEasterDate(jasonYear)[1]-1
        #print("%d" % jasonYear)
        if longFriday == 13:
            x += 1
            print("Det er langfredag 13. april %d." % jasonYear)

def findPrevJason(jasonYear):
    y = 0
    for x in range(20):
        if y == 7:
            break
        if y > 7:
            y -= 7
        y += 1
        #print("y: %d, year: %d" % (y, year))
        if jasonYear % 4 == 0:
            y += 1
            #print("4 evoked")
        if jasonYear % 100 == 0:
            y -= 1
            #print("100 evoked")
        if jasonYear % 400 == 0:
            y += 1
            #print("400 evoked")
        jasonYear -= 1
    return jasonYear

def findFirstJason(jasonYear):
    year = jasonYear
    while year > 0:
        jasonYear = year
        year = findPrevJason(year)
    return jasonYear

def findAllJasons():
    year = findFirstJason(2001)
    jasonYears = []
    while year < 5000:
        year = findNextJason(year)
        #longFriday = checkEasterDate(year)
        longFriday = checkEasterDate(year)[1]-1
        if longFriday == 13:
            jasonYears.append(year)
    print("Length: %d" % len(jasonYears))
    for x in jasonYears:
        print("Det er langfredag 13. april %d" % x)

def getMonth(monthInt):
    monthStr = ""
    if monthInt == 3:
        monthStr = "March"
    elif monthInt == 4:
        monthStr = "April"
    else:
        monthStr = "ERROR"
    return monthStr

#findAllJasons()
print("Easter day in year 0 was on Saturday %s %d." % (getMonth(checkEasterDate(0)[0]), checkEasterDate(0)[1]))
#year = 2001
#findNextLongJason(year)
#longFriday = checkEasterDate(year)
#print("Fredag 13. april er i år %d" % year)
#year = findNextJason(year)
#print("Neste fredag 13. april er i år %d" % year)
#year = findNextJason(year)
#print("Og så i år %d og %d" % (year, findNextJason(year)))
#year = 2096
#print("Next Friday 13th: %d" % findNextJason(year))
#year = 2018
#print("Fredag 13. april er i år %d" % year)
#year = findPrevJason(year)
#print("Forrige fredag 13. april er i år %d" % year)
#year = findPrevJason(year)
#print("Og så i år %d og %d" % (year, findPrevJason(year)))
#print("First year with Friday 13th in April is %d" % findFirstJason(year))
