from django.views.generic import ListView
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.db.models import Value, CharField, Q
from blog.models import Post
from store.models import Product
from portfolio.views import PROJECTS
from itertools import chain
from operator import attrgetter
import re
from django.urls import reverse
from .utils import SearchHighlighter, create_search_snippet, highlight_search_title

class SearchResult:
    """Wrapper class to make portfolio results compatible with database results"""
    def __init__(self, project_data, query=''):
        self.title = project_data['title']
        self.slug = project_data['slug']
        self.description = project_data['description']
        self.content = project_data.get('overview', '')
        self.result_type = 'portfolio'
        self.rank = 0.0
        self.query = query
        self.tech_stack_text = self._extract_tech_stack(project_data)
        
        if query:
            highlighter = SearchHighlighter(query)
            self.highlighted_title = highlighter.highlight_title(self.title)
            self.search_snippet = highlighter.highlight_text(self.description + ' ' + self.content, 250)
        else:
            self.highlighted_title = self.title
            self.search_snippet = self.description[:200] + '...'
        
    def _extract_tech_stack(self, project_data):
        tech_stack = project_data.get('tech_stack', {})
        all_tech = []
        for category, tools in tech_stack.items():
            if isinstance(tools, list):
                all_tech.extend(tools)
        return ' '.join(all_tech)
    
    def get_absolute_url(self):
        return reverse('portfolio:project_detail', kwargs={'slug': self.slug})

class SearchView(ListView):
    template_name = 'search/results.html'
    paginate_by = 20
    context_object_name = 'results'
    
    def get_queryset(self):
        query = self.request.GET.get('q', '').strip()
        if not query:
            return []
        
        # Search blog posts here
        blog_results = self.search_posts(query)
        
        # Search products - hurr
        product_results = self.search_products(query)
        
        # Search portfolio projects
        portfolio_results = self.search_portfolio(query)
        
        # Combine results and sort by rank
        combined_results = list(chain(blog_results, product_results, portfolio_results))
        
        # Sort by rank (highest first)
        return sorted(combined_results, key=attrgetter('rank'), reverse=True)
    
    def search_posts(self, query):
        """Search blog posts with highlighting"""
        try:
            # Try PostgreSQL full-text search first
            search_vector = SearchVector('title', weight='A') + SearchVector('content', weight='B')
            search_query = SearchQuery(query)
            
            results = Post.objects.filter(is_published=True).annotate(
                search=search_vector,
                rank=SearchRank(search_vector, search_query),
                result_type=Value('blog', output_field=CharField())
            ).filter(search=search_query)
            
            # Add highlighting to results
            for result in results:
                result.highlighted_title = highlight_search_title(result.title, query)
                result.search_snippet = create_search_snippet(result, query, 'content', 250)
                result.query = query
            
            # If no results, fallback to simple text search
            if not results.exists():
                results = Post.objects.filter(
                    is_published=True
                ).filter(
                    Q(title__icontains=query) | Q(content__icontains=query)
                ).annotate(
                    rank=Value(1.0),
                    result_type=Value('blog', output_field=CharField())
                )
                
                # Add highlighting to fallback results
                for result in results:
                    result.highlighted_title = highlight_search_title(result.title, query)
                    result.search_snippet = create_search_snippet(result, query, 'content', 250)
                    result.query = query
                
            return results
            
        except Exception as e:
            # Fallback to simple search
            results = Post.objects.filter(
                is_published=True,
                title__icontains=query
            ).annotate(
                rank=Value(1.0),
                result_type=Value('blog', output_field=CharField())
            )
            
            # Add highlighting to fallback results
            for result in results:
                result.highlighted_title = highlight_search_title(result.title, query)
                result.search_snippet = create_search_snippet(result, query, 'content', 250)
                result.query = query
                
            return results
    
    def search_products(self, query):
        """Search products with highlighting"""
        try:
            # Try PostgreSQL full-text search first
            search_vector = SearchVector('title', weight='A') + SearchVector('description', weight='B')
            search_query = SearchQuery(query)
            
            results = Product.objects.annotate(
                search=search_vector,
                rank=SearchRank(search_vector, search_query),
                result_type=Value('product', output_field=CharField())
            ).filter(search=search_query)
            
            # Add highlighting to results
            for result in results:
                result.highlighted_title = highlight_search_title(result.title, query)
                result.search_snippet = create_search_snippet(result, query, 'description', 200)
                result.query = query
            
            # If no results, fallback to simple text search
            if not results.exists():
                results = Product.objects.filter(
                    Q(title__icontains=query) | Q(description__icontains=query)
                ).annotate(
                    rank=Value(1.0),
                    result_type=Value('product', output_field=CharField())
                )
                
                # Add highlighting to fallback results
                for result in results:
                    result.highlighted_title = highlight_search_title(result.title, query)
                    result.search_snippet = create_search_snippet(result, query, 'description', 200)
                    result.query = query
                
            return results
            
        except Exception as e:
            # Fallback to simple search
            results = Product.objects.filter(
                title__icontains=query
            ).annotate(
                rank=Value(1.0),
                result_type=Value('product', output_field=CharField())
            )
            
            # Add highlighting to fallback results
            for result in results:
                result.highlighted_title = highlight_search_title(result.title, query)
                result.search_snippet = create_search_snippet(result, query, 'description', 200)
                result.query = query
                
            return results
    
    def search_portfolio(self, query):
        """Search portfolio projects using simple text matching with highlighting"""
        query_lower = query.lower()
        query_words = query_lower.split()
        
        matching_projects = []
        
        for project in PROJECTS:
            score = self._calculate_portfolio_score(project, query_lower, query_words)
            if score > 0:
                result = SearchResult(project, query)  # Pass query for highlighting
                result.rank = score
                matching_projects.append(result)
        
        return matching_projects
    
    def _calculate_portfolio_score(self, project, query_lower, query_words):
        """Calculate relevance score for portfolio project"""
        score = 0.0
        
        # Check title (highest weight)
        title = project.get('title', '').lower()
        if query_lower in title:
            score += 2.0
        for word in query_words:
            if word in title:
                score += 1.0
        
        # Check description (medium weight)
        description = project.get('description', '').lower()
        if query_lower in description:
            score += 1.0
        for word in query_words:
            if word in description:
                score += 0.5
        
        # Check overview (medium weight)
        overview = project.get('overview', '').lower()
        if query_lower in overview:
            score += 1.0
        for word in query_words:
            if word in overview:
                score += 0.3
        
        # Check tech stack (lower weight but important for technical searches)
        tech_stack = project.get('tech_stack', {})
        for category, tools in tech_stack.items():
            if isinstance(tools, list):
                for tool in tools:
                    tool_lower = tool.lower()
                    if query_lower in tool_lower:
                        score += 0.8
                    for word in query_words:
                        if word in tool_lower:
                            score += 0.4
        
        # Check other searchable fields
        searchable_fields = ['problem', 'solution', 'build_notes']
        for field in searchable_fields:
            field_content = project.get(field, '')
            if isinstance(field_content, str):
                field_content = field_content.lower()
                for word in query_words:
                    if word in field_content:
                        score += 0.2
        
        return score
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['total_results'] = len(context['results']) if context['results'] else 0
        
        # Count results by type for display
        if context['results']:
            context['blog_count'] = len([r for r in context['results'] if r.result_type == 'blog'])
            context['product_count'] = len([r for r in context['results'] if r.result_type == 'product']) 
            context['portfolio_count'] = len([r for r in context['results'] if r.result_type == 'portfolio'])
        else:
            context['blog_count'] = 0
            context['product_count'] = 0
            context['portfolio_count'] = 0
            
        return context