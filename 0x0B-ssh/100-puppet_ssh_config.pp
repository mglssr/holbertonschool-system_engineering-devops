#Client configuration file (w/ Puppet)

exec {'ssh_config':
    path    => '/usr/bin/',
    command => 'echo "IdentityFile ~/.ssh/school\n PasswordAuthentication no" >> /etc/ssh/ssh_config'
}
