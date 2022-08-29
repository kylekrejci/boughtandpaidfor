import requests
import os
import json
import pymongo

bearer_token = os.environ.get("BEARER_TOKEN")
search_url = "https://api.twitter.com/2/tweets/search/recent"
query_params = {'query': 'from:JoeBiden'}
source_account = "JoeBiden"

def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "paid_4_by"
    return r

def search_connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    # print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def compare_and_write_or_update_latest_tweet_id_to_db(source_account, latest_tweet_id):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["paid_4_by"]
    coll = db["latest_tweet_id_table"]
    document = {'account': source_account, 'latest_id': latest_tweet_id}
    cursor = coll.find(document)
    if len(list(cursor)) == 1:
        return "Already Latest Tweet"
    else:
        document_update_result = coll.update_one({'account': source_account}, {'$set': {'latest_id': latest_tweet_id}})
        if document_update_result.acknowledged:
            return "Tweet Updated Successfully"
        else:
            return "DB Write Error"

def main():
    json_response = search_connect_to_endpoint(search_url, query_params)
    # print(json.dumps(json_response, indent=4, sort_keys=True))
    latest_tweet_id = json_response['meta']['newest_id']
    print(latest_tweet_id)
    compare_and_write_result = compare_and_write_or_update_latest_tweet_id_to_db(source_account, latest_tweet_id)
    print(compare_and_write_result)

if __name__ == "__main__":
    main()