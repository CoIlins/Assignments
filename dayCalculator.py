#
# Zeller’s formula calculates the day of the week for any date in the Gregorian calendar.
#
# Let:
#
# - `q` = day of the month
# - `m` = month (3 = March, 4 = April, ..., 12 = December; January and February are counted as 13 and 14 of the previous year)
# - `Y` = year (adjusted if month is Jan or Feb)
# - `K` = year of the century (`year % 100`)
# - `J` = zero-based century (`year // 100`)
#
# Then the formula is:
#
# ## h = (q + ⌊13(m + 1) / 5⌋ + K + ⌊K / 4⌋ + ⌊J / 4⌋ + 5J) % 7
#
# ## Task: Solve This Using OOP
#
# - Define a class `DateCalculator`
# - Initialize with `year`, `month`, `day`
# - Adjust month/year for January and February
# - Calculate components: `K` and `J`
# - Use the formula to compute the weekday
# - Return or print the result
#
# ---

class DateCalculator:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.adjust_date()

    def adjust_date(self):

        if self.month == 1 or self.month == 2:
            self.month += 12
            self.year -= 1

    def calculate_day_of_week(self):
        q = self.day
        m = self.month
        Y = self.year
        K = Y % 100  # Year of the century
        J = Y // 100  # Zero-based century

        h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + (5 * J)) % 7

        # Mapping the result to the weekday name
        days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        return days[h]

    def print_day_of_week(self):
        day_name = self.calculate_day_of_week()
        print(f"The day of the week is: {day_name}")

if __name__ == "__main__":
    date = DateCalculator(2024, 4, 28)  # April 28, 2024
    date.print_day_of_week()
