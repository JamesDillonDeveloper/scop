from picamera2 import Picamera2

camera = Picamera2(1)
camera.start()

camera.capture_file('hello.jpg')

camera.stop()
