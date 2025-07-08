def adjust_severity_for_patient(severity, age, weight, conditions):
    severity_map = {'low': 1, 'moderate': 2, 'high': 3}
    score = severity_map.get(severity, 1)

    if age < 12 or age > 65:
        score += 1
    if weight < 45 or weight > 100:
        score += 1
    for condition in conditions:
        if condition.strip() in ['diabetes', 'liver issues', 'kidney issues']:
            score += 1

    score = min(score, 3)
    reverse_map = {1: 'low', 2: 'moderate', 3: 'high'}
    return reverse_map[score]
