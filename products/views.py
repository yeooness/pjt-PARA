from django.shortcuts import render
from .models import Image, Product, Category
from reviews.models import Review
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    # images = Image.objects.order_by("-pk").
    images = Image.objects.all()
    products = Product.objects.all()
    context = {
        "products": products,
        "images": images,
    }
    return render(request, "products/index.html", context)


def detail(request, pk):
    # 특정 글을 가져온다.
    products = Product.objects.get(pk=pk)
    images = Image.objects.filter(product_id=pk)
    reviews = Review.objects.filter(product_id=pk)

    # template에 객체 전달
    context = {
        "products": products,
        "images": images,
        "reviews": reviews,
    }
    return render(request, "products/detail.html", context)


def category(request, category_pk):
    c = Category.objects.get(sort=category_pk)
    products = Product.objects.filter(category_id=c)
    # images = Image.objects.filter()
    img_dict = {}
    for product in products:
        img = Image.objects.filter(product_id=product.id)  # 프로덕트 ID에 해당하는 이미지 객체 다 가져옴
        img_dict[product.id] = img
    print(img_dict)
    # gender = Product.objects.filter(gender=gender)
    # print(images)
    context = {
        "img_dict": img_dict,
        "products": products,
        # "images": images,
        # "gender": gender,
    }
    return render(request, "products/category.html", context)


# def category(request, category_id):
#     categories = Category.objects.all()
#     category = Category.objects.get(pk=category_id)
#     products = Product.objects.filter(category=category).order_by("pub_date")
#     lank_products = Product.objects.filter(category=category).order_by("-hit")[:4]
#     paginator = Paginator(products, 5)
#     page = request.GET.get("page")
#     try:
#         products = paginator.page(page)
#     except PageNotAnInteger:
#         products = paginator.page(1)
#     except EmptyPage:
#         products = paginator.page(paginator.num_pages)
#     print(categories)
#     context = {
#         "lank_products": lank_products,
#         "products": products,
#         "category": category,
#         "categories": categories,
#     }
#     return render(request, "products/category.html", context)
