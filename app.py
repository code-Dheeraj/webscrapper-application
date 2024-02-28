import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import shutil

def scrape_and_export_first_five_tables(url, output_folder):
    try:
        # Send an HTTP GET request to the specified URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all tables on the webpage
        tables = soup.find_all('table')

        csv_files = []

        # Iterate through the first 5 tables and extract content
        for i, table in enumerate(tables):
            table_class = table.get('class', [])
            table_name = table.get('name', f"Table_{i+1}")

            # Extract content of the table using pd.read_html()
            table_content = extract_table_content(table)

            if table_content is not None:
                # Export table content to CSV
                file_name = f"{table_name}_data.csv"
                csv_files.append({
                    'table_name': table_name,
                    'file_name': file_name
                })
                export_csv(table_content, os.path.join(output_folder, file_name))

        return csv_files

    except requests.exceptions.RequestException as e:
        st.error(f"Error scraping website: {e}")
        return None

def extract_table_content(table):
    # Use pd.read_html() to convert the table to a DataFrame
    try:
        table_df = pd.read_html(str(table), header=0)[0]
        return table_df
    except Exception as e:
        st.warning(f"Error extracting table content: {e}")
        return None

def export_csv(dataframe, file_path):
    try:
        dataframe.to_csv(file_path, index=False)
        st.success(f"Table content exported to {file_path}")
    except Exception as e:
        st.error(f"Error exporting to CSV: {e}")

# Streamlit UI
st.title("Web Scraper and CSV Downloader")

# Input box for website URL
website_url = st.text_input("Enter website URL:")

# Output folder selection
output_folder = st.text_input("Enter output folder path:", "output")

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Scrape and download buttons
if st.button("Scrape and Download Tables"):
    if website_url:
        # Scrape tables and get CSV file info
        csv_files_info = scrape_and_export_first_five_tables(website_url, output_folder)

        if csv_files_info:
            # Provide download buttons for each CSV file
            for file_info in csv_files_info:
                st.download_button(
                    label=f"Download {file_info['table_name']} Table",
                    data=open(os.path.join(output_folder, file_info['file_name']), 'rb').read(),
                    file_name=file_info['file_name'],
                )

# Download all button
if st.button("Download All Tables"):
    if website_url:
        # Scrape tables and get CSV file info
        csv_files_info = scrape_and_export_first_five_tables(website_url, output_folder)

        if csv_files_info:
            try:
                # Create a zip file containing all CSV files
                zip_file_path = os.path.join(output_folder, 'all_tables.zip')
                with shutil.ZipFile(zip_file_path, 'w') as zip_file:
                    for file_info in csv_files_info:
                        file_path = os.path.join(output_folder, file_info['file_name'])
                        zip_file.write(file_path, file_info['file_name'])

                # Provide a download button for the zip file
                st.download_button(
                    label="Download All Tables (ZIP)",
                    data=open(zip_file_path, 'rb').read(),
                    file_name='all_tables.zip',
                )

            except Exception as e:
                st.error(f"Error creating ZIP file: {e}")
