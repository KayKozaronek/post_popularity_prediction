import requests
import requests_cache
import json
import pandas as pd
import csv 

requests_cache.install_cache()


INIT_POST = 22201337
REQUEST_AMOUNT = 140

def get_item(post_id):
    """
    This function takes an ID and returns
    the corresponding Hacker News Item
    Items can be of type:
        - story
        - comment 
        - ask 
        - job 
        - poll
        - poll parts 
    """
    url =  f"https://hacker-news.firebaseio.com/v0/item/{post_id}.json?print=pretty"

    response = requests.get(url)

    return response

def jprint(obj):
    """
    This function receives an JSON object as input.
    It returns a Python f-string.
    It allows us to see the results of our request.
    """
    text = json.dumps(obj, sort_keys = True, indent=4)
    print(text)
    
#jprint(get_post(INIT_POST).json())
#print(type(get_post(INIT_POST).json()))


# Prepare header names for csv files
headers = {
    "story" : ["id", "by", "descendants", "kids", "score", "time", "title", "type", "url"],
    "comment" : ["id", "type", "by", "time", "text", "parent", "kids"],
    #"ask" : ["by", "descendants", "id", "kids", "score", "text", "time", "title", "type"],
    "job" : ["id", "type", "by", "time", "text", "url", "score", "title"],
    "poll" : ["id", "type", "by","time", "text", "kids", "score", "title", "parts", "descendants"],
    "pollopt" : ["by", "id", "poll", "score", "text", "time", "type"],
    #"user" : ["id", "created", "karma", "about", "submitted"]
}

csv_files = {
    "story":"stories.csv",
    "comment":"comment.csv",
    "job":"job.csv",
    "poll":"poll.csv",
    "pollopt":"pollopt.csv"
}

# Initialize empty lists
data_lists = {
    "story": [],
    "comment": [],
    "job": [],
    "poll": [],
    "pollopt": []
}

# Make API requests
for i in range(REQUEST_AMOUNT):
    response = get_item(INIT_POST - i).json()
    # Appends response to corresponding list
    if (("deleted" in response.keys()) or ("dead" in response.keys())):
            continue
    data_lists[response["type"]].append(response)

# Write data to csv.files   
for category in data_lists:
    try: 
        with open(csv_files[category], "w", encoding= "utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers[category])
            writer.writeheader()
            for data in data_lists[category]:
                writer.writerow(data)

    except IOError:
        print("I/O error")


# if __name__ == "main":
#     main()