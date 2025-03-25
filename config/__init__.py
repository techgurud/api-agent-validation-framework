"""
Configuration module for API testing framework
"""
import os
from .config import BASE_URL, API_KEY

# Override with local config if available
try:
    from .local_config import API_KEY as LOCAL_API_KEY
    API_KEY = LOCAL_API_KEY
except ImportError:
    # Fall back to environment variable if no local config
    API_KEY = os.getenv('OPENWEATHER_API_KEY', API_KEY)
