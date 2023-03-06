# ladd-and-weights
Metadata of Lacmus dataset and trained model weitghts tracked with dvc. 


## Usage
Repository in intended to sustain reproducability and versioning of the dataset and model weights.

In order to get access to cloud storage, contact lacmus team as described on wiki and put credentials to `~/.aws/`
(or other folder and configure it with `dvc remote modify --local digital_ocean credentialpath <path_to_file>`)

To get latest version on artefacts 
- Install dvc (https://dvc.org/doc/install) with conda `conda install -c conda-forge dvc dvc-s3`
- Unfortunately there is an issue in DVC https://github.com/iterative/dvc/issues/7303, prefenting to fetch some files. To fetch data until issue is fixed you need to apply workaround, described in issue to <your_conda_path>/envs/<your_conda_environment_name>/lib/python<your_python_version_in_this_env>/site-packages/dvc/fs/base.py  
- Fork repository, checkout it and then get files (this option will let you create PRs and update dataset and weights)
	- `git clone  https://github.com/<your_github_with_forked_repo>/ladd-and-weights`
	- `dvc pull`
- to gather LADD  from relevant parts run `dvc repro gather-LADD` to merge with heridal dataset and convert to yolov5 format for training refer to https://github.com/lacmus-foundation/lacmus-research/blob/master/extra/EDA/LADDvsIPSAR_merge_and_prepare.ipynb

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
		-- unmarked
			---
			... folders of file sets, submitted by users, but not yet included into main dataset
			---
		-- 3rd_party
			--- heridal - http://ipsar.fesb.unist.hr/HERIDAL%20database.html (*) 
	- weights 
		-- yolo5 - wieghts for yolo v5 (https://github.com/ultralytics/yolov5) currently in production 
		-- keras-retinanet - weights for keras retina-net model (https://github.com/lacmus-foundation/lacmus/tree/master/keras_retinanet) - previous version of network
		-- torch
			--- pretrain
			--- experimental
		
----
(*) Dunja Božić-Štulić, Željko Marušić, Sven Gotovac: Deep Learning Approach on Aerial Imagery in Supporting Land Search and Rescue Missions, International Journal of Computer Vision, 2019.
