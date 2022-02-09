import requests

if __name__ == '__main__':
    data = open('./byxlogo.png', 'rb').read()
    res = requests.post(url='https://image.groupme.com/pictures',
                        data=data,
                        headers={'Content-Type': 'image/png',
                                 'X-Access-Token': 'rLuheSG4Swp8V0rWCOGA4uIHDQzoHabwKPrmDW9a'})
    print(res.content)