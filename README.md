# ladd-and-weights
Metadata of Lacmus dataset and trained model weitghts tracked with dvc. 


## Usage
Repository in intended to sustain reproducability and versioning of the dataset and model weights, if you want just look around and play with dataset, some version of it still available at https://cloud.mail.ru/public/2k53/2bJVwYSa7

In order to get ssh access to cloud storage, contact lacmus team as described on wiki

To get latest version on artefacts 
- Install dvc (https://dvc.org/doc/install), simpliest way for ubuntu `snap install --classic dvc`
- Either just download files without checking it out 
	- Get dataset with `dvc get https://github.com/lacmus-foundation/ladd-and-weights dataset`
	- Get model weights with `dvc get https://github.com/lacmus-foundation/ladd-and-weights weights`
- Or checkout repository and then get files (this option will let you create PRs and update dataset and weights)
	- `git clone  https://github.com/lacmus-foundation/ladd-and-weights`
	- `dvc pull`
- to gather dataset for training from relevant parts run `dvc repro gather-LADD`

## Contributing

In case you'll add new imagesSet, please also update dvc.yaml and gather_LADD.sh 

## Project structure
	\
	- dataset
		-- pretrain
			--- sdd-lacmus-version - Prepared Standford Dron Dataset
			--- VisDrone2019-DET VisDone Dataset
		-- LADD
			---
			...  folders part of dataset, gathered as project evolves 
			--- 
	- weights 
		-- keras-retinanet - weights for keras retina-net model (https://github.com/lacmus-foundation/lacmus/tree/master/keras_retinanet)
		-- torch
			--- pretrain
			--- experimental

