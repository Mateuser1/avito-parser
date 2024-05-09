from parser import Parser
from product_parser import ParserProduct


link = "https://www.avito.ru/sankt-peterburg/telefony/iphone_xr_64_gb_3874641763"
# parser = Parser(link)
parser_product = ParserProduct(link)
parser_product.start()
