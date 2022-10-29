# genomics-DSA4262
NUS DSA4262 Genomics Project
- Step 1: Launch AWS and navigate to your home directory using the command: ``` $ cd ~ ```
- Step 2: Create a virtual envionment by running the following bash commands:
  - Install pip ``` $ sudo apt-get install python3-pip ```
  - Intall virtualenv ``` $ sudo pip3 install virtualenv ```
  - Check that you have downloaded virtualenv using the command: ``` $ virtualenv --version ```
  - Replace 'venv name' with a name for your virtual environment.``` $ virtualenv 'venv name' ```
  - Activate your virtual envionment ``` $ source 'venv name'/bin/activate ```
 - Step 3: git clone this repository. 
 - Step 4: Locate the requirements.txt file and run the following command: ``` $ pip install -r /path/to/requirements.txt ```
 - Step 5: Once done, cd to the src folder: ``` $ cd src ```
 - Step 6: Run the following command: ``` $ python make_pred.py ```
 - Step 7: Once done, the results csv file will be located in a folder called 'Results' in the parent directory of src. 
 
