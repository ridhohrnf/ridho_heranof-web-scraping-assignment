import requests
import json

url ="https://gorest.co.in/public/v2/graphql"
body = """
query {
  users(first: 10) {
    nodes {
      id
      name
      email
      status
      posts(first: 5) {
        nodes {
          id
          title
          body
        }
      }
      todos(first: 5) {
        nodes {
          id
          title
          status
        }
      }
    }
  }
}
"""
 
response = requests.post(url=url, json={"query": body})
print("response status code: ", response.status_code)
if response.status_code == 200:
    data = response.json()  # Convert the response content to JSON format
    print(json.dumps(data, indent=2))  # Print the JSON data with indentation
    with open("user_data.json", "w") as json_file:  # Open a file in write mode
        json.dump(data, json_file, indent=2)  # Write the JSON data to the file with indentation
    print("Data saved to 'user_data.json' successfully.")
else:
    print("Failed to fetch data from the API.")