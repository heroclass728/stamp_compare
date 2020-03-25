import numpy as np
import cv2

from skimage.metrics import structural_similarity as ssim


def compare_two_images(frame1_path, frame2_path):

    # compute the mean squared error and structural similarity
    # index for the images
    frame1 = cv2.imread(frame1_path)
    frame2 = cv2.imread(frame2_path)
    # origin_frame_hist = cv2.equalizeHist(origin_frame)
    frame1 = cv2.resize(frame1, (frame2.shape[1], frame2.shape[0]))
    m = mse(frame1, frame2)
    s = ssim(frame1, frame2, multichannel=True)

    return m, s


def mse(image_a, image_b):

    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((image_a.astype("float") - image_b.astype("float")) ** 2)
    err /= float(image_a.shape[0] * image_a.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are

    return err


if __name__ == '__main__':

    compare_two_images(frame1_path="", frame2_path="")
