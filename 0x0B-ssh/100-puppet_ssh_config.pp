# make changes to the ssh configuration file
include stdlib

file { '/home/user/.ssh/config':
  ensure => present,
}

file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/home/user/.ssh/config',
  line   => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  ensure => present,
  path   => '/home/user/.ssh/config',
  lin    => 'IdentityFile ~/.ssh/school',
}
