# Handling the exceptions

distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU", # float() cannot convert "AU" into float value 
    "New Horizons": "58",
    "Pioneer 11": "44 AU"
}

def main():
    spacecraft = input("Enter a spacecraft: ")

    # In case where float value cannot convert the string.

    try: 
        au = float(distances[spacecraft])
    except KeyError: # If user input a key that's not available in dictionary. 
        print(f"'{spacecraft}' is not in dictionary")
    except ValueError:
        print(f"can't convert {distances[spacecraft]} to a float")
        return
    
    m = convert(au)
    print(f"{m} m away")

def convert(au):
    return au * 149597870700

main()