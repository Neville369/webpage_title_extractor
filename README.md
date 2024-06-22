# webpage_title_extractor
This Python script reads a list of URLs from a text file and prints the title of each webpage. Here's a detailed description:

1. **Importing Libraries**:
   - `BeautifulSoup` from the `bs4` library for parsing HTML content.
   - `requests` for making HTTP requests.
   - `lxml` for HTML parsing.
   - `re` for regular expression operations (though it isn't used in the provided code).

2. **Reading URLs from a Text File**:
   - The script opens a file named `urls.txt` in read mode.
   - It reads each line, strips leading/trailing whitespace, and removes any trailing commas.
   - The processed URLs are stored in a list named `urls`.

3. **Defining a Function to Get the Title of a Webpage**:
   - The `get_title` function takes a URL as input.
   - It sends an HTTP GET request to the URL.
   - If the request is successful, it parses the HTML content using `BeautifulSoup` with `lxml` parser.
   - It extracts and returns the text within the `<title>` tag.
   - If an exception occurs during the request (e.g., network issues, invalid URL), it returns `None`.

4. **Iterating Over the URLs and Printing Titles**:
   - The script iterates through each URL in the `urls` list.
   - For each URL, it calls the `get_title` function.
   - It prints the title of the webpage, prefixed with the URL.

This script is useful for extracting and displaying the titles of multiple webpages, which can be helpful for various web scraping or content verification tasks.
