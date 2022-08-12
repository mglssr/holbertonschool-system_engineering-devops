exec { 'pkill -f /tmp/killlmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin/'
}
