urls = ["https://google.com", "https://github.com", "https://invalid-url.com",""]



for n, link in enumerate(urls, 1):
    if link == "":
        print("Entry", n, "is blank")