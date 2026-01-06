import os
from pathlib import Path
from dotenv import load_dotenv

import sys
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

if os.path.exists(BASE_DIR.parent / '.env'):
    load_dotenv(BASE_DIR.parent / '.env')

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')
if not ALLOWED_HOSTS or ALLOWED_HOSTS == ['']:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third apps
    'accounts',
    'withMe',
    'findMe',
    'community',
    'chatBot',
    'mypage',
    'manager',
    'etc'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# 환경변수 디버깅
print("\n" + "=" * 80)
print("DATABASE CONFIGURATION DEBUG")
print("=" * 80)

# 모든 환경변수 확인
import sys
print(f"Python version: {sys.version}")

# DATABASE_URL 확인
DATABASE_URL = os.getenv('DATABASE_URL')
print(f"\n1. DATABASE_URL exists: {DATABASE_URL is not None}")

if DATABASE_URL:
    print(f"2. DATABASE_URL length: {len(DATABASE_URL)}")
    print(f"3. DATABASE_URL first 70 chars: {DATABASE_URL[:70]}...")
    print(f"4. Starts with 'postgresql://': {DATABASE_URL.startswith('postgresql://')}")
    print(f"5. Contains 'railway': {'railway' in DATABASE_URL}")
else:
    print("2. ❌ DATABASE_URL is COMPLETELY MISSING!")
    print("\n3. Checking individual DB variables:")
    print(f"   DB_HOST: {os.getenv('DB_HOST', 'NOT SET')}")
    print(f"   DB_NAME: {os.getenv('DB_NAME', 'NOT SET')}")
    print(f"   DB_USER: {os.getenv('DB_USER', 'NOT SET')}")
    print(f"   DB_PORT: {os.getenv('DB_PORT', 'NOT SET')}")
    
print("\n4. All environment variables starting with 'DB' or 'DATABASE':")
for key, value in os.environ.items():
    if key.startswith('DB') or key.startswith('DATABASE'):
        if 'PASSWORD' in key or 'PASS' in key:
            print(f"   {key}: ***hidden***")
        else:
            print(f"   {key}: {value[:50] if len(value) > 50 else value}...")

print("=" * 80 + "\n")


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('DB_NAME'),
#         'USER': os.getenv('DB_USER'),
#         'PASSWORD': os.getenv('DB_PASSWORD'),
#         'HOST': os.getenv('DB_HOST'),
#         'PORT': os.getenv('DB_PORT'),
#     }
# }

# 데이터베이스 설정
if DATABASE_URL:
    print("✅ Configuring database with DATABASE_URL\n")
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600)
    }
    print(f"Parsed database config:")
    print(f"  ENGINE: {DATABASES['default']['ENGINE']}")
    print(f"  NAME: {DATABASES['default']['NAME']}")
    print(f"  HOST: {DATABASES['default']['HOST']}")
    print(f"  PORT: {DATABASES['default']['PORT']}")
else:
    print("❌ WARNING: Using fallback local database config - THIS WILL FAIL ON RAILWAY!\n")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME', ''),
            'USER': os.getenv('DB_USER', ''),
            'PASSWORD': os.getenv('DB_PASSWORD', ''),
            'HOST': os.getenv('DB_HOST', 'localhost'),
            'PORT': os.getenv('DB_PORT', '5432'),
        }
    }
    print(f"Fallback database config:")
    print(f"  HOST: {DATABASES['default']['HOST']}")
    print(f"  NAME: {DATABASES['default']['NAME']}")

print("=" * 80 + "\n")


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
