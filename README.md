# SchoolWorksPro-File-Downloader
This Python script allows SchoolWorksPro users to download all the files in a module with just one command. The script uses the SchoolWorksPro API to authenticate the user and retrieve a list of all the files in the module. It then downloads all the files to a specified directory on the user's local machine.

## Installation
To install the dependencies for this project, run the following command:

```
pip install -r requirements.txt
```

## Usage
After installing the required modules, you can use this project by following these steps:

Open the schoolworks.py file in a code editor.
Change the following values in the script to match your own credentials and preferences:

* USER_NAME : 'your_schoolworkspro_username'
* PASSWORD : 'your_schoolworkspro_password'
* module_url : "https://schoolworkspro.com/modules/csc-1020-introduction-to-e-commerce-sunway"
* directory_path : 'path_to_save_downloaded_files'(optional)


Save the schoolworks.py file.
Open a command prompt or terminal window.
Navigate to the directory where the schoolworks.py file is located.
Run the following command to execute the script:

```
python schoolworks.py
```

This will run the script and download the files from the specified module URL to the directory you specified (or the default directory if you didn't specify one).

