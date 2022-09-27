import csv
import re
import json
import requests









# # Builds list of URLs for senators to grab candidate_id from FEC
# list_of_senators = []

# with open('listofsens.txt', 'r') as f:
#     reader = csv.reader(f)
#     for i in reader:
#         for j in i:
#             list_of_senators.append(j)
#
# list_of_query_strings = []
#
# for i in list_of_senators:
#     j = i.replace(' ', '%20')
#     k = 'api_key=BEYZOlqUaTtunyHiKleP6Qi8rYdTquSyYn9vsMex&q=' + j + '&page=1&sort=name&per_page=20&office=S'
#     list_of_query_strings.append(k)
#
# list_of_urls = []
#
# for i in list_of_query_strings:
#     j = 'https://api.open.fec.gov/v1/candidates/search/?' + i
#     list_of_urls.append(j)
#
# with open('listofurls.txt', 'w') as f:
#     for i in list_of_urls:
#         f.write(i + '\n')



# # Takes list of URLs, queries each one, and builds a new list of candidate_ids
# url_list = []
# with open('listofurls.txt', 'r') as f:
#     for i in f:
#         i = i.rstrip('\n')
#         url_list.append(i)
#
# list_of_candidate_ids = []
# k = 0
# for j in url_list:
#     response = requests.get(j)
#     response = response.text
#     response = json.loads(response)
#     k += 1
#     print(response['results'][0]['candidate_id'], " ", k)
#     list_of_candidate_ids.append(response['results'][0]['candidate_id'] + '\n')
#
# with open('listofcandidateids.txt', 'w') as f:
#     for i in list_of_candidate_ids:
#         f.write(i)


# list_of_candidate_form_2_urls = []
#
# with open('listofcandidateids.txt', 'r') as f:
#     for i in f:
#         j = i.rstrip('\n')
#         list_of_candidate_form_2_urls.append('https://api.open.fec.gov/v1/candidate/' + j + '/filings/?api_key=BEYZOlqUaTtunyHiKleP6Qi8rYdTquSyYn9vsMex&sort_hide_null=false&per_page=20&sort_null_only=false&form_type=F2&office=S')
#
# print(list_of_candidate_form_2_urls)
#
# with open('listofform2urls.txt', 'w') as f:
#     for i in list_of_candidate_form_2_urls:
#         f.write(i + '\n')




list_of_csv_urls = []
a = 0

with open('listofform2urls.txt', 'r') as f:
    for i in f:
        j = i.rstrip('\n')
        response = requests.get(j)
        response = response.text
        response = json.loads(response)
        a += 1
        print(response['results'][0]['csv_url'])
        list_of_csv_urls.append(response['results'][0]['csv_url'])

with open('listofcsvurls.txt', 'w') as f:
    for x in list_of_csv_urls:
        if x is None:
            f.write("NONE" + '\n')
        else:
            f.write(x + '\n')













# #  Reads the CSV file that is downloaded from the FEC and scrapes official and authorized committee ID numbers
# with open('1615482.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     csv_contents = ""
#     for i in csv_reader:
#         csv_contents += str(i)
#     list_of_ids = re.findall(r'\b[C][0-9]{8}', csv_contents)
#
# principal_campaign_committee = list_of_ids[0]
#
# print(list_of_ids)





