import webbrowser as wb


def webauto():
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    URLS = ("stackoverflow.com","gmail.com","google.com", "youtube.com")

    for url in URLS:
        print("Opening: " + url)
        wb.get(chrome_path).open(url)


webauto()