from PIL import Image
bg = Image.open("/home/pi/Desktop/pi_video_control_test/image.jpg")
fg = Image.open("/home/pi/Desktop/pi_video_control_test/fade.jpg")
# set alpha to .7
Image.blend(bg, fg, .7).save("out.png")