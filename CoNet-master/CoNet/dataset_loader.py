import os

import numpy as np
import PIL.Image
import scipy.io as sio
import torch
from torch.utils import data

class MyData(data.Dataset):  # inherit
    """
    load data in a folder
    """
    mean_rgb = np.array([0.447, 0.407, 0.386])
    std_rgb = np.array([0.244, 0.250, 0.253])
    def __init__(self, root, transform=False):
        super(MyData, self).__init__()
        self.root = root

        self._transform = transform

        img_root = os.path.join(self.root, 'train_images')
        lbl_root = os.path.join(self.root, 'train_masks')
        depth_root = os.path.join(self.root, 'train_depth')
        edge_root = os.path.join(self.root, 'train_edge')

        file_names = os.listdir(img_root)
        self.img_names = []
        self.lbl_names = []
        self.depth_names = []
        self.edge_names = []
        for i, name in enumerate(file_names):
            if not name.endswith('.jpg'):
                continue
            self.lbl_names.append(
                os.path.join(lbl_root, name[:-4]+'.png')
            )
            self.img_names.append(
                os.path.join(img_root, name)
            )
            self.depth_names.append(
                os.path.join(depth_root, name[:-4] + '.png')
            )
            self.edge_names.append(
                os.path.join(edge_root, name[:-4] + '.png')
            )

    def __len__(self):
        return len(self.img_names)

    def __getitem__(self, index):
        # load image
        img_file = self.img_names[index]
        img = PIL.Image.open(img_file)
        # img = img.resize((256, 256))
        img = np.array(img, dtype=np.uint8)
        # load label
        lbl_file = self.lbl_names[index]
        lbl = PIL.Image.open(lbl_file)
        # lbl = lbl.resize((256, 256))
        lbl = np.array(lbl, dtype=np.int32)
        lbl[lbl != 0] = 1
        # load depth
        depth_file = self.depth_names[index]
        depth = PIL.Image.open(depth_file)
        # depth = depth.resize(256, 256)
        depth = np.array(depth, dtype=np.uint8)
        # load edge
        edge_file = self.edge_names[index]
        edge = PIL.Image.open(edge_file)
        edge = np.array(edge, dtype=np.uint8)



        if self._transform:
            return self.transform(img, lbl, depth, edge)
        else:
            return img, lbl, depth, edge


    # Translating numpy_array into format that pytorch can use on Code.
    def transform(self, img, lbl, depth, edge):

        img = img.astype(np.float64)/255.0
        img -= self.mean_rgb
        img /= self.std_rgb
        img = img.transpose(2, 0, 1)  # to verify
        img = torch.from_numpy(img).float()
        lbl = torch.from_numpy(lbl).long()
        depth = depth.astype(np.float64)/255.0
        depth = torch.from_numpy(depth).float()
        edge = edge.astype(np.float64) / 255.0
        edge = torch.from_numpy(edge).long()
        return img, lbl, depth, edge


class MyTestData(data.Dataset):
    """
    load data in a folder
    """
    mean_rgb = np.array([0.447, 0.407, 0.386])
    std_rgb = np.array([0.244, 0.250, 0.253])


    def __init__(self, root, transform=False):
        super(MyTestData, self).__init__()
        self.root = root
        self._transform = transform

        img_root = os.path.join(self.root, 'test_images')
        file_names = os.listdir(img_root)
        self.img_names = []
        self.names = []

        for i, name in enumerate(file_names):
            if not name.endswith('.jpg'):
                continue
            self.img_names.append(
                os.path.join(img_root, name)
            )
            self.names.append(name[:-4])


    def __len__(self):
        return len(self.img_names)

    def __getitem__(self, index):
        # load image
        img_file = self.img_names[index]
        img = PIL.Image.open(img_file)
        img_size = img.size
        # img = img.resize((256, 256))
        img = np.array(img, dtype=np.uint8)


        if self._transform:
            img = self.transform(img)
            return img, self.names[index], img_size
        else:
            return img, self.names[index], img_size

    def transform(self, img):
        img = img.astype(np.float64)/255.0
        img -= self.mean_rgb
        img /= self.std_rgb
        img = img.transpose(2, 0, 1)
        img = torch.from_numpy(img).float()

        return img
