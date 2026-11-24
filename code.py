from sense_hat import SenseHat
import time

# γύρνα την οθόνη σε συγκεκριμένη πλευρά
sense = SenseHat()
sense.set_rotation(270)

# Set up the colour sensor
sense.color.gain = 60  
sense.color.integration_cycles = 128

# χρώματα
Y = (255, 255, 0)   # Yellow / Κίτρινο
W = (255, 255, 255) # White / Άσπρο

# άρχησε να μετράς χρόνο
start_time = time.time()

# Animation 
while time.time() - start_time < 28:
    #  βρες το χρώμα από τον σένσορα
    rgb = sense.color
    B = (rgb.red, rgb.green, rgb.blue)

    image = [
        B, B, B, B, B, B, B, B,
        B, B, Y, Y, Y, B, B, B,
        B, Y, Y, Y, Y, Y, B, B,
        B, Y, Y, Y, Y, Y, B, W,
        B, Y, Y, Y, Y, Y, B, W,
        B, Y, Y, Y, Y, Y, B, B,
        B, B, Y, Y, Y, B, B, B,
        B, B, B, B, B, B, B, B
    ]

    pacman_g = [
        B, B, B, B, B, B, B, B,
        B, B, Y, Y, Y, B, B, B,
        B, Y, Y, Y, Y, B, B, B,
        B, Y, Y, Y, B, B, W, W,
        B, Y, Y, Y, B, B, W, W,
        B, Y, Y, Y, Y, B, B, B,
        B, B, Y, Y, Y, B, B, B,
        B, B, B, B, B, B, B, B,
    ]

    pacman_2 = [
        B, B, B, B, B, B, B, B,
        B, B, Y, Y, Y, B, B, B,
        B, Y, Y, Y, B, B, B, B,
        B, Y, Y, B, W, W, B, B,
        B, Y, Y, B, W, W, B, B,
        B, Y, Y, Y, B, B, B, B,
        B, B, Y, Y, Y, B, B, B,
        B, B, B, B, B, B, B, B
    ]

    frames = [image, pacman_g, pacman_2]

    for frame in frames:
        sense.set_pixels(frame)
        time.sleep(0.16)  # Short delay between frames

# Clear the screen after 28 seconds
x = (178, 34, 34)  
sense.clear(B)
