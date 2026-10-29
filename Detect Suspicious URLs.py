url = input("Enter URL: ").lower()

words = ["login", "verify", "free", "password", "account", "winner"]
found = [word for word in words if word in url]

if found:
    print("Warning: Suspicious keywords detected!")
    print("Keywords:", found)
else:
    print("No suspicious keywords detected.")