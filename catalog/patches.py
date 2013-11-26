# django imports
from django.conf import settings
from django.template import RequestContext
from django.template.loader import render_to_string
from django.core.cache import cache

#lfs_facebook import
from lfs_facebook.decorators import permissions_required 

# lfs imports
from lfs.catalog.settings import SELECT
from lfs.catalog import views
from lfs.catalog.views import calculate_packing
from lfs.catalog.models import ProductPropertyValue
from lfs.catalog.settings import PROPERTY_VALUE_TYPE_DEFAULT
from lfs.core import views as core_views

@permissions_required('product')
def product_inline(request, product, template_name="lfs/catalog/products/product_inline.html"):
    """
    Part of the product view, which displays the actual data of the product.

    This is factored out to be able to better cached and in might in future used
    used to be updated via ajax requests.
    """
    cache_key = "%s-product-inline-%s-%s" % (settings.CACHE_MIDDLEWARE_KEY_PREFIX, request.user.is_superuser, product.id)
    result = cache.get(cache_key)
    if result is not None:
        return result

    # Switching to default variant
    if product.is_product_with_variants():
        temp = product.get_default_variant()
        product = temp if temp else product

    properties = []
    variants = []

    display_variants_list = True
    if product.is_variant():
        parent = product.parent
        if parent.variants_display_type == SELECT:
            display_variants_list = False
            # Get all properties (sorted). We need to traverse through all
            # property/options to select the options of the current variant.
            for property in parent.get_property_select_fields():
                options = []
                for property_option in property.options.all():
                    if product.has_option(property, property_option):
                        selected = True
                    else:
                        selected = False
                    options.append({
                        "id": property_option.id,
                        "name": property_option.name,
                        "selected": selected,
                    })
                properties.append({
                    "id": property.id,
                    "name": property.name,
                    "title": property.title,
                    "unit": property.unit,
                    "options": options,
                })
        else:
            properties = parent.get_property_select_fields()
            variants = parent.get_variants()

    elif product.is_configurable_product():
        for property in product.get_configurable_properties():
            options = []
            try:
                ppv = ProductPropertyValue.objects.get(product=product, property=property, type=PROPERTY_VALUE_TYPE_DEFAULT)
                ppv_value = ppv.value
            except ProductPropertyValue.DoesNotExist:
                ppv = None
                ppv_value = ""

            for property_option in property.options.all():
                if ppv_value == str(property_option.id):
                    selected = True
                else:
                    selected = False

                options.append({
                    "id": property_option.id,
                    "name": property_option.name,
                    "price": property_option.price,
                    "selected": selected,
                })
            properties.append({
                "obj": property,
                "id": property.id,
                "name": property.name,
                "title": property.title,
                "unit": property.unit,
                "display_price": property.display_price,
                "options": options,
                "value": ppv_value,
            })

    if product.get_template_name() != None:
        template_name = product.get_template_name()

    if product.get_active_packing_unit():
        packing_result = calculate_packing(request, product.id, 1, True, True)
    else:
        packing_result = ""
    # lfs utility 
    fb_reserved = "False"
    for p in product.get_properties():
        if p.title == settings.FACEBOOK_FAN_RESERVED_PROPERTY:
            fb_reserved = "True"
    # attachments
    attachments = product.get_attachments()
    result = render_to_string(template_name, RequestContext(request, {
        "product": product,
        "variants": variants,
        "product_accessories": product.get_accessories(),
        "properties": properties,
        "packing_result": packing_result,
        "attachments": attachments,
        "quantity": product.get_clean_quantity(1),
        "price_includes_tax": product.price_includes_tax(request),
        "price_unit": product.get_price_unit(),
        "unit": product.get_unit(),
        "display_variants_list": display_variants_list,
        "for_sale": product.get_for_sale(),
        #lfs_facebook variables
        "facebook_app_id": settings.FACEBOOK_APP_ID,
        "facebook_page": settings.FACEBOOK_PAGE,
        "fb_reserved": fb_reserved,
    }))
    cache.set(cache_key, result)
    return result

views.product_inline = product_inline

original_product = views.product_view

@permissions_required('product')
def protected_product(request, slug, template_name="lfs/catalog/product_base.html"):
    return original_product(request, slug, template_name="lfs/catalog/product_base.html")

views.product_view  = protected_product

original_add_to_cart = views.add_to_cart

@permissions_required('add-to-cart')
def protected_add_to_cart(request, product_id=None):
    return original_add_to_cart(request, product_id=None)

views.add_to_cart = protected_add_to_cart

original_category_view = views.category_view

@permissions_required('category')
def protected_category_view(request, slug, template_name="lfs/catalog/category_base.html"):
    return original_category_view(request, slug, template_name="lfs/catalog/category_base.html")

views.category_view = protected_category_view

original_shop_view = core_views.shop_view

@permissions_required('shop')
def protected_shop_view(request, template_name="lfs/shop/shop.html"):
    return original_shop_view(request, template_name="lfs/shop/shop.html")

core_views.shop_view = protected_shop_view
