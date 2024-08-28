def new_id(name, number):
    return f"{name}{number+1}"


assert new_id("Ellie", 22) == "Ellie23", "ERROR!"

print()