import board
import neopixel
import time

pixel_pin = board.D12
num_pixels = 12
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=1, auto_write=True, pixel_order=ORDER
)
pixels.fill((255,200,0))
pixels.show()
# pixels[0] = (0,0,0)
# pixels[1] = (0,0,0)
# pixels[2] = (0,0,0)
# pixels[3] = (0,0,0)
# count = 0
# while 1:
#     pixels[count] = (0,0,255)
#     pixels[count-2] = (0,0,0)
#     pixels[count-6] = (255,0,0)
#     pixels[count-8] = (0,0,0)
#     count = count + 1
#     if count > 11:
#         count = 0
#     time.sleep(.01)
sleepTime = 0.1
while 1:
    pixels[0] = (255,200,0)
    pixels[3] = (255,200,0)
    time.sleep(sleepTime)
    pixels[1] = (255,200,0)
    pixels[2] = (255,200,0)
    time.sleep(sleepTime)
    pixels[1] = (0,0,0)
    pixels[2] = (0,0,0)
    time.sleep(sleepTime)
    pixels[0] = (0,0,0)
    pixels[3] = (0,0,0)
    time.sleep(sleepTime)