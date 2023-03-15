import wikipedia

# Set language to English
wikipedia.set_lang("en")

# Search for a page
page = wikipedia.page("Allama Iqbal")

#printing everythign
print(page.content)

# Get the summary of the page
summary = page.summary

# Print the summary
# print(summary)