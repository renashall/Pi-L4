from imutils.video import VideoStream
import imutils, time, cv2

from aicode101.aicode101_img_utils import get_img_model, read_json
from utils.mobilenet_tflite_utils import MobilenetFeatures
from utils.img_classify_utils import ImgKNN

path = 'aicode101/model/dataset.json'
dataset = read_json(path)
classifier = ImgKNN(dataset)

mobilenet_model_path = 'utils/imagenet_mobilenet_v2_050_224_feature_vector_1.tflite'
mobnet = MobilenetFeatures(model_path=mobilenet_model_path)

# initialize the video stream and allow the camera sensor to
# warmup
vs = VideoStream(usePiCamera=1).start()
time.sleep(2.0)

def loop():
    pass

if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        vs.stop() # release the video stream pointer
