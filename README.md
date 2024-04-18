## Step to train Lunar Lander model
- Clone lunar-lander in your local machine
- Download and install Anaconda from https://www.anaconda.com/download
- Type anaconda on windows search and open anaconda command prompt
- Navigate to lunar-lander progect (in step 1) from conda prompt and/by follow below commands
    * cd <basepath>/lunar-lander
    * conda create -n lunar-lander python=3.11 -y
    * conda activate lunar-lander
    * conda install swig -y
    * pip install -r requirements.txt
    * python setup.py install
- Run below python command to train your Lunar Module
    * python src\trainer.py