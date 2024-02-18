import math


def angle(player_x, player_y, mouse_x, mouse_y):
    dx = mouse_x - player_x
    dy = mouse_y - player_y
    angle_rad = math.atan2(-dy, dx) 
    angle_deg = math.degrees(angle_rad)
    return angle_deg

def trajectoire(start_x, start_y, power, angle_deg, num_points):
    trajectory_points = []
    for i in range(num_points):
        time = i * 0.1
        x = start_x + power * math.cos(math.radians(angle_deg)) * time
        y = start_y - (power * math.sin(math.radians(angle_deg)) * time - 0.5 * 9.8 * time ** 2)
        trajectory_points.append((x, y))
    return trajectory_points

def switch_player(current_player, player1, player2):
    if current_player == player1:
        return player2
    else:
        return player1





