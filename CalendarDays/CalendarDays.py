# You are working with your team on a project for M number of days. For this example, let’s say M=7.
# Each person works a certain number of days, as illustrated X’s in the “calendar” below:
#                1   2   3   4   5   6   7  ... M
#
# Victor             x   x
#
# Clara          x        x   x   x
#
# Ali                                    x

# We want to calculate the number of calendars for a particular project schedule.
# Calendar days are equal to the number of days where at least one person worked.
# For this example -
# •
# at least one person was working from days 1-5 (+5)
# •
# no one was working on day 6 (+0)
# •
# Ali the manager swooped in on day 7 (+1)
# The number of calendar days is equal to 5 + 0 + 1.
# Programmatically, we can represent the calendar as a list of intervals.
# An interval has a start and end, and represents a range of contiguous days where one person worked.
# In this example, intervals would equal [Interval(2,3), Interval(1,1), Interval(3,5),
# Interval(7,7)].
# Note that the interval range is inclusive.
# Write a function get_cal_days(intervals)that takes in a list of intervals, and returns the number of
# calendar days as an int.


def get_cal_days(intervals):
    cal = {}
    for i in intervals:
        for x in range(i[0], i[1] + 1):
            cal[x] = 1
    return len(cal.keys())


a = get_cal_days([[2, 3], [1, 1], [3, 5], [7, 7]])
print(a)