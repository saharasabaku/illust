from PIL import Image
import glob,os

from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent
rawdata_dir = os.path.join(BASE_DIR,'img/rawdata')
makedata_dir = os.path.join(BASE_DIR,'img/makedata')