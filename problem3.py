from enum import Enum

# Enum Definition
class Week(Enum):
    Saturday = 1
    Sunday = 2
    Monday = 3
    Tuesday = 4
    Wednesday = 5
    Thursday = 6
    Friday = 7

# Using Enum
print(f"Week day: {Week.Monday}, Value: {Week.Monday.value}")
print(f"All days in week: {[Week for Week in Week]}")