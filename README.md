# ddc_mapping
Project to produce a dataset that maps Dewey Decimal Classification (DDC) numbers to their associated classes, divisions, and sections.

I was having difficulty finding a simple dataset that mapped DDC numbers to their classes, divisions, and sections.  I wrote this script which parses the data and produces CSV and JSON files as a result, which I have included.  The pdftotext utility is required.

Usage:

$ pdftotext ddc23-summaries.pdf   # Parse pdf to text data

$ python3 parse_ddc.py < ddc23-summaries.txt
