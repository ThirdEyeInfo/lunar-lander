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
- Run below python command to train your Lunar Module and wait until below message appears
    * python src\trainer.py
  ![image](https://github.com/ThirdEyeInfo/lunar-lander/assets/93641638/40c5e8c4-f24d-44f3-b33e-c7e97a69d170)
