# install flask from pip3

package {'python3':
  ensure => installed,
}

package {'werkzeug':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3']
}
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['werkzeug'],
}
