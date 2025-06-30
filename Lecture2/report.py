"""def main():
    spacecraft = {"name": "Voyage 1", "distance": "163"}
    print(create_report(spacecraft))

def create_report(spacecraft):
     return f"""
#    ========= REPORT =========

#    Name : {spacecraft.get("name", "unknown")}
#    Distance : {spacecraft["distance"]} AU
     
#    ==========================
#    """

# Another way to access key in dictionary

#  Distance : {spacecraft.get("distance", "unknown")}
#  spacecraft["distance"] = 0.01

def main():
    spacecraft = {"name": "James Webb Space Telescope"}

    # Another way to add key to the dictionary if
    # we want add multiple keys.

    spacecraft.update({"distance": 0.01, "orbit": "Sun"})
    print(create_report(spacecraft))

    def create_report(spacecraft):
        return f"""
        ========= REPORT =========

        Name: {spacecraft.get("name", "unknown")}
        Distance: {spacecraft.get("distance", "unknown")}
        Orbit: {spacecraft.get("orbit", "unknown")}

        ==========================
        """
    
main() 