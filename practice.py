urls = ["https://google.com", "https://github.com", "https://invalid-url.com"]
     
def link(urls):
    n = 1 
    for link in urls:
        
        print(str(n)+".",urls)
        n= n+1
    
    return(n)

check_urls= link(urls)
print(check_urls)