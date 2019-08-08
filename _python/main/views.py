from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import redirect_to_login
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ContentAnnotationSerializer
from .models import Casebook, Resource


def login_required_response(request):
    if request.user.is_authenticated:
        return HttpResponseForbidden()
    else:
        return redirect_to_login(request.build_absolute_uri())

@login_required
@api_view(['GET'])
def annotations(request, resource_id, format=None):
    """
        /resources/:resource_id/annotations view.
        Was: app/controllers/content/annotations_controller.rb
    """
    resource = get_object_or_404(Resource.objects.select_related('casebook'), pk=resource_id)

    # check permissions
    if not resource.casebook.viewable_by(request.user):
        return login_required_response(request)

    if request.method == 'GET':
        return Response(ContentAnnotationSerializer(resource.annotations.all(), many=True).data)

def index(request):
    return render(request, 'index.html')

def casebook(request, casebook_id):
    casebook = get_object_or_404(Casebook, id=casebook_id)

    # check permissions
    if not casebook.viewable_by(request.user):
        return login_required_response(request)

    contents = casebook.contents.all().order_by('ordinals')

    # TODO: find out about the resources that appear in this TOC, but not on prod.
    return render(request, 'casebook.html', {
        'casebook': casebook,
        'contents': contents
    })

