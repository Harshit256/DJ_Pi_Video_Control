from PIL import Image
from PIL import ImageEnhance

image = Image.open(r'/home/pi/Desktop/pi_video_control_test/Transition.jpg')
enhancer = ImageEnhance.Brightness(image)
brighter_image = enhancer.enhance(2)
darker_image = enhancer.enhance(0.5)