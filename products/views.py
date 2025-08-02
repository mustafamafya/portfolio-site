from django.shortcuts import render,redirect
from userpage.models import Profile
from .models import Product,product_review
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')  # Ensre uthe user is logged in to access the profile
def products(request):
    return render(request, 'products.html', {'pro' : Product.objects.all()})

# Updated view to filter products by category if provided in the request

def products(request): # Updated view to filter products by category
    category = request.GET.get('category')
    if category:
        filtered_products = Product.objects.filter(category=category)
    else:
        filtered_products = Product.objects.all()

    return render(request, 'products.html', {'pro': filtered_products})

def products(request): # Updated view to filter products by category and search term
    category = request.GET.get('category')
    search = request.GET.get('search')
    queryset = Product.objects.all()

    if category:
        queryset = queryset.filter(category=category)
    if search:
        queryset = queryset.filter(name__icontains=search)
    return render(request, 'products.html', {'pro': queryset})



    page_number = request.GET.get('page', 1)
    all_products = Product.objects.all().order_by('id')
    paginator    = Paginator(all_products, 8)       # 8 items per page

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        page_obj = paginator.get_page(page_number)
        html     = render_to_string('partials/product_cards.html',
                                    {'pro': page_obj})
        return JsonResponse({
            'html': html,
            'has_next': page_obj.has_next()
        })

    page_obj = paginator.get_page(page_number)
    return render(request, 'products.html', {'pro': page_obj})


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product, product_review

def product_page(request, pk):
    product = get_object_or_404(Product, id=pk)
    reviews = product_review.objects.filter(product=product)
    review_count = reviews.count()
    avg_rating = product.average_rating()
    gallery_images = product.gallery.all()
    # Handle review submission
    if request.method == 'POST':
        rating = int(request.POST.get('rating'))
        comment = request.POST.get('comment')

        existing_review = product_review.objects.filter(user=request.user, product=product).first()

        if existing_review:
            # Replace old review with new one
            existing_review.rating = rating
            existing_review.comment = comment
            existing_review.save()
            messages.success(request, "Your review was updated.")
        else:
            product_review.objects.create(
                user=request.user,
                product=product,
                rating=rating,
                comment=comment
            )
            messages.success(request, "Review submitted successfully!")

        return redirect('product_page', pk=pk)

    # Check if user already reviewed (for button label)
    existing_review = product_review.objects.filter(user=request.user, product=product).first()

    context = {
        'product': product,
        'reviews': reviews,
        'avg_rating': avg_rating,
        'review_count': review_count,
        'gallery_images': gallery_images,
        'existing_review': existing_review,
        'name_of_reviewer':Profile.full_name,
        'user_pic':Profile.profile_picture,
    }
    return render(request, 'product_page.html', context)

# views.py

