def calculate_fine(data):
    fines = {
        "helmet": 1000,
        "triple_riding": 1500,
        "drunk_driving": 5000
    }

    base_fine = fines.get(data.violation.lower(), 500)

    if data.repeat_offense:
        base_fine *= 2

    return {
        "violation": data.violation,
        "state": data.state,
        "fine": base_fine
    }