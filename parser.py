from parsel import Selector
import json
from utils import xpath_file

XPATH_file="xpaths.json"
XPATHS=xpath_file(XPATH_file)

#parser
def parser(text):
    product = text[XPATHS["product"]]
    sel = Selector(json.dumps(product), type="json")
    name = sel.jmespath('productDetail.productCopies[0].description').get()
    product_id=sel.jmespath('productDetail.number').get()
    prodUrl=sel.jmespath('pageMetaOverride.openGraphTags[2].content').get()
    brand=sel.jmespath('productDetail.brandName').get()
    variants=[] #variants list
    info = {}
    for sku in sel.jmespath('productDetail.skus'):
        info['size_code']=sku.jmespath('sizeCode').get()
        info['colorCode']=sku.jmespath('colorCode').get()
        info["sale_price"]=sku.jmespath('price.currentPrice').get()
        info["original_price"]=sku.jmespath('price.originalPrice').get()
        info["size"]=sku.jmespath('size.values[0].label').get()
        info["size_label"] = sku.jmespath('size.values[0].longLabel').get()
        info["size_range"] = sku.jmespath('attributesTypes[0].values[0].label').get()
        info["fit"] = sku.jmespath('attributesTypes[1].values[0].label').get()
        info["color"]=sku.jmespath('color.values[0].label').get()
        variants.append(info)

    result = [{
        "prodUrl":prodUrl,
        "product_name": name,
        "brand":brand,
        "product_id":product_id,
        "variants":variants
    }]

    return result