import sys, requests, bs4

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green

url = sys.argv[1]

res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

anchors = soup.select('a')

for anchor in anchors:
    href = anchor.get('href')
    if not href.startswith('http'):
        if href.endswith('/'):
            href = url + href
        else:
            href = url + '/' + href
    res = requests.get(href)
    if res.status_code == 200:
        print('[' + G + str(res.status_code) + W + '] ', end='')
    else:
        print('[' + R + str(res.status_code) + W + '] ', end='')
    print(href)
