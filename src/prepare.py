from dataset import Data
from utils import *


class Prepare:

    def __init__(self, train_dataset, val_dataset, test_dataset, path_to_yolo):
        assert isinstance(train_dataset, Data), "torchdataset object must be inherited from Data class."
        assert isinstance(val_dataset, Data), "torchdataset object must be inherited from Data class."
        assert isinstance(test_dataset, Data), "torchdataset object must be inherited from Data class."
        self.train_dataset = train_dataset
        self.val_dataset = val_dataset
        self.test_dataset = test_dataset

        assert os.path.exists(path_to_yolo), f"Cannot reach {path_to_yolo}"
        self.path_to_yolo = os.path.join(path_to_yolo, 'data')

    def check_datasets(self):
        print("Checking Dataset 🔥🔥🔥...")
        check_dataset(self.train_dataset)
        check_dataset(self.val_dataset)
        check_dataset(self.test_dataset)
        print("All set to go 🚀🚀🚀")

    def create(self):
        self.check_dataset()
        create_folders_for_yolo(self.path_to_yolo)
        move_files(self.train_dataset,
                   os.path.join(self.path_to_yolo, 'dataset/images/train'),
                   os.path.join(self.path_to_yolo, 'dataset/labels/train')
                   )
        move_files(self.val_dataset,
                   os.path.join(self.path_to_yolo, 'dataset/images/val'),
                   os.path.join(self.path_to_yolo, 'dataset/labels/val')
                   )
        move_files(self.test_dataset,
                   os.path.join(self.path_to_yolo, 'dataset/images/test'),
                   os.path.join(self.path_to_yolo, 'dataset/labels/test')
                   )

        print("All set to go 🚀🚀🚀")


