from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import DetailView
from django.core.paginator import Paginator
from hostelguests.models import Guest


class GuestDetailView(PermissionRequiredMixin, DetailView):
    model = Guest
    template_name = 'guestdetail.html'
    permission_required = 'hostelguests.can_view_guest'
    paginate_comments_by = 2
    paginate_notes_orphans = 0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        notes, page, is_paginated = self.paginate_notes(self.object)
        context['notes'] = notes
        context['page_obj'] = page
        context['is_paginated'] = is_paginated
        return context

    def paginate_notes(self, guest):
        notes = guest.notes.all()
        if notes.count() > 0:
            paginator = Paginator(notes, self.paginate_comments_by, orphans=self.paginate_notes_orphans)
            page_number = self.request.GET.get('page', 1)
            page = paginator.get_page(page_number)
            is_paginated = paginator.num_pages > 1  # page.has_other_pages()
            return page.object_list, page, is_paginated
        else:
            return notes, None, False
