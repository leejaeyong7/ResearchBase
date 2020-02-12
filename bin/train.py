# -*- coding: utf-8 -*-
""" Entry file for training."""
import sys
sys.path.append('.')
sys.path.append('..')
import argparse
import logging
from tqdm import tqdm
import yaml
import torch
from time import time

from powerpoint import PowerPoint
from utils.trainer import Trainer
from utils.saver import Saver
from utils.validator import Validator
from utils.logger import Logger

logging.basicConfig(level='INFO',
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


def main(experiment_name: str,
         config: dict,
         dataset_path: str,
         logging_path: str,
         checkpoint_path: str,
         resume: bool,
         device: str):
    '''
    args:
      config(dict): configuration object for this experiment.
        @see docs/config.md for detailed structure
    '''
    pass

############################
# -- Main Program entry -- #
############################
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # logging related arguments

    # path to config file
    # config file name (without .yaml / .yml) is treated as experiment name
    parser.add_argument('--config-file', type=str, required=True,
                        help='yaml file that contains config')

    # path to dataset directory
    parser.add_argument('--dataset-dir', type=str, required=False,
                        default='./data',
                        help='Dataset directory')

    # path to logging directory for tensorboard
    parser.add_argument('--logging-dir', type=str, required=False,
                        default='./logs',
                        help='Logging directory')

    # device ID
    parser.add_argument('--device', type=int, required=False,
                        default=None,
                        help='Device to use for training. CPU by Default')

    # path to checkpoint directory.
    # if there are checkpoint that has same experiment name as this run,
    # it will try to continue from that file
    # you can disable that option by specifying --no-resume option
    parser.add_argument('--checkpoint-dir', type=str, required=False,
                        default='./checkpoints',
                        help='Checkpoint directory')

    # WARNING: setting this to true will override existing checkpoints
    parser.add_argument('--no-resume', type=bool, required=False,
                        default=False,
                        help='whether to resume from last checkpoint or not.')

    parser.set_defaults()
    args = parser.parse_args()

    # parse yaml file from input, and
    config_filename = args.config_file.split('/')[-1]
    experiment_name = '.'.join(config_filename.split('.')[:-1])
    with open(args.config_file, 'r') as f:
        try:
            config = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            logging.error("Invalid YAML")
            logging.error(exc)

    # warn user for resume option
    if args.no_resume:
        logging.warning('No-Resume options is on. This will overwrite existing checkpoints')

    # log experiment name
    logging.info("Running experiment: {}".format(experiment_name))
    device = 'cpu' if args.device is None else 'cuda:{}'.format(args.device)

    main(experiment_name,
         config,
         args.dataset_dir,
         args.logging_dir,
         args.checkpoint_dir,
         not args.no_resume,
         device)
