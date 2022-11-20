import jetson_inference
import jetson_utils
from constants import cam_height, cam_width, cam_device, model, model_threshold

net = jetson_inference.detectNet(model, threshold=model_threshold)

camera = jetson_utils.gstCamera(cam_height, cam_width, cam_device)
display = jetson_utils.glDisplay()

while display.IsOpen():  # Main loop
    (
        img,
        width,
        height,
    ) = (
        camera.CaptureRGBA()
    )  # Returns image and dimensions from the cam_device. Blocks pipeline until receives a full frame
    detections = net.Detect(img, width, height)
    display.RenderOnce(
        img, width, height
    )  # Renders the image being capture to an OpenGL window
    display.SetTitle(
        "Object Detector | PDS | ECAT 2022 | MINJAE, KASSIANE, JULIANA & EDUARDO | {:.0f} FPS".format(net.GetNetworkFPS())
    )
