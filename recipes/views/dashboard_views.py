from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ..models import RecipeModels



@login_required
def dashboard(request):

    drafts = RecipeModels.objects.filter(
        author=request.user,
        is_published=False
    )

    published = RecipeModels.objects.filter(
        author=request.user,
        is_published=True
    )

    return render(request, 'recipes/page/dashboard.html', {
        'drafts': drafts,
        'published': published
    })