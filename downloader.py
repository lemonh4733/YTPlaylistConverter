from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
line = "-----------------------"

print(line+"\nChoose Download Type: ")
print("\n1) Playlist ")
print("2) Songs array \n"+line+"\n")
choice = int(input())
print("\nPlease wait...")

if choice == 1:
    from playlist import links
elif choice == 2:
    from links import links
else:
    print("Bad input ERORR")
    time.sleep(3)
    exit()

chromedriver = './chrome/chromedriver'
class YTDownloader():
    def __init__(self):
        self.bot = webdriver.Chrome(chromedriver)
    def download(self, link):
        self.link = link
        bot = self.bot
        bot.get('https://ytmp3.cc/en13/')
        link = bot.find_element_by_xpath('//*[@id="input"]')
        link.clear()
        link.send_keys(self.link)
        time.sleep(2)
        link.send_keys(Keys.RETURN)
        time.sleep(5)
        try:
            downloadBTN = bot.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/a[1]")
            downloadBTN.click()
            anotherSong = bot.find_element_by_xpath("//*[@id='buttons']/a[3]")
            anotherSong.click()
        except Exception as ex:
            time.sleep(5)



song = YTDownloader()
for i in range(len(links)):
    song.download(links[i])
    print(str(len(links)-(i+1))+" songs left!")
print(line+"\nDownload successful!!")
exit()