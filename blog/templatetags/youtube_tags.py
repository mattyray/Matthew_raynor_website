import re
from django import template

register = template.Library()


@register.filter
def youtube_id(url):
    """
    Extract YouTube video ID from various URL formats:
    - https://www.youtube.com/watch?v=VIDEO_ID
    - https://youtu.be/VIDEO_ID
    - https://www.youtube.com/embed/VIDEO_ID
    """
    if not url:
        return ""
    
    patterns = [
        r'(?:youtube\.com\/watch\?v=)([\w-]+)',
        r'(?:youtu\.be\/)([\w-]+)',
        r'(?:youtube\.com\/embed\/)([\w-]+)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, str(url))
        if match:
            return match.group(1)
    
    return ""


@register.filter
def youtube_thumbnail(url):
    """
    Get YouTube thumbnail URL from video URL.
    """
    video_id = youtube_id(url)
    if video_id:
        return f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
    return ""


@register.filter
def cloudinary_transform(url, transforms):
    """
    Insert Cloudinary transforms into a Cloudinary URL path.
    Usage: {{ post.image.url|cloudinary_transform:"w_400,h_225,c_fill,q_auto,f_auto" }}
    """
    if not url:
        return ""
    url = str(url)
    marker = "/upload/"
    if marker in url:
        idx = url.index(marker) + len(marker)
        return url[:idx] + transforms + "/" + url[idx:]
    return url