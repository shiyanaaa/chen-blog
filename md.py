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
  'Cookie': 'acw_tc=2760821e17286274486064279ea74f0f3b70e9b2aebd27dbf46d26b0a7e105; SHARESESSID=03796010c449809c20d980a4bc7cf9da; PHPSESSID=8b1527be4df94396ea080a042af133a0; Hm_lvt_e23800c454aa573c0ccb16b52665ac26=1728627449; Hm_lpvt_e23800c454aa573c0ccb16b52665ac26=1728627449; HMACCOUNT=818561313C1512DB; _ga_MJYFRXB3ZX=GS1.1.1728627449.1.0.1728627449.0.0.0; _ga=GA1.1.1341766831.1728627450; ssxmod_itna=eu0=qAxfEGCDOKDXDyx3qYK7tDOGczDCOYjGTRBxD5Dkz3iiWaxIEibrPPGXxPoDSxD=D6D7YDtohAQD0Ygru538fi2tfnGfGauz2lta2wzLYTCiTeqS1BgqoDU4i8DCwKlxjmDYYmDt4DIDAYDDxDWDYESDGtdDG=D7E0P1l2qxi3DbhbDmkt=RmTD0R+4VLTD4qDBe8tDKTqek4Dl8SFc7hNFBeD+ILTdzpr8SpG4x0t=DBdPFUE4HpOvk8RzdID=ygNDzwkDtMrTHlciijbYce3e9gxemB=1U8D8KipKiAo87gZ5SfPkGvviqYiDS=q1QhvAiDDp4n4CAhDD=; ssxmod_itna2=eu0=qAxfEGCDOKDXDyx3qYK7tDOGczDCOYjGTRBxD5Dkz3iiWaxIEibrPA=ZaaD/7h7DGaFa0BjsNQ8jrhsYY+mK6sPdF1orD0iCD=Fia0SL4+nWCpIHeQE=Bf7+YAhKBiXt/RR3GFWhYVKBQ4Oo3x5Ajn/xExZ+I5/oiVm3RstuNM7kbxqWdPRlxY6bpKeCPn+kYWhWb36nfRlLjqUSnxubbBeQ9A3bTawRt43R=FtnX5m+DnmCiE/QU3rTBxM+Y2/rOjEEhL0FPA3RLi2ldniDCXeSvT1P2jj+OnB8kP+i0uWo+6k0tAr5cAj8Bov665eox2KL=GKioPC3kG0roA5+IVQG50eVj56n2QaGN1Ax0UKC34CoXEvyevnCIKmpBlDPA5fYo=KAemUAiEH7=8io4lEvrYEAQUCIdaoCg4w0p5AqDQFxl9a7vQC4bfSy8Ii4nqzRHCA50GZQ0iU8xeD=; SHARESESSID=8b1527be4df94396ea080a042af133a0',
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
lists=[]
for i in range(1,5):
    res=requests.get(f'{url}{i}')
    bs=BeautifulSoup(res.text,"html.parser")
    listsss=bs.select(".container .title")
    for i in listsss:
        lists.append(base_url+i.get("href"))
for new_url in lists:
    print(new_url)
    res=requests.get(new_url,headers=headers)
    print(res.text)
    bs=BeautifulSoup(res.text,"html.parser")
    tag=bs.select("a.badge-tag")
    tag=[i.get_text() for i in tag] 
    title=bs.select_one(".h2 a.text-body").text.replace("|","").replace("?","").replace("/","")
    for i in bs.find_all('img'):
        i.decompose()
    for i in bs.find_all('script'):
        i.decompose()
    for i in bs.find_all('a'):
        print(i)
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
    markdown=markdown.replace("<","&lt;")
    markdown=markdown.replace(">","&gt;")
    with open(f"D:/code/chen-blog/src/posts/other/{title}.md","w",encoding="utf-8") as f:
        f.write(markdown)