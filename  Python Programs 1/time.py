SECONDS = 1
MINUTES = 60 * SECONDS
HOURS = 60 * MINUTES

# All these results are in seconds

time_left_house = 6 * HOURS + 52 * MINUTES

miles_run_easy_pace = 2 * (8 * MINUTES + 15 * SECONDS)

miles_run_fast_pace = 3 * (7 * MINUTES + 12 * SECONDS)

total_time_run = miles_run_easy_pace + miles_run_fast_pace + time_left_house

# So we now have a big number of seconds to split into hours/minutes/seconds

hours = total_time_run // HOURS

# the left over part is minutes and seconds (still in seconds)

part_hour = total_time_run % HOURS
minutes = part_hour // MINUTES
seconds = part_hour % MINUTES

print "Total time run: {}, Hours: {}, Minutes: {}, Seconds: {}".format(
    total_time_run, hours, minutes, seconds)
