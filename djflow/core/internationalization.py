from .json_settings import get_settings

settings = get_settings()

LANGUAGE_CODE = settings['LANGUAGE_CODE']
TIME_ZONE = settings['TIME_ZONE']
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Configuración de formatos de fechas

DATETIME_INPUT_FORMATS = (
    '%Y-%m-%d %H:%M:%S',     # '2006-10-25 14:30:59'
    '%Y-%m-%d %H:%M:%S.%f',  # '2006-10-25 14:30:59.000200'
    '%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
    '%Y-%m-%d',              # '2006-10-25'
    '%d-%m-%Y %H:%M:%S',     # '2006-10-25 14:30:59'
    '%d-%m-%Y %H:%M:%S.%f',  # '2006-10-25 14:30:59.000200'
    '%d-%m-%Y %H:%M',        # '2006-10-25 14:30'
    '%Y-%m-%d',              # '2006-10-25'
    '%m/%d/%Y %H:%M:%S',     # '10/25/2006 14:30:59'
    '%m/%d/%Y %H:%M:%S.%f',  # '10/25/2006 14:30:59.000200'
    '%m/%d/%Y %H:%M',        # '10/25/2006 14:30'
    '%m/%d/%Y',              # '10/25/2006'
    '%m/%d/%y %H:%M:%S',     # '10/25/06 14:30:59'
    '%m/%d/%y %H:%M:%S.%f',  # '10/25/06 14:30:59.000200'
    '%m/%d/%y %H:%M',        # '10/25/06 14:30'
    '%m/%d/%y',              # '10/25/06'
    '%m/%d/%Y',              # '10/25/2006'
    '%d/%m/%Y',              # '10/25/2006'
    '%d/%m/%y',              # '10/25/06'
)

DATE_INPUT_FORMATS = (
    '%d/%m/%Y',                         # '10/25/2006'
    '%d/%m/%y',                         # '10/25/06'
    '%d-%m-%Y',                         # '10-25-2006'
    '%d-%m-%y',                         # '10-25-06'
)