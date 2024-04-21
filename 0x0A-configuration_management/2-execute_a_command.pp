# kills a process named killmenow

exec { 'Kill_procces':
  command     => 'pkill killmenow',
  refreshonly => true,
}
