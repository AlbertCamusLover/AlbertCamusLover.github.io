import csv

def csv_to_html(csv_file_path):
    html_output = ""

    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip header row if present

        for row in reader:
            if len(row) < 4:
                continue  # Skip rows with missing data

            character = row[0].strip()
            tagline = row[1].strip()
            tags_raw = row[2].strip()
            tags = [tag for tag in tags_raw.split() if tag]  # space-separated
            link = row[3].strip()

            tag_spans = "\n              ".join([f'<span class="tag">{tag}</span>' for tag in tags])

            html_block = f'''
  <div class="bot window p-4" data-tags="{tags_raw}"> 
    <div class="window-header">{character}</div> 
    <div class="mt-3 text-base">
      {tagline}
    </div>
    <div class="mt-2">  
      {tag_spans}
    </div>
    <a href="{link}" target="_blank" class="button-link">Chat with Bot</a>
  </div>'''
            html_output += html_block + "\n"

    return html_output


def getTextFile(output):
    f = open("myBots.txt", "w")
    f.write(output)
    f.close

getTextFile(csv_to_html('sheet.csv'))