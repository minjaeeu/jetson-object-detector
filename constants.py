
model = "ssd-mobilenet-v2" # trained model to be used from jetson inference

model_threshold = 0.6 # inc = detect less objects || dec = detect more objects

cam_device = "/dev/video0" # v4l2 camera device id

cam_width = 1280 # video recording width

cam_height = 720 # video recording height
