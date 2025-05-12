# portfolio/tests/test_views.py
from django.test import TestCase
from django.urls import reverse
from django.http import Http404
from portfolio.views import PROJECTS


class PortfolioViewTest(TestCase):
    def test_portfolio_index_view_renders(self):
        response = self.client.get(reverse("portfolio:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "portfolio/index.html")
        self.assertIn("projects", response.context)
        self.assertEqual(response.context["projects"], PROJECTS)


class ProjectDetailViewTest(TestCase):
    def test_valid_project_detail_view(self):
        project = PROJECTS[0]  # Use the first project in the list
        response = self.client.get(reverse("portfolio:project_detail", args=[project["slug"]]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "portfolio/detail.html")
        self.assertIn("project", response.context)
        self.assertEqual(response.context["project"]["slug"], project["slug"])

    def test_invalid_project_slug_raises_404(self):
        response = self.client.get(reverse("portfolio:project_detail", args=["non-existent"]))
        self.assertEqual(response.status_code, 404)
