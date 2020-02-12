# Generic Model Training Setup
This repository contains generic deep learning experiments setup.
## Structure
The folder structure contains following items:
`dataloader`: folder containing pyTorch dataloaders for different datasets. 
`models`: folder containing actual model definition.
`utils`: folder containing all the utility functions that is not under dataloader / utilities.
`configs`: folder containing yaml files for experiment configutations
`tests`: folder containing unit tests for each modules.
`doc`: folder containing documentations
`bin`: folder containing scripts for running.

## Development
In order to develop from this repo please do following.

1. Implement data loaders for different datasets.
2. Implement models.
  - Implement baseline model
  - Implement experimental model
3. Implement utils functions.
  - Implement logger for tensorboard
  - Implement evaluation functions
4. Implement binary functions.
  - Implement train.py that uses dataloader / utils / models.
  - Implement test.py that uses dataloader / utils / models.
5. Implement unit tests
6. Fill in the documentations.

## Running Experiment
All the experimental setups should be setup under configs/EXPERIMENT_NAME.yaml

i.e) in order to run any experiments, it should follow this format:
`python bin/train.py --config-file=configs/EXPERIMENT_NAME.yaml`

in order to test with trained experiments, it should follow this format:
`python bin/test.py --config-file=configs/EXPERIMENT_NAME.yaml`

## Distribution
In order to distribute this code, please edit setup.py

