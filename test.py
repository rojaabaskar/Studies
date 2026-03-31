urls = ["https://google.com", "https://github.com", "https://invalid-url.com",""]
     
def Check_urls(urls):
    if len(urls)==0:                    # condition to check the empty list 
        print("No URLs provided")
    else: 
       
        for n , link in enumerate(urls, 1):
            if link =="":   # Empty strings inside the list 
                print("Entry "+str(n)+":","Blank, URL is not provided.") 
                
            else:
                print(str(n)+".", link)   # loop through each URL
                

Check_urls(["", "https://github.com", ""]) # calling the fucntion with a list along with few blank data