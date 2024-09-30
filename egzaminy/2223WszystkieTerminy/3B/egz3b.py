#Wojciech Michaluk
#...
#no niestety nie działa to O(nlogn)

from egz3btesty import runtests


def uncool(P):
    # Step 1: Sort the intervals by their start points
    intervals = sorted((start, end, idx) for idx, (start, end) in enumerate(P))

    # Step 2: Use a list to maintain active intervals
    active_intervals = []

    # Step 3: Sweep line algorithm to find the first pair of intervals that are not fine
    for start, end, idx in intervals:
        # Remove intervals from the active list that end before the current interval's start
        active_intervals = [(e, i) for e, i in active_intervals if e >= start]

        # Check current interval with all active intervals
        for e, i in active_intervals:
            # Check if intervals overlap and are not containing each other
            if not (P[i][0] <= start and end <= P[i][1]) and not (start <= P[i][0] and P[i][1] <= end):
                return (i, idx)

        # Insert the current interval into the active list, keeping it sorted by end points
        active_intervals.append((end, idx))
        active_intervals.sort()

runtests( uncool, all_tests = True)
