import scrape

lojas = {
    "magalu":{
        "nameXpathUn": "/html/body/div[3]/div[5]/div/div[4]/div[1]/h1",
        "nameXpathAv": "/html/body/div[3]/div[5]/div[1]/div[3]/h1",
        "naXpath": "/html/body/div[3]/div[5]/div/div[4]/div[2]/p[1]",
        "priceXpath": "/html/body/div[3]/div[5]/div[1]/div[4]/div[2]/div[4]/div/div[2]/div/span[2]"
    },
    "americanas":{
        "nameXpathUn": '/html/body/div[1]/div/div[3]/div[1]/div[2]/span',
        "nameXpathAv": '/html/body/div[1]/div/div[3]/div[1]/div[2]/span',
        "naXpath": '/html/body/div[1]/div/div[3]/div[2]/div[1]/form',
        "priceXpath": '/html/body/div/div/div[3]/div[2]/div[1]/div[1]/div'
    },
    "pontofrio":{
        "nameXpathUn": '/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div/div/div/h1',
        "nameXpathAv": '/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div/div/div/h1',
        "naXpath": '//*[@id="titleAvailability"]',
        "priceXpath": '/html/body/div[1]/div[2]/div[2]/div[2]/div[5]/div[1]/div/p[2]/span[1]'
    },  
    "shopb":{
        "nameXpathUn": '//*[@id="corpo"]/div/div[1]/div/div[1]/div[2]/div/div[1]/h1',
        "nameXpathAv": '//*[@id="corpo"]/div/div[1]/div[1]/div[1]/div[2]/div/div[1]/h1',
        "naXpath": '//*[@id="corpo"]/div/div[1]/div/div[1]/div[2]/div/div[2]/div[1]/div/div',
        "priceXpath": '//*[@id="corpo"]/div/div[1]/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div[1]/strong'
    },
    "extra":{
        "nameXpathUn": '/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div/div/div/h1',
        "nameXpathAv": '/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div/div/div/h1',
        "naXpath": '//*[@id="titleAvailability"]',
        "priceXpath": '/html/body/div[1]/div[2]/div[2]/div[2]/div[5]/div[1]/div/p[2]/span[1]'
    },
    "casasbahia":{
        "nameXpathUn": '/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div/div/div/h1',
        "nameXpathAv": '/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div/div/div/h1',
        "naXpath": '//*[@id="titleAvailability"]',
        "priceXpath": '/html/body/div[1]/div[2]/div[2]/div[2]/div[5]/div[1]/div/p[2]/span[1]'
    },
}

def filter(loja, urls):
    nameXpathUn = lojas[loja]["nameXpathUn"]
    nameXpathAv = lojas[loja]["nameXpathAv"]
    naXpath = lojas[loja]["naXpath"]
    priceXpath = lojas[loja]["priceXpath"]
    for url in urls:
        scrape.start(loja, url, naXpath, priceXpath, nameXpathUn, nameXpathAv)

# if __name__ == "__main__":
#     filter('magalu', 1)