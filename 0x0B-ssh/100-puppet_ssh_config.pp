# Ensure the ssh_config file exists
file { '/etc/ssh/ssh_config':
  ensure  => file,
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
}

# Ensure PasswordAuthentication is set to 'no'
file_line { 'Turn off passwd auth':
  ensure             => present,
  path               => '/etc/ssh/ssh_config',
  line               => '    IdentityFile ~/.ssh/school',
  match              => '^[#]+[\s]*(?i)PasswordAuthentication[\s]+(yes|no)$',
  append_on_no_match => true
}

# Ensure IdentityFile is set to the correct key
file_line { 'Declare identity file':
  ensure             => present,
  path               => '/etc/ssh/ssh_config',
  line               => '    IdentityFile ~/.ssh/school',
  match              => '^[#]+[\s]*(?i)IdentityFile[\s]+~/.ssh/id_rsa$',
  append_on_no_match => true
}
