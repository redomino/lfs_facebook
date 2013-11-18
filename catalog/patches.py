# lfs imports
from lfs.caching.utils import lfs_get_object_or_404
from lfs.catalog.models import Product
from lfs.catalog.views import product_inline

# django imports
from django.http import Http404
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

#lfs_facebook import
from facebook_settings import FACEBOOK_PAGE, FACEBOOK_APP_ID

from lfs.catalog import views

def product_view(request, slug, template_name="lfs/catalog/product_base.html"):
    """Main view to display a product.
    """
    product = lfs_get_object_or_404(Product, slug=slug)
    import pdb; pdb.set_trace()
    if (request.user.is_superuser or product.is_active()) == False:
       raise Http404()

    # Store recent products for later use
    recent = request.session.get("RECENT_PRODUCTS", [])
    if slug in recent:
        recent.remove(slug)
    recent.insert(0, slug)
    if len(recent) > settings.LFS_RECENT_PRODUCTS_LIMIT:
        recent = recent[:settings.LFS_RECENT_PRODUCTS_LIMIT + 1]
    request.session["RECENT_PRODUCTS"] = recent

    result = render_to_response(template_name, RequestContext(request, {
        "product_inline": product_inline(request, product),
        "product": product,
        "facebook_page": FACEBOOK_PAGE,
        "facebook_app_id": FACEBOOK_APP_ID,
    }))
    return result

views.product_view = product_view
