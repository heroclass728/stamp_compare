import os
import glob
import math
import json

from flask import Flask, request
from src.ssim.image_similarity import compare_two_images
from src.image_url.image_from_url import get_image_from_url
from utils.image_processing import preprocess_image
from settings import EXP_CONST, SERVER_HOST, SERVER_PORT, CUR_DIR, LOCAL

app = Flask(__name__)


@app.route('/compare', methods=['GET'])
def run():

    frame1_url = request.args.get('img1')
    frame2_url = request.args.get('img2')

    frame1_path = get_image_from_url(https_url=frame1_url, file_id="1")
    frame2_path = get_image_from_url(https_url=frame2_url, file_id="2")
    processed_frame1_path = preprocess_image(frame_path=frame1_path, file_id="1")
    processed_frame2_path = preprocess_image(frame_path=frame2_path, file_id="2")
    _, similarity = compare_two_images(frame1_path=processed_frame1_path, frame2_path=processed_frame2_path)
    ss = 1 - math.exp(EXP_CONST * similarity)
    print(similarity)
    print(ss)
    data = {'similarity score': ss}
    response = json.dumps(data)
    for path in glob.glob(os.path.join(CUR_DIR, 'utils', '*.jpg')):
        os.remove(path)

    return response


if __name__ == '__main__':

    if LOCAL:
        app.run(debug=True, host=SERVER_HOST, port=SERVER_PORT)
        app.run(debug=True)
    else:
        app.run()
