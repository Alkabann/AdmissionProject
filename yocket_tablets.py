import requests
from lxml import html

USERNAME = "aymeric.laugel@laposte.net"
PASSWORD = "xanuzo72"

BASE_URL = "https://yocket.in"
LOGIN_URL = "https://yocket.in/account/login"
URL = "https://yocket.in/recent-admits-rejects?page="

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='_csrfToken']/@value")))[0]

    # Create payload
    payload = {
        "username": USERNAME, 
        "password": PASSWORD, 
        "_csrfToken": authenticity_token
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
    result = session_requests.get(URL, headers = dict(referer = URL))
    tree = html.fromstring(result.content)
    text_to_script = tree.xpath("//title/text()")	#devrait afficher Admit and Reject mais affiche Login Account...

    for i in text_to_script:
            if(i != '\n'):
                print(i)



if __name__ == '__main__':
    main()