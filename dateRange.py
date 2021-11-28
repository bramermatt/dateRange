# Date Range Program
# Determine difference between dates in total difference:
# The total difference is: ## month(s) ## day(s) #### year(s) 

# how to do the input method
# Month Day Year
# 12 5 1957

print('Welcome to the date conversion machine! \nThe goal is to determine the difference between two dates! \nThe first date starts right now!\n')

# Starting Date
startMonth = int(input('What is the number Month?(1-12) '))
# if statement for wrong numbers? - work in progress
startDay = int(input('What is the number Day?(1-31) '))
# if statement for wrong numbers? - work in progress
startYear = int(input('What is the number Year?(1-2021) '))
# if statement for wrong numbers? - work in progress

print('\nThe starting date is:', startMonth, startDay, startYear, "\n")


# Ending Date
endMonth = int(input('What is the ending Month?(1-12) '))
endDay = int(input('What is the ending Day?(1-31) '))
endYear = int(input('What is the ending Year?(1-2021) '))

print('\nThe ending date is:', endMonth, endDay, endYear, "\n")

if startMonth < endMonth:
    totalMonth = endMonth - startMonth
else:
    totalMonth = startMonth - endMonth

if startDay < endDay:
    totalDay = endDay - startDay 
else:
    totalDay = startDay - endDay

if startYear < endYear:
    totalYear = endYear - startYear 
else:
    totalYear = startYear - endYear

print('The total difference is:', totalYear,'year(s)', totalMonth,'month(s)', totalDay,'day(s).',"\n")

# the goal is to have ONLY days difference. 
# need to make Day as (31 days (some days 30 days)), Year as (365 days (some years 366 days)), and Month as (31 days (some months 30 days))

inDays = ((totalYear * 365) + (totalMonth * 31) + (totalDay * 31))
print('The total in days is', inDays,'day(s).',"\n")
