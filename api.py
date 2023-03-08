import requests

# content是用户前端输入的内容
json_data = {"status": 1, "content": "c++的二叉树前序遍历"}

r = requests.post("http://127.0.0.1:5000/add", json=json_data)

print(r.text)