"""Grade calculation."""


def calculate_grade(average, thresholds):
    """Return the grade for an average using thresholds sorted high -> low."""
    for t in thresholds:
        if average >= t["min"]:
            return t["grade"]
    return thresholds[-1]["grade"]
