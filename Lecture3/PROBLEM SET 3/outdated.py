# PROBLEM

# In the United States, dates are typically formatted in 
# month-day-year order (MM/DD/YYYY), otherwise known as 
# middle-endian order, which is arguably bad design. Dates in 
# that format can’t be easily sorted because the date’s year 
# comes last instead of first. Try sorting, for instance, 
# 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program 
# (e.g., a spreadsheet). Dates in that format are also ambiguous. 
# Harvard was founded on September 8, 1636, but 9/8/1636 could 
# also be interpreted as August 9, 1636!

# Fortunately, computers tend to use ISO 8601, an international 
# standard that prescribes that dates should be formatted in 
# year-month-day (YYYY-MM-DD) order, no matter the country, 
# formatting years with four digits, months with two digits, and 
# days with two digits, “padding” each with leading zeroes as 
# needed.

# In a file called outdated.py, implement a program that prompts 
# the user for a date, anno Domini, in month-day-year order, 
# formatted like 9/8/1636 or September 8, 1636, wherein the 
# month in the latter might be any of the values in the list 
# below:

def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    month_to_num = {month.upper(): i + 1 for i, month in enumerate(months)}

    while True:
        date_input = input("Date: ").strip()

        month, day, year = None, None, None

        try:
            if '/' in date_input:
                parts = date_input.split('/')
                if len(parts) == 3:
                    month = int(parts[0])
                    day = int(parts[1])
                    year = int(parts[2])
            elif ',' in date_input:
                parts = date_input.split()
                if len(parts) == 3 and parts[1].endswith(','):
                    month_name_raw = parts[0]
                    day_str_raw = parts[1]
                    year_str_raw = parts[2]

                    month_name_upper = month_name_raw.upper()

                    if month_name_upper in month_to_num:
                        month = month_to_num[month_name_upper]
                        day = int(day_str_raw.replace(',', ''))
                        year = int(year_str_raw)
            else:
                continue

            if month is None or day is None or year is None:
                continue

            if not (1 <= month <= 12 and 1 <= day <= 31 and year >= 0):
                continue

            print(f"{year:04d}-{month:02d}-{day:02d}")
            break

        except (ValueError, IndexError):
            continue

if __name__ == "__main__":
    main()