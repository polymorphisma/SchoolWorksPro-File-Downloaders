# SchoolWorksPro-File-Downloaders
This Python script allows SchoolWorksPro users to download all the files in a module with just one command. The script uses the SchoolWorksPro API to authenticate the user and retrieve a list of all the files in the module. It then downloads all the files to a specified directory on the user's local machine.

# Installation
To install the dependencies for this project, run the following command:\n
pip install -r requirements.txt\n

# Usage
After installing the required modules, you can use this project by following these steps:\n

Open the schoolworks.py file in a code editor.\n
Change the following values in the script to match your own credentials and preferences:\n
USER_NAME: your schoolworkspro username\n
PASSWORD: your schoolworkspro password\n
module_url: the URL of the module you want to download files from\n
directory_path: the path of the directory where you want to save the downloaded files (optional)\n

USER_NAME = 'your_schoolworkspro_username'\n
PASSWORD = 'your_schoolworkspro_password'\n
module_url = "https://example.com/module_url"\n
directory_path = 'path_to_save_downloaded_files'\n

Save the schoolworks.py file.\n
Open a command prompt or terminal window.\n
Navigate to the directory where the schoolworks.py file is located.\n
Run the following command to execute the script:\n

python schoolworks.py\n
This will run the script and download the files from the specified module URL to the directory you specified (or the default directory if you didn't specify one).\n

Remember to replace "your_schoolworkspro_username", "your_schoolworkspro_password", "https://example.com/module_url", and "path_to_save_downloaded_files" with the actual values for your project.
