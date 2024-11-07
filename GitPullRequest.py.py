# Program to get the list of pull requests from Kubernetes GitHub using Git api

import requests

def get_api_url():
    url=f'https://api.github.com/repos/kubernetes/kubernetes/pulls'
    return url

def get_pull_request(url):
    url_response=requests.get(url)
    #to check the type of response
    print(type(url_response))
    #to get the status code
    print(url_response.status_code)
    #to convert the response to json
    if url_response.status_code==200:
        complete_data=url_response.json()
        
        #empty dictionary for count
        count_user= {}

        for data in complete_data:
            user=data['user']['login']
            if user in count_user:
                count_user[user]+=1
            else:
                count_user[user]=1

        #print the users and count of pull request
        for name,count in count_user.items():
            print(f"{name}:{count}")
            

def main():
    url=reponse=get_api_url()
    get_pull_request(url)
    
if __name__=="__main__":
   main()


