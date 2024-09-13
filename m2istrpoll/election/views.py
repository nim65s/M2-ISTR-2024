from django.views.generic import DetailView, ListView, RedirectView
from django.views.generic.detail import SingleObjectMixin

from . import models


class ElectionListView(ListView):
    model = models.Election


class ElectionDetailView(DetailView):
    model = models.Election


class VoteView(SingleObjectMixin, RedirectView):
    model = models.Candidate

    def get_redirect_url(self, *args, **kwargs):
        candidate = self.get_object()
        candidate.score += 1
        candidate.save()
        return f"/election/{candidate.election.id}"
