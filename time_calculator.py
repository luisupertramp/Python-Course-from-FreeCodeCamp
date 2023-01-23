def add_time(start, duration, day=''):

    # *** SPLIT PARAMETERS ***
    hours  = int(start.split()[0].split(':')[0])
    minutes  = int(start.split()[0].split(':')[1])
    noon = start.split()[1]

    addHours = int(duration.split(':')[0])
    addMinutes = int(duration.split(':')[1])
    addDays = 0

    # *** ADDING MINUTES ***
    if minutes + addMinutes >= 60 :     # if the total of minutes is more than 60 ...
        addHours += 1                   # an extra hour is added to the variable 'addHours'
        minutes += (addMinutes - 60)    # and the remaining minutes are assigned to the variable 'minutes'
    else : 
        minutes += addMinutes           # otherwise, it's just a simple addition

    # *** ADDING HOURS AND DAYS (IF APPLICABLE) ***

    if hours + addHours < 12 :         # if the total hours is not greater than 12, simple addition
        hours += addHours

    elif hours + addHours >= 12 and hours + addHours < 24 :   #if hours is not greater than 24 hours but greater or equal than 12
        hours += addHours-12 if hours + addHours > 12 else addHours      # substract 12 hours only if the total hours is greater than 12 (to avoid outputs like 0:00)
        if noon == "PM" :               # if noon EQ PM it means that 1 days has passed
            addDays += 1
            noon = "AM" 
        else :                          # otherwise, just change the 'noon' variable
            noon = "PM"

    elif hours + addHours >= 24 :       # if the total of hours is more than 24 ...
        hours += 12 if noon == "PM" else 0  # easier to handle in 24 hours format and re-format at the end
        addDays, modHours = divmod((addHours + hours) / 24 , 1) # Calculate days based on hours and store it in 'addDays'
        hours = round(modHours*24)      # the remaining hours are stored in 'modHours' and added to 'hours' variable

        if hours > 12 :                 # format the remaining hours for AM or PM
            hours -= 12
            noon = "PM"
        else : 
            noon = "AM"
            hours = 12 if hours == 0 else hours     #display 12 instead of 0 when the addDays result is exact
                
    
    # *** CONCATENATE RESULTS ***
    outputHour = str(hours) + ":" + (("0" + str(minutes)) if int(minutes) < 10 else str(minutes)) + " " + noon
    
    # If the day of the week was sent
    dayPosition = 0

    if not day == '' :
        daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        day = day.capitalize()                  # format day to match the array above
        dayPosition = daysOfWeek.index(day)     # get position of given day

        if addDays :                            # if more than a day passed..
            # Calculate the position of the new day based on the addition of current day position + the days elapsed
            newDayOfWeek = int((addDays+dayPosition)%7 if addDays+dayPosition>=7 else addDays+dayPosition)
            outputHour += ', ' + daysOfWeek[newDayOfWeek]
        else :                                  # otherwise, print the day sent
            outputHour += ', ' + day

    # If more than a day has passed
    if addDays == 1 :
        outputHour += ' (next day)'
    elif addDays >= 2 : 
        outputHour += ' (' + str(int(addDays)) + ' days later)'

    return outputHour

# print(add_time("3:00 PM", "3:10"))
# print(add_time("11:30 AM", "2:32", "Monday"))
# print(add_time("11:43 AM", "00:20"))
# print(add_time("10:10 PM", "3:30"))
# print(add_time("11:43 PM", "24:20", "friDay"))
# print(add_time("6:30 PM", "205:12"))