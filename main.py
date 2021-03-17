from bs4 import BeautifulSoup
import requests as req

response = req.get('https://www.revistabula.com/7073-a-lista-definitiva-dos-100-melhores-filmes-de-todos-os-tempos/')
bula_web_page = response.text

soup = BeautifulSoup(bula_web_page, "html.parser")

div_name_movies = soup.find_all(name='div', class_="shortcode-featured-title")

names = [tag.getText() for tag in div_name_movies]

with open('movies.txt', mode='w') as file:
    index = 1
    for name in names:
        file.write(f"{index}. {name}\n")
        index += 1