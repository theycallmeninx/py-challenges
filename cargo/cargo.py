#! python

CAPACITY = {
    "S": 50,
    "M": 100,
    "L": 200
}


def will_fit(holds, cargo):
    """ Determine if the cargo being loaded will fit with the ship's capacity.

    Args:
        holds (list):
        cargo (list):

    Returns:
        Boolean
    """
    cargo_slots = len(holds)
    final_cargo = [0] * cargo_slots
    for item in cargo:
        for index, slot in enumerate(final_cargo):
            if slot + item <= CAPACITY[holds[index]]:
                final_cargo[index] += item
                break
            if index+1 == cargo_slots:
                return False
    return True



