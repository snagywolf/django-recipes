from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator

from ..models import RecipeModels, Category
from ..forms import RecipeForm



def home(request):

    query = request.GET.get('q', '').strip()
    category_id = request.GET.get('category')

    recipes_list = RecipeModels.objects.filter(is_published=True)

    # 🔥 filtro por categoria
    if category_id:
        recipes_list = recipes_list.filter(categories__id=category_id)

    # 🔍 busca
    if query:
        recipes_list = recipes_list.filter(title__icontains=query)

    paginator = Paginator(recipes_list, 6)
    page_number = request.GET.get('page')
    recipes = paginator.get_page(page_number)

    categories = Category.objects.all()

    return render(request, 'recipes/page/home.html', {
        'recipes': recipes,
        'categories': categories,
        'query': query,
        'category_id': category_id
    })
def recipe_view(request, slug):

    recipe = get_object_or_404(RecipeModels, slug=slug)
    if not recipe.is_published and recipe.author != request.user:
        return redirect('home')
    return render(request,'recipes/page/recipe.html',{'recipe':recipe})
@login_required
def create_recipe(request):

    if request.method == 'POST':

        form = RecipeForm(request.POST, request.FILES)

        if form.is_valid():

            recipe = form.save(commit=False)

            recipe.author = request.user
            recipe.is_published = False

            recipe.save()

            return redirect('dashboard')

    else:
        form = RecipeForm()

    return render(request, 'recipes/page/form.html', {'form': form})
@login_required
def update_recipe(request, id):

    recipe = get_object_or_404(
        RecipeModels,
        id=id,
        author=request.user
    )

    if request.method == 'POST':

        form = RecipeForm(
            request.POST,
            request.FILES,
            instance=recipe
        )

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = RecipeForm(instance=recipe)

    return render(
        request,
        'recipes/page/form.html',
        {
            'form': form
        }
    )
@login_required
@require_POST
def delete_recipe(request, id):

    recipe = get_object_or_404(
        RecipeModels,
        id=id,
        author=request.user
    )

    if request.method == 'POST':
        recipe.delete()
        return redirect('dashboard')

    return redirect('dashboard')
