import httpx


login_payload = {
  "email": "my@user.com",
  "password": "1111"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()


headers = {"Authorization": f"Bearer {login_response_data['token']['accessToken']}" }
get_me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
print(get_me_response.json())
print(get_me_response.status_code)
