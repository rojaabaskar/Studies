urls = ["https://google.com", "https://github.com","","https://invalid-url.com",""]
     
def summarise_urls(urls):
    # printing the length of the list 
    print("Total:", len(urls))
    # validiating the list
    valid = 0
    blank = 0

    for link in urls:
        if link != "":
            valid += 1
        else:
            blank += 1
    
        print("Valid:", valid)
        print("Blank:", blank)

summarise_urls(urls)

