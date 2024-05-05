# Configure Nginx server.

# Update package lists
exec { 'apt_update':
  command => 'apt-get update',
}

# Install Nginx
package { 'nginx':
  ensure => installed,
  require => Exec['apt_update'],
}

# Allow connections to Nginx over the firewall
ufw::allow { 'Nginx HTTP':
  port => '80',
}

# Create the index.html file
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

# Create a custom 404 error page
file { '/var/www/html/404.html':
  ensure  => file,
  content => "Ceci n'est pas une page",
}

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Restart Nginx server
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
  subscribe => File['/etc/nginx/sites-available/default'],
}
