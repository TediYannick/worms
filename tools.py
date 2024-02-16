import math

def angle(player_x, player_y, mouse_x, mouse_y):
    dx = mouse_x - player_x
    dy = mouse_y - player_y
    angle_rad = math.atan2(-dy, dx) 
    angle_deg = math.degrees(angle_rad)
    return angle_deg
