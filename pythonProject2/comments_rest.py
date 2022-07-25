from rest import Rest
import requests

class CommentsRest(Rest):
    def __init__(self):
        super().__init__()

    def retrieve_comments(self, api_url, header):
        return super().get_data(api_url, header)

    def create_comment(self, todo, api_url, header):
        super().post(todo, api_url, header)

    def delete_object(self, api_url, nume, header):
        for item in self.get_data(api_url, header):
            print(item)
            if item["name"] == nume:
                api_url = api_url + '/' + str(item["id"])
                response = requests.delete(api_url, headers=header)
                print(response.status_code)
                if response.status_code == 200:
                    print("A fost sters")