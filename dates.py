# get average of dates
# not currently in use but may be used later

def find_poll_cadence(dates):
    average_interval = []

    for d in range(len(dates)):
        if d == 0:
            last_date = dates[d]
        else:
            last_date = dates[d-1]

        current_date = dates[d]
        day_delta = (current_date - last_date).days * 24
        hour_delta = (current_date - last_date).seconds // 3600

        average_interval.append(day_delta + hour_delta)

    last_five_average = sum(average_interval[:5]) / len(average_interval[:5])

    update_cadence = "none"

    print(last_five_average)

    if last_five_average < 24:
        update_cadence = "hourly"
    else:
        update_cadence = "daily"

    print(update_cadence)