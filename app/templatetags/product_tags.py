from django import template

register=template.Library()
@register.simple_tag
def cal(Product_Price,Product_Discount):
    if Product_Discount is None or Product_Discount is 0:
        return Product_Price
    cal=Product_Price
    cal=Product_Price-(Product_Price*Product_Discount/100)
    return cal
@register.simple_tag
def progress_bar(Product_Availability,Product_Quantity):
    progress_bar=Product_Availability*(100/Product_Quantity)
    return progress_bar