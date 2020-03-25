import os

from utils.folder_file_manager import make_directory_if_not_exists


CUR_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = make_directory_if_not_exists(os.path.join(CUR_DIR, 'utils', 'model'))
INCEPTION_URL = 'http://download.tensorflow.org/models/image/imagenet/inception-2015-12-05.tgz'

EXP_CONST = -11.51248
LOCAL = False
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5000
