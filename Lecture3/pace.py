def main():
    pace = get_pace(miles = 25.2, minutes = 180)
    print(f"You need to run each mile in {round(pace, 2)} minutes.")

def get_pace(miles, minutes):
    return miles/minutes

main()