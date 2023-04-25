 
import requests
import pandas as pd
import schoolworks_apis
import re
import os
import random
import string

USER_NAME = '' # -> schoolworkspro username
PASSWORD = '' # -> schoolworkspro password
module_url = "" # -> module url
directory_path = '' #  -> where to save files


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

def return_api_url(url):
    """
    Takes a SchoolWorks module URL and returns the corresponding API URL for making a lessons request.

    Parameters:
    url (str): The URL of the SchoolWorks module.

    Returns:
    str: The API URL for making a lessons request for the specified module.
    """
    module_slang = url.split('/')[-1]
    return schoolworks_apis.lessons_request_api.format(module_slang)

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

def parse_lesson_response(response):
    """
    Takes a JSON response from the SchoolWorks API and extracts the 'lessons' field. 
    Then converts the data into a Pandas DataFrame.

    Parameters:
    response (dict): The JSON response from the SchoolWorks API.

    Returns:
    pandas.DataFrame: A DataFrame containing the lesson data extracted from the JSON response.
    """
    response = response['lessons']

    df = pd.DataFrame({})

    for res in response:
        df = pd.concat([df, pd.DataFrame(res['lessons'])])

    return df

def parse_raw_link(string):
    """
    Parses a string for all href links and returns them as a list.

    Parameters:
    string (str): The string to parse for href links.

    Returns:
    list: A list of href links extracted from the provided string.
    """
    hrefs = re.findall(r'href="(.*?)"', string)
    return hrefs

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


if directory_path == '':
    dir = os.path.dirname(os.path.abspath(__file__))
    directory_path = os.path.join(dir, module_url.split('/')[-1])
    try:
        os.mkdir(directory_path)
    except FileExistsError:
        os.mkdir(directory_path+generate_random_string(10))

lesson_url = return_api_url(module_url)
access_token = return_access_token(USER_NAME=USER_NAME, PASSWORD=PASSWORD)
lesson_response = schoolworkspro_request(lesson_url, access_token)
module_df = parse_lesson_response(lesson_response)

for ind, row in module_df.iterrows():
    lesson_ = schoolworks_apis.lessons_link_api.format(row['lessonSlug'])
    link_response = schoolworkspro_request(lesson_, access_token)
    raw_links = link_response['lesson']['lessonContents']
    links = parse_raw_link(raw_links)

    save_path = os.path.join(directory_path, row['lessonTitle'].strip())

    try:
        os.mkdir(save_path)
    except FileExistsError:
        os.mkdir(save_path+generate_random_string(10))

    for link in links:
        file_name = link.split('/')[-1]
        file_path = os.path.join(save_path, file_name)
        response = requests.request('GET', link)
        with open(file_path, "wb") as f:
            f.write(response.content)