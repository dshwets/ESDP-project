from django.views.generic import DetailView

from hostelguests.models import Guest


class Guest_Detail_View(DetailView):
    model = Guest
    template_name = 'view/guest_detail_view.html'