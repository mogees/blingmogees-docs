from recommonmark.parser import CommonMarkParser
import sphinx_rtd_theme

# Adding this theme as an extension is what enables localization of theme 
# strings in your translated output. If these strings are not translated 
# in your output, either we lack the localized strings for your locale, 
# or you are using an old version of the theme.
extensions = [
    'sphinx_rtd_theme',
]
html_theme = "sphinx_rtd_theme"

source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']

master_doc = 'index'
project = u'hypersurfaces-calibration-platform'
