from src.feature_calculation.image_feature import ImageFeature
from scipy.spatial import distance


image_feature_detector = ImageFeature()


def calculate_distance_between_features(frame1_path, frame2_path):

    frame1 = image_feature_detector.get_feature_from_image(img_path=frame1_path)
    frame2 = image_feature_detector.get_feature_from_image(img_path=frame2_path)

    eu_dist = distance.euclidean(frame2, frame1)

    return eu_dist


if __name__ == '__main__':

    dist = calculate_distance_between_features(frame1_path="/media/mensa/Data/Task/ImageComparison/data/1003.jpg",
                                               frame2_path="/media/mensa/Data/Task/ImageComparison/data/4.jpg")
    print(dist)
