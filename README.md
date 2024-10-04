# Web News Scraping with Python

This repository contains a web scraping project aimed at extracting news data from the detik.com website. The scraper retrieves the following information from the news articles:
- News Link: The URL link to the original news article.
- Title: The headline of the news article.
- Author: The author or writer of the news article (if available).
- Date: The publication date of the news article.
- Image URL: The URL of the main image associated with the news article.
- Content: The main content or body of the news article.

### Installation
1. Clone the repository:
```
git clone https://github.com/rakaarfi/news-scraper.git
cd news-scraper
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```
### Usage
To run the scraper, simply execute the following command:

```
python main.py
```

The scraped data will be stored in a dictionary format, where each entry contains the following fields: `Link`, `Title`, `Author`, `Date`, `Image URL`, and `Content`.
