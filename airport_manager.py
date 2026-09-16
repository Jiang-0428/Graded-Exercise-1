######################## IMPORTANT ########################
""" Do not rename the variables or functions.
Do not change the function parameters.
Do not add input() calls inside airport_manager.py.
The file must be importable by the tests. """
###########################################################

airport_info = ("OUL", "1", "14-09-2026")
allowed_gates = {"A1", "A2", "A3", "A4", "B1", "B2"}
restricted_destinations = {"Moscow", "Pyongyang"}
flights = {
    "AY450": {
        "destination": "Helsinki",
        "departure": "08:30",
        "gate": "A2",
        "capacity": 5,
        "passengers": ["Alice Wong", "David Kim", "Fatima Ali"]
    },
    "SK271": {
        "destination": "Stockholm",
        "departure": "10:15",
        "gate": "B1",
        "capacity": 4,
        "passengers": ["Chen Wei", "George Smith"]
    },
    "LH2491": {
        "destination": "Munich",
        "departure": "12:40",
        "gate": "A4",
        "capacity": 5,
        "passengers": ["Hana Lee", "Maria Garcia", "Noah Wilson"]
    }
}

## Logic to find if a flight exists
def find_flight(flights, flight_number):
    search_key = flight_number.strip().upper()
    for key in flights:
        if key.upper() == search_key:
            return key
    return None

## Logic to find if a passenger exists
def passenger_exists(passengers, passenger_name):
    target = passenger_name.strip().casefold()
    for name in passengers:
        if name.strip().casefold() == target:
            return True
    return False

## Logic to check in a passenger
def check_in_passenger(
    flights,
    flight_number,
    passenger_name,
    restricted_destinations
):
    norm_flight_key = find_flight(flights, flight_number)
    if norm_flight_key is None:
        return "FLIGHT_NOT_FOUND"

    flight = flights[norm_flight_key]
    if flight["destination"] in restricted_destinations:
        return "RESTRICTED"

    stored_name = passenger_name.strip()
    if not stored_name:
        return "EMPTY_NAME"

    if passenger_exists(flight["passengers"], passenger_name):
        return "DUPLICATE"

    if len(flight["passengers"]) >= flight["capacity"]:
        return "FULL"

    flight["passengers"].append(stored_name.title())
    return "OK"

## Logic to remove a passenger from a flight
def remove_passenger(
    flights,
    flight_number,
    passenger_name
):
    norm_flight_key = find_flight(flights, flight_number)
    if norm_flight_key is None:
        return "FLIGHT_NOT_FOUND"
    flight = flights[norm_flight_key]

    if not passenger_exists(flight["passengers"], passenger_name):
        return "PASSENGER_NOT_FOUND"

    target_low = passenger_name.strip().casefold()
    for idx, stored_name in enumerate(flight["passengers"]):
        if stored_name.strip().casefold() == target_low:
            del flight["passengers"][idx]
            break
    return "OK"

# Logic to change the gate of a flight
def change_gate(
    flights,
    flight_number,
    new_gate,
    allowed_gates
):
    norm_flight_key = find_flight(flights, flight_number)
    if norm_flight_key is None:
        return "FLIGHT_NOT_FOUND"

    input_gate = new_gate.strip().upper()
    if input_gate in allowed_gates:
        flights[norm_flight_key]["gate"] = input_gate
        return "OK"
    return "INVALID_GATE"

# Logic to get the status of a flight
def flight_status(flight):
    cap = flight["capacity"]
    count = len(flight["passengers"])
    pct = (count / cap) * 100
    if pct >= 100:
        return "FULL"
    elif pct >= 75:
        return "ALMOST FULL"
    else:
        return "AVAILABLE"

# Logic to get the sorted manifest of a flight
def sorted_manifest(
    flights,
    flight_number
):
    norm_key = find_flight(flights, flight_number)
    if norm_key is None:
        return None
    return sorted(flights[norm_key]["passengers"])

# Logic to get the total number of passengers across all flights
def total_passengers(flights):
    total = 0
    for flight_data in flights.values():
        total += len(flight_data["passengers"])
    return total

# Logic to check if any flight is full
def any_full_flight(flights):
    for fd in flights.values():
        if len(fd["passengers"]) >= fd["capacity"]:
            return True
    return False

# Logic to check if all flights have at least one passenger
def all_flights_have_passengers(flights):
    for fd in flights.values():
        if len(fd["passengers"]) == 0:
            return False
    return True
