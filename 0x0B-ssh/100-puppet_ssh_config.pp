# Configure the ssh client

include stdlib

file_line { 'Turn off password authontication':
  ensure => present,
  path   => '/root/.ssh/config',
  line   => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  ensure => present,
  path   => '/root/.ssh/config',
  line   => 'IdentityFile ~/.ssh/school',
}
