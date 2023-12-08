import json

# Open the JSON file for reading
with open('oral_pseudonymise.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Open the JSON file for reading
with open('written_pseudonymise.json', 'r', encoding='utf-8') as file:
    data2 = json.load(file)

# Create a dictionary to keep track of content occurrences
content_occurrences = {}

# Create a new list to store the cleaned data
cleaned_data = []
cleaned_data2 = []

# Create a list to store duplicate entries
duplicates = []
duplicates2 = []

for entry in data:
    content = entry["content"]
    if content not in content_occurrences:
        content_occurrences[content] = 1
        cleaned_data.append(entry)
    elif content_occurrences[content] == 1:
        content_occurrences[content] += 1
    else:
        duplicates.append(entry)

for entry2 in data2:
    content2 = entry2["content"]
    if content2 not in content_occurrences:
        content_occurrences[content2] = 1
        cleaned_data2.append(entry2)
    elif content_occurrences[content2] == 1:
        content_occurrences[content2] += 1
    else:
        duplicates2.append(entry2)

# Write the cleaned data to a new JSON file
with open('cleaned_oraldata.json', 'w', encoding='utf-8') as file:
    json.dump(cleaned_data, file, ensure_ascii=False, indent=4)

# Write the cleaned data to a new JSON file
with open('cleaned_writtendata.json', 'w', encoding='utf-8') as file:
    json.dump(cleaned_data2, file, ensure_ascii=False, indent=4)

# Write the list of duplicate entries to a new JSON file
with open('oralduplicates.json', 'w', encoding='utf-8') as dup_file:
    json.dump(duplicates, dup_file, ensure_ascii=False, indent=4)

# Write the list of duplicate entries to a new JSON file
with open('writtenduplicates.json', 'w', encoding='utf-8') as dup_file:
    json.dump(duplicates2, dup_file, ensure_ascii=False, indent=4)