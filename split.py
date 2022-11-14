import shutil
import os
import numpy as np
import argparse

def get_files_from_folder(path, extension):

    # files = os.listdir(path)
    # return np.asarray(files)
    files = []
    for file in os.listdir(path):
        if file.endswith(extension):
            files.append(file)
        else:
          print(file)
    return np.asarray(files)

def main(path_to_data, path_to_test_data, train_ratio):
    # get dirs
    _, dirs, _ = next(os.walk(path_to_data))

    # calculates how many train data per class
    data_counter_per_class = np.zeros((len(dirs)))
    for i in range(len(dirs)):
        path = os.path.join(path_to_data, dirs[i])
        files = get_files_from_folder(path, extension=".jpg")
        data_counter_per_class[i] = len(files)
    test_counter = np.round(data_counter_per_class * (1 - train_ratio))

    # transfers files
    for i in range(len(dirs)):
        path_to_original = os.path.join(path_to_data, dirs[i])
        path_to_save = os.path.join(path_to_test_data, dirs[i])

        label_path_to_original = os.path.join(path_to_data, dirs[i] + "\\Label")
        label_path_to_save = os.path.join(path_to_save, "Label")

        #creates dir
        if not os.path.exists(path_to_save):
            os.makedirs(path_to_save)
        if not os.path.exists(label_path_to_save):
            os.makedirs(label_path_to_save)

        files = get_files_from_folder(path_to_original, extension=".jpg")
        label_files = get_files_from_folder(label_path_to_original, extension=".txt")

        # moves data corresponding to class counts
        for j in range(int(test_counter[i])):
            img_dst = os.path.join(path_to_save, files[j])
            img_src = os.path.join(path_to_original, files[j])

            shutil.move(dst = img_dst, src= img_src)
            for label in label_files:
              label_dst = os.path.join(label_path_to_save, label)
              label_src = os.path.join(label_path_to_original, label)
              if label[:-len(".txt")] == files[j][:-len(".jpg")]:
                shutil.move(dst = label_dst, src = label_src)
                break


def parse_args():
  parser = argparse.ArgumentParser(description="Dataset divider")
  parser.add_argument("--data_path", required=True,
    help="Path to data", default="dataset")
  parser.add_argument("--test_data_path_to_save", required=True,
    help="Path to test data where to save", default="dataset/test")
  parser.add_argument("--train_ratio", required=True,
    help="Train ratio - 0.7 means splitting data in 70 % train and 30 % test",default=0.7)
  return parser.parse_args()

if __name__ == "__main__":
  args = parse_args()
  main(args.data_path, args.test_data_path_to_save, float(args.train_ratio))