import requests
import telegram
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

bot = telegram.Bot(token = '5396545974:AAEZl9YZY8pF2jye_dcJh_0oR_IfyDBZNAU')
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0199&date=20220504'

def job_function():
    html = requests.get(url)
    #print(html.text)

    soup = BeautifulSoup(html.text, 'html.parser')
    imax = soup.select_one('span.imax')
    if(imax):
        imax = imax.find_parent('div', class_='col-times')
        title = imax.select_one('div.info-movie > a > strong').text.strip()
        bot.sendMessage(chat_id = 5128747328, text =  title + "IMAX 예매가 열렸습니다.")
        sched.pause()
        # 굳이 예매가 열리지 않았을때 알림을 보내줄 필요가 없다.
    # else:
    #     bot.sendMessage(chat_id = 5128747328, text = "IMAX 예매가 아직 열리지 않았습니다.")
        # print('IMAX 예매가 아직 열리지 않았습니다.')

sched = BlockingScheduler(timezone = 'Asia/Seoul')
sched.add_job(job_function, 'interval', seconds = 30)
sched.start()
