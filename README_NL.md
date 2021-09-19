
Project Setup

After cloning the git repo and checking out the correct branch, build the docker image using the Dockerfile.gpu in the build folder. The tfrecord data files should be placed in “../data/waymo_processed” relative to the repo folder.


Training Command

python experiments/model_main_tf2.py --model_dir=training/improved4/ --pipeline_config_path=training/improved4/pipeline_new.config

Testing on Validation Command

python experiments/model_main_tf2.py --model_dir=training/improved4/ --pipeline_config_path=training/improved4/pipeline_new.config --checkpoint_dir=training/improved4/

Testing on Testing Command

python experiments/model_main_tf2.py --model_dir=training/improved4/ --pipeline_config_path=training/improved4/pipeline_new_test.config --checkpoint_dir=training/improved4/
