import requests
import json

def fetch_data(url, body):
    response = requests.post(url=url, json={"query": body})
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data from the API.")
        return None

def save_data_to_file(data, filename):
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=2)
    print(f"Data saved to '{filename}' successfully.")

def process_users_data(users_data):
    processed_data = []
    for user in users_data:
        processed_user = {
            "id": user["id"],
            "name": user["name"],
            "email": user["email"],
            "status": user["status"],
            "posts_count": len(user["posts"]["nodes"]),
            "todos_count": len(user["todos"]["nodes"])
        }
        processed_data.append(processed_user)
    return processed_data

if __name__ == "__main__":
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
    
    data = fetch_data(url, body)
    if data:
        users_data = data["data"]["users"]["nodes"]
        processed_data = process_users_data(users_data)
        print(json.dumps(processed_data, indent=2))
        save_data_to_file(processed_data, "processed_users_data.json")
