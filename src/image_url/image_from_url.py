import os
import cv2

from skimage import io
from settings import CUR_DIR


def get_image_from_url(https_url, file_id):

    file_path = os.path.join(CUR_DIR, 'utils', 'download_temp_{}.jpg'.format(file_id))

    http_frame = io.imread(https_url)
    image = cv2.cvtColor(http_frame, cv2.COLOR_BGR2RGB)
    # cv2.imshow("url image", image)
    # cv2.waitKey()
    cv2.imwrite(file_path, image)

    return file_path


if __name__ == '__main__':

    get_image_from_url(https_url="", file_id=0)
