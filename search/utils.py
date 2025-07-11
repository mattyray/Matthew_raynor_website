import re
from django.utils.html import format_html
from django.utils.safestring import mark_safe

class SearchHighlighter:
    """Utility class for highlighting search terms in text"""
    
    def __init__(self, query):
        self.query = query.strip()
        self.query_words = [word.strip() for word in self.query.split() if len(word.strip()) > 2]
    
    def highlight_text(self, text, max_length=300):
        """Highlight search terms in text and return a snippet"""
        if not text or not self.query_words:
            return text[:max_length] + ("..." if len(text) > max_length else "")
        
        # Convert to string and clean
        text = str(text)
        
        # Find the best snippet location (around first match)
        snippet_start = self._find_best_snippet_start(text, max_length)
        
        # Extract snippet
        snippet = text[snippet_start:snippet_start + max_length]
        
        # Add ellipsis if needed
        if snippet_start > 0:
            snippet = "..." + snippet
        if snippet_start + max_length < len(text):
            snippet = snippet + "..."
        
        # Highlight terms
        highlighted = self._highlight_terms(snippet)
        
        return mark_safe(highlighted)
    
    def highlight_title(self, title):
        """Highlight search terms in title (no truncation)"""
        if not title or not self.query_words:
            return title
        
        return mark_safe(self._highlight_terms(str(title)))
    
    def _find_best_snippet_start(self, text, max_length):
        """Find the best place to start the snippet (around first match)"""
        text_lower = text.lower()
        
        # Look for the first occurrence of any search word
        earliest_pos = len(text)
        
        for word in self.query_words:
            word_lower = word.lower()
            pos = text_lower.find(word_lower)
            if pos != -1 and pos < earliest_pos:
                earliest_pos = pos
        
        if earliest_pos == len(text):
            return 0  # No matches found, start from beginning
        
        # Try to center the snippet around the match
        snippet_start = max(0, earliest_pos - max_length // 3)
        
        # Try to start at a word boundary
        if snippet_start > 0:
            word_boundary = text.find(' ', snippet_start)
            if word_boundary != -1 and word_boundary - snippet_start < 50:
                snippet_start = word_boundary + 1
        
        return snippet_start
    
    def _highlight_terms(self, text):
        """Apply HTML highlighting to search terms"""
        if not self.query_words:
            return text
        
        highlighted_text = text
        
        # Sort words by length (longest first) to avoid partial replacements
        sorted_words = sorted(self.query_words, key=len, reverse=True)
        
        for word in sorted_words:
            # Use word boundaries to avoid partial matches
            pattern = r'\b' + re.escape(word) + r'\b'
            replacement = f'<mark class="search-highlight">{word}</mark>'
            highlighted_text = re.sub(pattern, replacement, highlighted_text, flags=re.IGNORECASE)
        
        return highlighted_text

def create_search_snippet(obj, query, content_field='content', max_length=200):
    """Create a highlighted snippet from an object's content"""
    highlighter = SearchHighlighter(query)
    
    if hasattr(obj, content_field):
        content = getattr(obj, content_field, '')
        return highlighter.highlight_text(content, max_length)
    
    return ''

def highlight_search_title(title, query):
    """Highlight search terms in a title"""
    highlighter = SearchHighlighter(query)
    return highlighter.highlight_title(title)