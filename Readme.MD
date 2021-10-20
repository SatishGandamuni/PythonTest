## Markdown file for python documentation
### Introduction

1. Install python 3.7 or above from [Python code](https://www.python.org/downloads/)
2. Install visual studio code - any version - 1.58.1 
3. Install Python extension for Visual studio code by selecting Python Extension in "Extension" tab
4. Once done, create a folder for your work.e.g. c:/PythonWork_CRUDWorkspace
5. Open that folder in Visual studio and create a file with python extension (.py)
6. Copy requirements.txt, createWorkspace.py, updateWorkspace.py, readWorkspace.py, deleteWorkspace.py, and workspace.env files to working folder. The workspace.env file is where we pass the parameters with our desired inputs and configure Databricks workspace
7. Open a new terminal and install/upgrade pip by running install 
8. Now run this command - pip install -r requirements.txt

### Create a plain vanilla Workspace
1. For validating creation of Databricks workspace, please utilize the createWorkspace.py script and workspace.env file. Please note that all the parameters have to be string in workspace.env file.
2. Few of the pre-requisites for validating this scenario would be
	#### a) Run the Az login command in the terminal and login in the browser to authenticate your credentials into Azure
	#### b) Using RP BugBash subscription, create a Resource Group in the Azure portal
    
3. In the Visual studio code, open the workspace.env and specify the parameters of the existing code and save;
	#### a) Specify the name of the existing Resource Group [String]
	#### b) Name of the Databricks Workspace to be created 
	#### c) SKU tier of the workspace
	#### d) Location of the workspace
	#### e) Enable No Public IP (Secure Connectivity cluster) [Optional]. Specify "True" to set NPIP enabled. Default value is "False"

4. The data type for all environmental variables in workspace.env file is string. Keep in mind to configure all parameters with "". Enable NPIP is a boolean parameter, either True or False. No need to configure MRG for this scenario since MRG will be generated randomnly

5. Copy the path of workspace.env and make sure to specify it as a Path argument on line 22 in createWorkspace.py. (./Workspace.env is dynamic)
6. Save all and run the command "Python createWorkspace.py" in the terminal
7. You should be able to see the workspace created in the resource group in Azure Portal within the Azure RP bug bash subscription

### Update a Databricks Workspace
1. For validating update on a Databricks Workspace, please utilize the updateWorkspace.py script and workspace.env file
2. Few of the pre-requisites for validating this scenario would be
	#### a) Run the Az login command in the terminal and login in the browser to authenticate your credentials into Azure
	#### b) Using RP BugBash subscription, make sure to take a note of the MRG from the export template of the databricks workspace. The MRG ID should be in syntax like "/subscriptions/subscription_id/resourceGroups/databricks-rg-myNPirufnvdqf4"

3. In the Visual studio code, open the workspace.env and specify the parameters of the existing code and save;
	#### a) You can perform update on tags and SKU, but not on NPIP configuration.  You can change the SKU tier in workspace.env file and you can specify tags on line 67 in updateWorkspace.py script.
	#### b) Specify the same details such as ResourceGroup, name of workspace, location. You might need to specify the MRG for updation to happen. Also, you may change the SKU tier of the workspace if needed. All these changes have to be done in the workspace.env file

4. Copy the path of workspace.env and make sure to specify it as a Path argument on line 22 in UpdateWorkspace.py.
5. Save all and run the command - Python updateWorkspace.py, in the terminal
6. Refresh your workspace. You should be able to see tags updated and SKU tier to be changed, if specified alternate SKU.

### Read a Databricks Workspace
1. For validating read operation on a Databricks Workspace, please utilize the ReadWorkspace.py script and workspace.env file
2. In the Visual studio code, open the workspace.env and specify the parameters of the existing code and save;
	#### a) Run the Az login command in the terminal and login in the browser to authenticate your credentials into Azure
	#### b) Make sure to specify the name of the Resource Group and name of the workspace you would like to read in the workspace.env file
	#### c) You can update tags on line 63 in ReadWorkspace.py [optional]

3. Copy the path of workspace.env and make sure to specify it as a Path argument on line 22 in ReadWorkspace.py.
4. Save all and run the command "Python ReadWorkspace.py" in the terminal
5. You should be able to see the details of the workspace in the terminal

### Delete a Databricks Workspace
1. For validating delete operation on a  Databricks Workspace, please utilize the deleteWorkspace.py script and workspace.env file
2. In the Visual studio code, open the workspace.env and specify the parameters of the existing code and save;
	#### a) Run the Az login command in the terminal and login in the browser to authenticate your credentials into Azure
	#### b) Make sure to specify the name of the Resource Group and name of the workspace you would like to delete in the workspace.env file. (Note: This operation only deletes the Databricks Workspace)

3. Copy the path of workspace.env and make sure to specify it as a Path argument on line 22 in deleteWorkspace.py.
3. Save all and run the command "Python deleteWorkspace.py" in the terminal
4. You should be able to see the workspace status to be in deleting state