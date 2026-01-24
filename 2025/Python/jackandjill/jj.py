HILL_F, LOG_ROLL_F, FRONT_ROLL_F = [float(x) for x in input().split()]

# Convert to integers (decimeters) to avoid all floating point errors.
HILL = round(HILL_F * 10)
LOG_ROLL = round(LOG_ROLL_F * 10)
FRONT_ROLL = round(FRONT_ROLL_F * 10)

best_log: int = 0
best_front: int = 0

min_distance_away: int = HILL + 1

for i in range(HILL // LOG_ROLL, -1, -1):
    log_distance = i * LOG_ROLL
    
    remaining_distance = HILL - log_distance
    
    curr_front = remaining_distance // FRONT_ROLL
    
    total_distance = log_distance + (curr_front * FRONT_ROLL)
    
    distance_away = HILL - total_distance
    
    if distance_away < min_distance_away:
        min_distance_away = distance_away
        best_log = i
        best_front = curr_front

print(f"{best_log} {best_front}")