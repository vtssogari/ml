import cv2
from pathlib import Path
import json
import math
import sys
import os
import tensorflow as tf
from object_detection.utils import dataset_util


LABEL_DICT =  {
    "heading" : 1,
    "paragraph" : 2
}

def createTFRecord(label, file_path, filename):
    img = cv2.imread(file_path)
    height, width, channel = img.shape
    filename = filename.encode()
    with tf.gfile.GFile(file_path, 'rb') as fid:
        encoded_image = fid.read()
    image_format = 'png'.encode() 

    # whole pic is training object
    xmins = [0]
    ymins = [0]
    xmaxs = [1]
    ymaxs = [1]

    classes_text = [label.encode()]
    classes = [int(LABEL_DICT[label])]

    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': dataset_util.int64_feature(height),
        'image/width': dataset_util.int64_feature(width),
        'image/filename': dataset_util.bytes_feature(filename),
        'image/source_id': dataset_util.bytes_feature(filename),
        'image/encoded': dataset_util.bytes_feature(encoded_image),
        'image/format': dataset_util.bytes_feature(image_format),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
        'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
        'image/object/class/label': dataset_util.int64_list_feature(classes),
    }))
    return tf_example

# convert image to tfrecord
def createTFRecords(image_directory, label):
    pathlist = Path(image_directory).glob('**/*.png')
    for path in pathlist:
        path_in_str = str(path)
        filename = path.name
        tf_example = createTFRecord(label, path_in_str, filename)
        writer.write(tf_example.SerializeToString())
        print(filename)
    return

# Main -----------------------------------



writer = tf.python_io.TFRecordWriter("/home/kun/ml/models/research/training/word_train.record")
createTFRecords("/home/kun/Downloads/data/training/heading", "heading")
createTFRecords("/home/kun/Downloads/data/training/paragraph", "paragraph")
writer.close()

writer = tf.python_io.TFRecordWriter("/home/kun/ml/models/research/training/word_test.record")
createTFRecords("/home/kun/Downloads/data/test/heading", "heading")
createTFRecords("/home/kun/Downloads/data/test/paragraph", "paragraph")
writer.close()

# python createTFRecord.py paragraph  

