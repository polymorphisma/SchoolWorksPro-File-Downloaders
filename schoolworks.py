import requests
import schoolworks_apis
import re
import os
import random
import string
from tqdm import tqdm

def return_access_token(USER_NAME, PASSWORD):
    """
        Sends a POST request to the SchoolWorks login API to obtain an access token for the given user credentials.

        Parameters:
        USER_NAME (str): The username of the user.
        PASSWORD (str): The password of the user.

        Returns:
        str: The access token if the request was successful, otherwise returns the string 'not valid'.
    """
    
    url = schoolworks_apis.login_api

    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.5",
        "content-type": "application/json",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sec-gpc": "1",
        "Referer": "https://schoolworkspro.com/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    
    payload = {
            "username": USER_NAME,
            "password": PASSWORD
        }
    
    response = requests.request('POST', url=url, headers=headers, json=payload)
    
    if response.status_code == 200:
        response = response.json()
        return response['token']
    
    return 'not valid'

def schoolworkspro_request(api_url, access_token):
    """
    Sends a GET request to the SchoolWorks API with the provided access token and returns the response as JSON.

    Parameters:
    api_url (str): The URL of the SchoolWorks API endpoint to send the request to.
    access_token (str): The access token to use for authentication.

    Returns:
    dict: The JSON response from the SchoolWorks API.
    """
    
    headers = {"Authorization": "Bearer {}".format(access_token)}
    payload = ""
    response = requests.request("GET", api_url, data=payload, headers=headers)
    return response.json()

def generate_random_string(n):
    """
    Generates a random string of length n using uppercase and lowercase letters and digits.

    Parameters:
    n (int): The length of the random string to generate.

    Returns:
    str: A randomly generated string of length n.
    """
    # Define the pool of characters to choose from
    chars = string.ascii_letters + string.digits
    
    # Generate a random string of length n
    return ''.join(random.choices(chars, k=n))

def generate_path(path):
    if os.path.exists(path):
        path += generate_random_string(10)
    return path

def main(USER_NAME, PASSWORD, module_url, directory_path=""):
    module_slang = module_url.split('/')[-1]

    if directory_path == "":
        current_dir = os.path.dirname(os.path.abspath(__file__))

        directory_path = os.path.join(current_dir, module_slang)

        os.mkdir(generate_path(directory_path))

    else:
        directory_path = os.path.join(directory_path, module_slang)
        os.mkdir(generate_path(directory_path))
        

    lesson_api_url = schoolworks_apis.lessons_request_api.format(module_slang)
    access_token = return_access_token(USER_NAME=USER_NAME, PASSWORD=PASSWORD)
    lesson_response = schoolworkspro_request(lesson_api_url, access_token)

    for lessons in tqdm(lesson_response['lessons']):
        for content in tqdm(lessons['lessons']):

            lesson_ = schoolworks_apis.lessons_link_api.format(content['lessonSlug'])

            link_response = schoolworkspro_request(lesson_, access_token)
            raw_links = link_response['lesson']['lessonContents']

            links = re.findall(r'href="(.*?)"', raw_links)

            save_path = os.path.join(directory_path, content['lessonTitle'].strip())

            os.mkdir(generate_path(save_path))

            for link in tqdm(links):

                file_name = link.split('/')[-1]
                file_path = os.path.join(save_path, file_name)

                response = requests.request('GET', link)

                with open(file_path, "wb") as f:
                    f.write(response.content)


if __name__ == '__main__':
    USER_NAME = "" # -> schoolworkspro username
    PASSWORD = "" # -> schoolworkspro password
    module_url = "" # -> module url
    directory_path = r"" #  -> where to save files

    main(USER_NAME, PASSWORD, module_url, directory_path)
 