import os
import numpy as np
import cv2

from settings import CUR_DIR


def preprocess_image(frame_path, file_id):

    file_path = os.path.join(CUR_DIR, 'utils', "temp_{}.jpg".format(file_id))
    frame = cv2.imread(frame_path)

    bg_color = np.zeros((1, 3))
    for i in range(10):
        bg_color += frame[1][i]
    bg_color /= 10
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if bg_color[0][0] >= 127 and bg_color[0][1] >= 127 and bg_color[0][2] >= 127:
        thresh_frame = cv2.threshold(frame_gray, 230, 255, cv2.THRESH_BINARY_INV)[1]
    else:
        thresh_frame = cv2.threshold(frame_gray, 100, 255, cv2.THRESH_BINARY)[1]

    contours, _ = cv2.findContours(thresh_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    sorted_contour = sorted(contours, key=cv2.contourArea, reverse=True)
    object_contour = sorted_contour[0]

    x, y, w, h = cv2.boundingRect(object_contour)
    obj_frame = frame_gray[y:y+h, x:x+w]

    cv2.imwrite(file_path, obj_frame)

    return file_path


def get_closest_point_from_corner(points, corner):

    points_dists = []
    for pt in points:
        dist = (pt[0][0] - corner[0]) ** 2 + (pt[0][1] - corner[1]) ** 2
        points_dists.append(dist)

    min_idx = points_dists.index(min(points_dists))

    return points[min_idx][0]


if __name__ == '__main__':

    preprocess_image(frame_path="", file_id=0)
