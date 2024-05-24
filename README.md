# ladd-and-weights
Metadata of Lacmus dataset and trained model weitghts tracked with dvc. 


## Usage
Repository in intended to sustain reproducability and versioning of the dataset and model weights.

- Install our fork of [dvc](https://dvc.org), becouse original dvc has an [issue](https://github.com/iterative/dvc/issues/7303)
```
conda create -n lacmus-dvc python==3.9 pip
conda activate lacmus-dvc
git clone https://github.com/lacmus-foundation/dvc.git
cd dvc
pip install .
```

- In order to get access to cloud storage, contact lacmus team as described on wiki and get your `credentials` file.
- Put credentials to `~/.aws/`
- Configure dvc and get data:
```
git clone https://github.com/lacmus-foundation/ladd-and-weights.git
cd ladd-and-weights
dvc remote modify --local digital_ocean credentialpath ~/.aws/credentials
dvc pull
```

- to gather LADD  from relevant parts run `python merge.py` to merge with heridal dataset and convert to yolov5 format for training refer to https://github.com/lacmus-foundation/lacmus-research/blob/master/extra/EDA/LADDvsIPSAR_merge_and_prepare.ipynb

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
