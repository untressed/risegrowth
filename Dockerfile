FROM php:8.3-apache

# Enable rewrite module for permalinks & REST API
RUN a2enmod rewrite

# Install SQLite dependencies
RUN apt-get update && apt-get install -y libsqlite3-dev \
    && docker-php-ext-install pdo_sqlite \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /var/www/html

# Copy WordPress installation
COPY wordpress/ .

# Set permissions for SQLite database and uploads
RUN chown -R www-data:www-data /var/www/html \
    && chmod -R 775 /var/www/html/wp-content

EXPOSE 80
