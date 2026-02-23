
import math

def get_new_angle(angle, v1, v2):
    """Snells law"""
    return math.asin(math.sin(angle)*v2/v1)

if __name__ == "__main__":
    # Distance from A (or B) perpendicular to the marsh bank
    D_TO_MARSH = (100/(2**0.5) - 50) / 2

    # Distance from A to B parallel to marsh bank
    # Marsh is at 45 deg so distance parallel is same as perpendicular
    D_NEEDED = D_TO_MARSH + 50 + D_TO_MARSH

    # Calculate optimal angle
    lower = 0
    upper = math.pi / 2
    for _ in range(100):
        # Snell angle (measured relative to perpendicular to mark bank)
        initial_angle = (lower+upper)/2
        angle = initial_angle

        # Distance measured parallel to the marsh bank
        initial_d = D_TO_MARSH*math.tan(initial_angle)  # Dist from A to marsh
        d = initial_d

        initial_speed = 10
        speed = initial_speed

        time_taken = (D_TO_MARSH/math.cos(angle)) / speed  # Time from A to entering marsh
        for new_speed in [9, 8, 7, 6, 5]:
            angle = get_new_angle(angle, speed, new_speed)
            speed = new_speed
            d += 10*math.tan(angle)
            time_taken += (10/math.cos(angle)) / speed
        time_taken += (D_TO_MARSH/math.cos(initial_angle)) / initial_speed  # Time from exiting marsh to B

        # By symmetry (the angles before entering and after exiting the marsh are the same),
        # the remaining distance after exiting the marsh
        # is the same as the initial distance before entering the marsh
        if (D_NEEDED - d) < initial_d:  # Gone too far in marsh, reduce angle
            upper = initial_angle
        else:
            lower = initial_angle
    print(f"{time_taken:.10f}")  # 13.1265108586
