# Third-party Imports
from flask import render_template, Blueprint

# Local Application Imports
from source import cache

# Initialize the Blueprint for home-related routes
bp = Blueprint('main_routes', __name__)


@bp.route('/')
@cache.cached(timeout=3600)
def home():
    """
    Render the home (landing) page.

    Returns:
        Rendered HTML for 'home.html'.
    """
    return render_template('home.html')


@bp.route('/coming_soon')
@cache.cached(timeout=3600)
def coming_soon():
    """
    Render the 'Coming Soon' placeholder page.

    Returns:
        Rendered HTML for 'coming_soon.html'.
    """
    return render_template('coming_soon.html')


@bp.route('/contact')
@cache.cached(timeout=3600)
def contact():
    """
    Render the contact page.

    Returns:
        Rendered HTML for 'contact.html'.
    """
    return render_template('contact.html')


@bp.route('/downloads')
@cache.cached(timeout=3600)
def downloads():
    """
    Render the contact page.

    Returns:
        Rendered HTML for 'contact.html'.
    """
    return render_template('downloads.html')

