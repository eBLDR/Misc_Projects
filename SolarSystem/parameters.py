# Parameters
W = 800  # screen size
H = 640

# The higher the FPS, the more accuracy the movement, and the more CPU required
FPS = 500

distance_factor = 3 * (10 ** 9)  # 1 pixel = ?x10^x meters
time_factor = 10 * (10 ** 6)  # 1 second real = ?x10^x second simulation
time_delta = int(round(time_factor / FPS))

G = 6.673 * (10 ** (-11))  # universal gravitational constant
