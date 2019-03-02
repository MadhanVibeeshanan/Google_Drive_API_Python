# Google_Drive_API_Python
Accessing Files from Google Drive using Google Drive API in Python

Find the steps below to successfully access the file in your Google Drive.
The above-mentioned project was implemented using Anaconda Navigator. Install Anaconda Navigator -  https://www.anaconda.com/distribution/  or use any of the Python IDE of your choice. 

# Step 1: Enabling your API in the Google Cloud Platform
 
  	Search Google Cloud Platform in your web browser or use link the link https://cloud.google.com/gcp/?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-e-dr-1006141&utm_content=text-ad-none-any-DEV_c-CRE_113120492767-ADGP_Hybrid%20%7C%20AW%20SEM%20%7C%20BKWS%20%7C%20US%20%7C%20en%20%7C%20EXA%20~%20Google%20Cloud%20Platform-KWID_43700009942847400-kwd-26415313501&utm_term=KW_google%20cloud%20platform-ST_google%20cloud%20platform&gclid=EAIaIQobChMI-Z-R_q3a4AIVEhx9Ch2yzQZbEAAYASAAEgJ22_D_BwE
  
  	Sign in Google using your Gmail id. 
  
  	Click the console button on the top right corner
  
  	create a new project using Select a project dropdown button 
  
  	Creating project will take a few minutes. 
  
  	After creating project use the search bar to search for Google Drive API
  
  	Click Enable button
  
  	Click Create Credentials button
  
   Select Google Drive API from Drop Down List for Which API are you using option
  
  	We have to select Other UI (eg. Windows, CLI tool) option for where will you be calling the API from.
  
  	Select User data for What data will you be accessing
  
  	The select what credentials do I need the option. It will get you through the second step of Create an OAuth 2.0 client ID
  
  	Give the name for OAuth and select Create OAuth Client
  
  	Select your Gmail id
  
  	Type your product name
  
  	Press the continue button.
  
  	Download the Client ID by clicking the Download option. Your credentials will be downloaded in the json format. Make sure you rename   the file to client_secret and save the file to you python file directory. 


# Step 2: Setting up the environment for your python file.  
  
  	Before the actual coding, you need to install a few python libraries related to Google API. 
     •	!pip install httplib2
     •	!pip install google-api-python-client
     •	!pip install oauth2client	

  	Once you are done with installation. you are all set. 

  	clone the main.py file from the repository and run the program (make sure you have saved the client_secret.json file in your active 
python directory).
