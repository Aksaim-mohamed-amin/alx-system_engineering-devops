# Set up the cinfuguration file for ssh client
file { '~/.ssh/config':
  ensure => file,
  content => '
Host *
     PasswordAuthentication no
     IdentityFile ~/.ssh/school
',
}
