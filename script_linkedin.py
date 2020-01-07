from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from parsel import Selector


def validate(field):
    if field:
        pass
    else:
        field = ''
    return field



driver = webdriver.Chrome('chromedriver')
driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

email = driver.find_element_by_id('username')
email.send_keys('EMAIL')
sleep(0.5)

password = driver.find_element_by_id('password')
password.send_keys('SENHA')
password.send_keys(Keys.ENTER)
sleep(2)


driver.get('http://www.google.com')

search_query = driver.find_element_by_name('q')
search_query.send_keys('site:/linkedin.com/in/ desenvolvedores python')
search_query.send_keys(Keys.RETURN)
sleep(3)
linkedin_urls = driver.find_elements_by_tag_name('cite')
linkedin_urls = [url.text for url in linkedin_urls]
sleep(0.5)


for link in linkedin_urls:
   link = link.split(' › ')
   if link[1].isalpha() == False:
     pass
   else:
     link = 'https://br.linkedin.com/in/'+link[1]
     print(link)
     driver.get(link)
     sleep(2)
     
     sel = Selector(text=driver.page_source)
     nome = sel.xpath('//title/text()').extract_first().split(' | ')[0]
     ocupacao = sel.xpath('//h2/text()').extract_first().strip()
     cidade = sel.xpath('//*[@class="t-16 t-black t-normal inline-block"]/text()').extract_first().strip()
     formacao_academica = sel.xpath('//*[contains(@class, "pv-entity__school-name")]/text()').extract()
     
     
     print('Nome: {}'.format(nome))
     print('Ocupacao: {}'.format(ocupacao))
     print('Cidade: {}'.format(cidade))
     print('Formacao academica: {}'.format(formacao_academica))
     print('\n')


driver.quit()

