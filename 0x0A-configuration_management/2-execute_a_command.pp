# Using Puppet, create a manifest that kills a process named killmenow
exec { 'pkill -f /tmp/killlmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin/'
}
