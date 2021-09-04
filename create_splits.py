import argparse
import glob
import os
import random

import numpy as np

from utils import get_module_logger


def split(data_dir):
    """
    Create three splits from the processed records. The files should be moved to new folders in the 
    same directory. This folder should be named train, val and test.

    args:
        - data_dir [str]: data directory, /mnt/data
    """
    
    print(data_dir)
    files = os.listdir(data_dir)
    files = [f for f in files if f.endswith(".tfrecord")]

    if len(files) < 1:
        return

    np.random.shuffle(files)
    # print(files)

    train_split = 0.7
    val_split = 0.1
    test_split = 0.2

    val_num_files = int(np.round(val_split * len(files)))
    test_num_files = int(np.round(test_split * len(files)))

    train_num_files = len(files) - val_num_files - test_num_files

    train_files = files[:train_num_files]
    val_files = files[train_num_files:train_num_files + val_num_files]
    test_files = files[train_num_files + val_num_files:]

    print(len(files))
    print(val_num_files, test_num_files, train_num_files)
    print(len(val_files), len(test_files), len(train_files))

    os.makedirs(os.path.join(data_dir, "train"), exist_ok=True)
    os.makedirs(os.path.join(data_dir, "val"), exist_ok=True)
    os.makedirs(os.path.join(data_dir, "test"), exist_ok=True)

    for file in train_files:
        os.rename(os.path.join(data_dir, file), os.path.join(data_dir, "train", file))
    for file in val_files:
        os.rename(os.path.join(data_dir, file), os.path.join(data_dir, "val", file))
    for file in test_files:
        os.rename(os.path.join(data_dir, file), os.path.join(data_dir, "test", file))


if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--data_dir', default="../data/waymo_processed",
                        help='data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.data_dir)