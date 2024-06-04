import PyPDF2
import time

def print_loading_bar(iteration, total, length=30):
    percent = f"{100 * (iteration / float(total)):.1f}"
    filled_length = int(length * iteration // total)
    bar = '#' * filled_length + '-' * (length - filled_length)
    print(f'\r|{bar}| {percent}%', end='\r')
    if iteration == total:
        print()

def extract_pages(input_pdf_path, output_pdf_path, start_page, end_page):
    # Open the input PDF file
    with open(input_pdf_path, 'rb') as input_pdf_file:
        reader = PyPDF2.PdfReader(input_pdf_file)
        
        # Check if the specified range is within the document
        num_pages = len(reader.pages)
        if start_page < 1 or end_page > num_pages:
            raise ValueError(f"The document has only {num_pages} pages. Specified range {start_page}-{end_page} is out of bounds.")
        
        # Create a PDF writer object
        writer = PyPDF2.PdfWriter()
        
        # Calculate the total number of pages to be added
        total_pages = end_page - start_page + 1
        
        # Add pages from the specified range to the writer and update the progress bar
        for i, page_num in enumerate(range(start_page - 1, end_page)):
            page = reader.pages[page_num]
            writer.add_page(page)
            print_loading_bar(i + 1, total_pages)
            time.sleep(0.01)  # Optional: simulate a delay for better visualization of the loading bar
        
        # Write the output PDF file
        with open(output_pdf_path, 'wb') as output_pdf_file:
            writer.write(output_pdf_file)

# Define the input and output file paths
input_pdf_path = 'path'
output_pdf_path = r'path'

# Define the range of pages to extract
start_page = "add the number of the page without the brackets"
end_page = "add the number of the page without the brackets"

# Extract the pages
extract_pages(input_pdf_path, output_pdf_path, start_page, end_page)

print("Extraction complete!")
