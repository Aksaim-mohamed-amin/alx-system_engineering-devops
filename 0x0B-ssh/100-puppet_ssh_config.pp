# make changes to the ssh configuration file
include stdlib

file { '~/.ssh/config':
  ensure => present,
}

file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '~/.ssh/config',
  line   => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  ensure => present,
  path   => '~/.ssh/config',
  line   => 'IdentityFile ~/.ssh/school',
}
