import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import html2text
import random
def generate_random_date(start_date_str, end_date_str):
    """
    生成两个日期之间的随机日期字符串。
    
    :param start_date_str: 开始日期字符串，格式为 'YYYY-MM-DD'
    :param end_date_str: 结束日期字符串，格式为 'YYYY-MM-DD'
    :return: 生成的随机日期字符串，格式为 'YYYY-MM-DD'
    """
    # 将日期字符串转换为 datetime 对象
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

    # 计算两个日期之间的差值
    delta = end_date - start_date

    # 生成一个随机天数
    random_days = random.randint(0, delta.days)

    # 计算随机日期
    random_date = start_date + timedelta(days=random_days)

    # 将随机日期转换回字符串格式
    return random_date.strftime('%Y-%m-%d')


url="https://segmentfault.com/blog/pingan8787?page="
base_url="https://segmentfault.com"
headers= {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cache-Control': 'no-cache',
  'Connection': 'keep-alive',
  'Cookie': '_ga=GA1.1.291472793.1722583552; Hm_lvt_e23800c454aa573c0ccb16b52665ac26=1728461270,1728524930,1728552510,1728613936; HMACCOUNT=96154F56E9F24BFB; PHPSESSID=a9c352e5150740e5e24c9a1c54551a6c; SHARESESSID=a9c352e5150740e5e24c9a1c54551a6c; acw_tc=2760823117286340243065964eb77d126a0e0aa5ef76acb0b73077160b098c; acw_sc__v2=6708dca8ee29b75c3afae4b5c9875d8ac60d5c28; _ga_MJYFRXB3ZX=GS1.1.1728634025.43.1.1728634036.0.0.0; Hm_lpvt_e23800c454aa573c0ccb16b52665ac26=1728634037; ssxmod_itna=eq0xgDn7GQ0Q0=eDQDXDyx3qYK7tDODL6DBR0Bw5c0u4xG==Yb=UUNNWdK=fDl=DAK3DnqD8D8x0iDC+RreTRoOxioDx9L3XabzlT+6sUD8AvxoppnL+iDHxY=DUc7h3HWDenbD5xGoDPxDYDG4DoP5DnhxDjxDdxzA+dtYDbxi3i4GCX2rp74DF7eBzO4i7DDHrXx07CiAeDGveu3x4UGvd74DrXpoKL+7qSt0Dx4G1CD0HDpjexzfRQd2wS3Q2F9uzDlI9DC9++zBfwi7mQ8OtYnu4YirP6ixFqnixoQwd6XGdbl4enarq7D2I5x3A3tBDC5DG8DbYh=WP4D==; ssxmod_itna2=eq0xgDn7GQ0Q0=eDQDXDyx3qYK7tDODL6DBR0Bw5c0u4xG==Yb=UUNNWdK=D62LXDDsqKBb4GaKYqE=eDf2O0K=YCeidtsCC805KU80c95Y7Pn8qoYofpLcPdKCnplKqtTerRKkP/FLaScGsLCpbkcDzH60rdYhxv271yOPr5ZP4o/9rSrmexEHaWoabYOHHo2BGGzmA427k4o9Df+iiarMFyEv7LUFf4ODbtrcptxE7a8Cit=whO93pY0AaclpTXBmdvPqsqn0Hv/Ie+g+G/p0FZPgHX2yf3w9M4ZZa96/hX1/i6q5+x6DZAN1oPmlIzom+hISiNDgXarwfGIKPioQGADUw7f1E5TZ36nov7L3ox6iQ4/K51oTEE4QLd+R5BmgBfuGD2jG7h5KcLr926Doq9+Xid406LQ=+FGuDYdgKdhpc6opowGmjZoWZmPPaoeYYYPay6XobRO4XOfQ2pL3EfFIjxBrlDYuS5n35rKemAvPB4wfjqxtD9A=bf4xNCoaf2Y5Ao/097+n23wLiGyEoKigy=bB80kQKUo2xhX4Yoo0TT5PyZP4QolCj6WTLQx=3aP47VevP2bUoWS3HqO9dsp9iogmF5=m4oRtaR5mlPcferefPwwnjh7mLG667La7i8Of6aADcSBoovB5PIEOU4K7T6pmk+bfGuzEEC+95nL+yjhy9yTOemyesEImetWR4QT4440qD07lPOWinm7DPMaTYPRrsrh+Wlo1LrVg46ibeK00u1rQhY4PbYQjKxmmmT9RZ0+ERnm3kT8CofnoFPjIxBey2Z0DsAe0wDg8AKBbVxeN0Phhp4rIeGB4D48GeYDD=',
  'Pragma': 'no-cache',
  'Sec-Fetch-Dest': 'document',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-User': '?1',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
  'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}
lists=['https://segmentfault.com/a/1190000006599500']
# for i in range(1,5):
#     res=requests.get(f'{url}{i}')
#     bs=BeautifulSoup(res.text,"html.parser")
#     listsss=bs.select(".container .title")
#     for i in listsss:
#         lists.append(base_url+i.get("href"))

for new_url in lists:
    print(new_url)
    res=requests.get(new_url,headers=headers)
    bs=BeautifulSoup(res.text,"html.parser")
    tag=bs.select("a.badge-tag")
    tag=[i.get_text() for i in tag] 
    title=bs.select_one(".h2 a.text-body").text.replace("|","").replace("?","").replace("/","")
    for i in bs.find_all('pre'):
        print(i)
        start=bs.new_tag("p")
        start.string = f"```js"
        end=bs.new_tag("p")
        end.string = "```"
        i.insert_before(start)
        i.insert_after(end)
    for i in bs.find_all('img'):
        i.decompose()
    for i in bs.find_all('script'):
        i.decompose()
    for i in bs.find_all('a'):
        i["href"]=""
    # print(res.text)
    article=bs.select_one("article.article")
    
    
    info="---\n"
    info+=f"date: {generate_random_date('2023-01-01','2024-09-30')}\n"
    info+="category:\n"
    info+=f"    - {tag[0]}\n"
    info+="tag:\n"
    for t in tag:
        info+=f"    - {t}\n"
    info+="---\n"
    markdown = html2text.html2text(article.prettify())
    markdown=f"{info} # {title}\n"+markdown
    markdown=markdown.replace('<script async src=" [ https://static.codepen.io/ass... ]() ;></script>',"")
    with open(f"./src/posts/other/{title}.md","w",encoding="utf-8") as f:
        f.write(markdown)