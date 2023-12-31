# email2api
Makes interacting with an API as easy as emailing a friend.

Example usage:

``` import email2api
send_to = "data@example.com"
subject = "api_key: 123456"
message = "mom’s birthday: June 6, mom’s name: Gladys"
response = email2api.send(send_to, message, subject)
print(response)
```
