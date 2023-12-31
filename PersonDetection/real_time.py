

# Imports
import tensorflow as tf

# Object detection imports
from utils import backbone
from api import object_counting

#if tf.__version__ < '1.4.0':
#  raise ImportError('Please upgrade your tensorflow installation to v1.4.* or later!')

input_video = "sample1.avi"

# By default I use an "SSD with Mobilenet" model here. See the detection model zoo (https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md) for a list of other models that can be run out-of-the-box with varying speeds and accuracies.
detection_graph, category_index = backbone.set_model('ssd_mobilenet_v1_coco_2017_11_17')

#object_counting_api.object_counting(input_video, detection_graph, category_index, 0) # for counting all the objects, disabled color prediction

#object_counting_api.object_counting(input_video, detection_graph, category_index, 1) # for counting all the objects, enabled color prediction


targeted_objects = "person" # (for counting targeted objects) change it with your targeted objects
fps = 80 # change it with your input video fps
width = 400 # change it with your input video width
height = 200 # change it with your input vide height
is_color_recognition_enabled = 0

object_counting.targeted_object_counting(input_video, detection_graph, category_index, is_color_recognition_enabled, 'person', 50, width, height) # targeted objects counting

#object_counting_api.object_counting(input_video, detection_graph, category_index, is_color_recognition_enabled, fps, width, height) # counting all the objects

