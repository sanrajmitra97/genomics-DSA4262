# genomics-DSA4262
NUS DSA4262 Genomics Project
- Step 1: Launch AWS and navigate to your home directory using the command: ``` $ cd ~ ```
- Step 2: Create a virtual envionment by running the following bash commands:
  - Install pip ``` $ sudo apt-get install python3-pip ```
  - Intall virtualenv ``` $ sudo pip3 install virtualenv ```
  - Check that you have downloaded virtualenv using the command: ``` $ virtualenv --version ```
  - Replace 'venv name' with a name for your virtual environment.``` $ virtualenv 'venv name' ```
  - Activate your virtual envionment ``` $ source 'venv name'/bin/activate ```
- Step 3: git clone this repository using the command: ``` $ git clone https://github.com/sanrajmitra97/genomics-DSA4262.git ```
- Step 4: Locate the requirements.txt file and run the following command: ``` $ pip install -r /path/to/requirements.txt ```
- Step 5: Once done, cd to the src folder: ``` $ cd src ```
- Step 6: Run the following command: ``` $ python train_model.py ```
  - You will be prompted to add a name for the model. Feel free to add any name for the model. For example, "model1". 
  - The results of the model's training performance will also be printed. 
  - This model is also saved in a "models" folder in the parent directory of src.
- Step 7: Run the following command while still in the src folder: ``` $ python make_pred.py ```
  - The model trained in the previous step will be used for making predictions on a small test dataset.
- Step 8: The predictions of the test dataset will be located in a folder called 'Results' in the parent directory of src. 
 
