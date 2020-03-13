import requests, re, time
from colorama import init, Fore
init(convert=True)

def start():

    url = "https://discordservers.me/servers/search?term=Nitro&page="
    numb = 1
    session = requests.Session()
    print(f"[{Fore.CYAN}>{Fore.RESET}] Input Discord Token")
    token = input(" > ")

    while int(numb) < 100:
        time.sleep(2)
        response = session.get(url + str(numb)).text

        regex = re.search("https(:)\/\/discord.gg\/[a-zA-Z0-9]+", response)

        if regex:
            code = str(regex.group()).split("/")[3]
            
            headers = {
                "Authorization": token
            }

            inviteResp = session.post(f"https://discordapp.com/api/v6/invites/{code}", headers=headers).json()

            if inviteResp["guild"]["name"]:
                print(f"[{Fore.CYAN}Success{Fore.RESET}] Joined the server: {inviteResp['guild']['name']}")

        else:
            pass
        numb+=1
    input("")

if __name__ == "__main__":
    start()
