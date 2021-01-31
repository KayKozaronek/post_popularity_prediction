#/bash
# a bash script to setup the environment for the project

# install pip3 and virtualenv
sudo apt-get install python3-pip -y

# create the virutual environment in the project root
pip3 install virtualenv
virtualenv -p python3 post_popularity_prediction_env

# activate the virtual environment
source post_popularity_prediction_env/bin/activate

# install packages you will need
pip3 install -r setup/requirements.txt

# Custom Kernel
python3 -m ipykernel install
python3 -m ipykernel install — user — name post_popularity_prediction_env — display-name "Post Popularity Prediction"
