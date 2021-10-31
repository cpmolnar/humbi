import os.path
from data.base_dataset import BaseDataset
from data.image_folder import make_dataset
import pandas as pd
from util import pose_utils
import numpy as np
import torch

class HMUBIDataset(BaseDataset):

    @staticmethod
    def modify_commandline_options(parser, is_train):
        parser = BaseDataset.modify_commandline_options(parser, is_train)
        if is_train:
            parser.set_defaults(load_size=256)
        else:
            parser.set_defaults(load_size=256)
        parser.set_defaults(old_size=(256, 256))
        parser.set_defaults(structure_nc=18)
        parser.set_defaults(image_nc=3)
        parser.set_defaults(display_winsize=256)
        return parser

    def get_paths(self, opt):
        if opt.phase == 'test':
            root = os.path.join(opt.dataroot, 'test')
            pairLst = os.path.join(opt.dataroot, 'pairs-test.txt')
        elif opt.phase == 'train':
            root = os.path.join(opt.dataroot, opt.phase)
            pairLst = os.path.join(opt.dataroot, 'pairs-train.txt')
        phase = opt.phase
        name_pairs = self.init_categories(pairLst)
        
        image_dir = os.path.join(root, 'image')
        bonesLst = os.path.join(root, 'keypoints')
        return image_dir, bonesLst, name_pairs


    def init_categories(self, pairLst):
        import os
        print(os.getcwd())
        pairs_file_train = pd.read_csv(pairLst, sep=' ', header=None)
        size = len(pairs_file_train)
        pairs = []
        print('Loading data pairs ...')
        for i in range(size):
            pair = [pairs_file_train.iloc[i][0], pairs_file_train.iloc[i][1]]
            pairs.append(pair)

        print('Loading data pairs finished ...')  
        return pairs    

    def name(self):
        return "HMUBIDataset"

                