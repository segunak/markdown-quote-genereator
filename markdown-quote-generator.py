import sys
import csv

def generate_markdown(quote, source, source_url, jekyll_target_blank=True):
    target_blank = "" if not jekyll_target_blank else "{:target=\"_blank\"}"
    if source_url:
        return f"> {quote}\n>\n> <cite>[{source}]({source_url}){target_blank}</cite>"
    else:
        return f"> {quote}\n>\n> <cite>{source}</cite>"

def convert_csv_to_markdown(file_path, jekyll_target_blank=True):
    markdown = ""

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for row in reader:
            quote = row[0].strip('"')
            source = row[1].strip('"')
            source_url = row[2].strip('"') if len(row) > 2 else None
            markdown += generate_markdown(quote, source, source_url, jekyll_target_blank) + "\n\n"

    return markdown


csv_path = sys.argv[1] if len(sys.argv) > 1 else "quotes.csv"
markdown = convert_csv_to_markdown(csv_path)

with open("output.md", "w") as file:
    file.write(markdown)

