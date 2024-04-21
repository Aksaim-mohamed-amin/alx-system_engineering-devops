# kills a process named killmenow

exec { 'Kill_procces':
  path        => '/usr/bin',
  command     => 'pkill killmenow',
}
