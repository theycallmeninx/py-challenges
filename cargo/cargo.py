#! python
from typing import List


def will_fit(holds: List[str], cargo: List[int]) -> bool:
    """ Determine if the cargo being loaded will fit with the ship's capacity.

    Notes:
        the capacity variable here is a lookup table of the capacity to its storage value. Here, the values represent
        the total amount that the cargo hold can store.

    Args:
        holds: the ship slots and its capacity (S,M,L)
        cargo: the incoming cargo weight
    """
    capacity = {"S": 50, "M": 100, "L": 200}
    cargo_slots = len(holds)
    final_cargo = [0] * cargo_slots
    for item in cargo:
        for index, slot in enumerate(final_cargo):
            if slot + item <= capacity[holds[index]]:
                final_cargo[index] += item
                break
            if index+1 == cargo_slots:
                return False
    return True



