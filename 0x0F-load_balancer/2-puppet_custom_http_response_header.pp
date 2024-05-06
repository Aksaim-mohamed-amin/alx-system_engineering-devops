# Install Nginx web server and configure it with a custom header

# Install Nginx package
package { 'nginx':
  ensure => present,
}

# Configure Nginx server with custom header
file_line { 'header line':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "    location / {
    add_header X-Served-By ${hostname};
  ",
  match  => '^\s*location / {',
  require => Package['nginx'],
  notify => Service['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure     => running,
  enable     => true,
  require    => Package['nginx'],
}
