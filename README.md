# Web Scraper and CSV Downloader

## Overview

This Python-based application leverages Streamlit, BeautifulSoup, and Pandas to create a user-friendly web scraper and CSV downloader. Users can input a website URL, scrape tables from the webpage, and download the table data as CSV files. The application provides options to download individual tables or a zip file containing all tables.

## Features

- **Scrape and Download Tables:** Input a website URL, click the "Scrape and Download Tables" button, and download individual CSV files for each table found on the webpage.

- **Download All Tables (ZIP):** Use the "Download All Tables" button to generate a zip file containing CSV files for all tables.

- **User-friendly Interface:** Streamlit UI allows easy interaction. Users can specify the output folder for downloaded files.

## Usage

1. **Installation:**
   - Ensure you have Python installed.
   - Install dependencies: `pip install -r requirements.txt`

2. **Run the App:**
   ```bash
   streamlit run app.py
   ```

3. **Usage:**
   - Enter the target website URL in the provided text input.
   - Specify the output folder (default is "output").
   - Click the "Scrape and Download Tables" button to download individual tables or use the "Download All Tables" button for a zip file.

## Screenshots

[I![image](https://github.com/code-Dheeraj/webscrapper-application/assets/72144099/036ebdc4-673d-4b16-9bc5-3aa2c544f6fb)
![image](https://github.com/code-Dheeraj/webscrapper-application/assets/72144099/c7c2edc3-5bb2-4b8a-8b00-c3a964049700)
![image](https://github.com/code-Dheeraj/webscrapper-application/assets/72144099/b0ceb79f-a383-48cf-9de4-28b2bcde3840)
![image](https://github.com/code-Dheeraj/webscrapper-application/assets/72144099/cca65b83-66ff-4a3b-bee9-45fab19ea603)

]

## Demo

[https://www.linkedin.com/posts/dheeraj-singh-8062311b8_python-datascience-webscraping-activity-7168530665355816964-AaEl?utm_source=share&utm_medium=member_desktop]

## Contributing

Contributions and feedback are welcome! If you find any issues, have feature requests, or want to contribute, please open an issue or submit a pull request.

## Areas of Improvement

While the application serves its purpose, there are areas where improvements can be made:

1. **Error Handling:** Implement more robust error handling to gracefully handle situations like invalid URLs, network errors, or unexpected HTML structures.

2. **User Feedback:** Provide clearer feedback to users during the scraping and downloading process. Display loading indicators or messages to keep users informed.

3. **Table Detection Logic:** Enhance the logic for detecting and selecting tables on the webpage. Currently, it assumes all tables are relevant, which might not be the case for every website.

4. **Compatibility:** Ensure compatibility with a broader range of websites and handle edge cases where the HTML structure deviates from the assumed norms.

5. **Logging:** Implement logging to capture and review errors or issues that may occur during the scraping and downloading process.

## Link for demo
https://capital-asset-pricing-model-dheeraj.streamlit.app/
