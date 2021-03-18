DirectoryIndex install.php index.html index.php

RewriteEngine On
RewriteRule ^install-mod-rewrite-test$ install.php?mod_rewrite_test=true [QSA,L]
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-l
RewriteRule ^([0-9a-zA-Z-_/.]+)$ index.php?route=$1 [QSA,L]

#Gzip
<ifmodule mod_deflate.c>
AddOutputFilterByType DEFLATE text/text text/html text/plain text/xml text/css application/x-javascript application/javascript
</ifmodule>
#End Gzip

<IfModule mod_expires.c>
ExpiresActive On
ExpiresByType image/gif "access plus 1 weeks"
ExpiresByType image/svg "access plus 1 weeks"
ExpiresByType image/jpg "access plus 1 weeks"
ExpiresByType image/jpeg "access plus 1 weeks"
ExpiresByType image/png "access plus 1 weeks"
ExpiresByType image/bmp "access plus 1 weeks"
ExpiresByType text/css "access plus 1 weeks"
ExpiresByType application/javascript "access plus 1 weeks"
ExpiresByType application/x-javascript "access plus 1 weeks"
ExpiresByType text/javascript "access plus 1 weeks"
</IfModule>

<IfModule mod_headers.c>
Header set Connection keep-alive
</IfModule>