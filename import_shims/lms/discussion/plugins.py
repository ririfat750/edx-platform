from import_shims.warn import warn_deprecated_import

warn_deprecated_import('discussion.plugins', 'lms.djangoapps.discussion.plugins')

from lms.djangoapps.discussion.plugins import *
