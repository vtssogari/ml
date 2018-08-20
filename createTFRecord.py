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
    height, width = img.shape
    filename = filename.encode()
    with tf.gfile.GFile(file_path, 'rb') as fid:
        encoded_image = fid.read()
    image_format = 'png'.encode() 

    # whole pic is training object
    xmins = [0]
    ymins = [0]
    xmaxs = [1]
    ymaxs = [1]

    classes_text = [label]
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
def createTFRecords(image_directory, label, output_path):
    pathlist = Path(image_directory).glob('**/*.png')
    writer = tf.python_io.TFRecordWriter(output_path)
    len_pathlist = len(pathlist)
    counter = 0
    for path in pathlist:
        path_in_str = str(path)
        filename = path.name
        tf_example = createTFRecord(label, path_in_str, filename)
        writer.write(tf_example.SerializeToString())

        if counter % 10 == 0:
            print("Percent done", (counter/len_pathlist)*100)
        counter += 1

    writer.close()
    return

# Main -----------------------------------
label = sys.argv[1]
image_directory = sys.argv[2] 
output_directory = sys.argv[3]


if not os.path.exists(output_directory):
    os.makedirs(output_directory)

print("image_directory : ", image_directory )
print("output_directory: ", output_directory)

createTFRecords(image_directory, label, output_directory)

print("Done. output folder : " + output_directory)
