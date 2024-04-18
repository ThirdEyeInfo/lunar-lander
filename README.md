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
- Run below python command to train your Lunar Module and generate video.mp4
    * python render.py
![image](https://github.com/ThirdEyeInfo/lunar-lander/assets/93641638/b8000816-ddf1-46c3-8c1d-e853bff4291c)

- Find video.mp4 under lunar-lander folder, play it to witness the landing of Lunar Lander as shown in below
![image](https://github.com/ThirdEyeInfo/lunar-lander/assets/93641638/c26a9152-3a7e-4a4a-aa5e-b4771ba795b5)



