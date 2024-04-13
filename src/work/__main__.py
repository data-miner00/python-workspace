import requests

# Perform any work within the block (entry point)
if __name__ == "__main__":
    print("Initiating work...")

    SCRAPE_ENDPOINT = "https://jsonplaceholder.typicode.com/posts"
    res = requests.options(SCRAPE_ENDPOINT)
    print(res.headers)
