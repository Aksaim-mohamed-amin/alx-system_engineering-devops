# Install a specific version of flask 2.1.0
package { 'python3':
  ensure => installed,
}

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['python3'],
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3'],
}
