import json
from gpt_crawler import GPTCrawler

def load_config():
    with open('config.json', 'r') as file:
        return json.load(file)

def main():
    config = load_config()
    crawler = GPTCrawler(config)
    crawler.start()

if __name__ == "__main__":
    main()
