# Install Nginx web server and configure it with a custom header                          

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

# Configure Nginx server                                                                  
file_line { 'add the custom header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "                                                                             
  location / {                                                                            
    add_header X-Served-By ${hostname};",
  match  => '^\tlocation / {',
  notify => Service['nginx'],
}
