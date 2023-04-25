# SchoolWorksPro-File-Downloaders
This Python script allows SchoolWorksPro users to download all the files in a module with just one command. The script uses the SchoolWorksPro API to authenticate the user and retrieve a list of all the files in the module. It then downloads all the files to a specified directory on the user's local machine.

# Installation
To install the dependencies for this project, run the following command:
pip install -r requirements.txt

# Usage
After installing the required modules, you can use this project by running the following steps:

changes values in:
USER_NAME = '' # -> schoolworkspro username /n
PASSWORD = '' # -> schoolworkspro password
module_url = "" # -> module url
directory_path = '' #  -> where to save files(Optional)


after changing values run following command:
python schoolworks.py
