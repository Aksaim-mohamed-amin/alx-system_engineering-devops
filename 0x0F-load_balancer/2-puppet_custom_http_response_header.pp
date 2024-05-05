# Install Nginx web server and configure it

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is enabled and running
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Define a custom index page
file { '/var/www/html/index.html':
  ensure  => file,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  content => 'Hello World!',
}

# Configure Nginx server
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  content => '
server {
       listen 80 default_server;
       listen [::]:80 default_server;

       root /var/www/html;
       index index.html;

       server_name _;

       location / {
                try_files $uri $uri/ =404;
                add_header X-Served-By $hostname;
       }
}',
  require => Package['nginx'],
  notify  => Service['nginx'],
}
