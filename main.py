from parser import Parser
from product_parser import ParserProduct


link = "https://www.avito.ru/sankt-peterburg/telefony/iphone_x_64_gb_2302159263"
# parser = Parser(link)
parser_product = ParserProduct(link)
parser_product.start()
