def add_time(start, duration, start_day_of_week=None):
  # convert start from 12hr to 24hr format
  new_time = ""
  new_time_ampm = "AM"
  days_later = 0
  additional_hours = 0
  days_of_the_week = {
      'monday': 1,
      'tuesday': 2,
      'wednesday': 3,
      'thursday': 4,
      'friday': 5,
      'saturday': 6,
      'sunday': 0
  }
  days_of_the_week_str = {
      1: 'Monday',
      2: 'Tuesday',
      3: 'Wednesday',
      4: 'Thursday',
      5: 'Friday',
      6: 'Saturday',
      0: 'Sunday'
  }

  am_pm = start.split(" ")[1]
  start_12hr = start.split(" ")[0]
  start_12hr_hr = int(start_12hr.split(":")[0])
  start_12hr_min = int(start_12hr.split(":")[1])
  start_24hr_hr = start_12hr_hr + 12 if am_pm == "PM" else start_12hr_hr
  start_24hr_min = start_12hr_min
  duration_hr = int(duration.split(":")[0])
  duration_min = int(duration.split(":")[1])

  # add the time together
  new_time_min = start_24hr_min + duration_min

  if new_time_min > 60:
    additional_hours = new_time_min // 60
    new_time_min %= 60

  new_time_hr = start_24hr_hr + duration_hr + additional_hours

  # format the new time for the hour place
  if new_time_hr > 24:
    days_later += new_time_hr // 24
    new_time_hr %= 24

  # convert from 24-hour format to 12-hour format
  if new_time_hr >= 12:
    new_time_ampm = "PM"

    if new_time_hr > 12:
      new_time_hr -= 12

  if new_time_hr == 0:
    new_time_hr = 12

  # format the new time for the minute place
  if new_time_min < 10:
    new_time_min = "0" + str(new_time_min)

  new_time = f'{new_time_hr}:{new_time_min} {new_time_ampm}'

  # account for day of week
  if start_day_of_week:
    start_day_of_week = start_day_of_week.lower()
    start_day_of_week_index = days_of_the_week[start_day_of_week]
    new_day_of_week_index = (start_day_of_week_index + days_later) % 7
    new_day_of_week = days_of_the_week_str[new_day_of_week_index]
    new_time += f', {new_day_of_week}'

  # account for additional days
  if days_later > 0:
    if days_later == 1:
      new_time += " (next day)"
    else:
      new_time += f" ({days_later} days later)"

  return new_time
