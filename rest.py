import requests

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    response = requests.get("http://api.open-notify.org/astros.json")
    print(response)

    print(response.content) # Return the raw bytes of the data payload
    print(response.text) # Return a string representation of the data payload
    print(response.json) # This method is convenient when the API returns JSON