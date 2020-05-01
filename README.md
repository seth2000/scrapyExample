### Prerequisites

Things required, only test successfully<br>
1. Python3
2. Scrapy 
  ```
  conda install -c conda-forge scrapy
  or
  pip install Scrapy
  pip install scrapy-fake-useragent
  ```


### Usage


Start the search with a keyword. I used "contacts of ceos in Pakistan" as an example.
  ```python
  python -m scrapy crawl emailspider -o output.json
  or
  python -m scrapy crawl emailspider -o output.csv  
  ```
  

