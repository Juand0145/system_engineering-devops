# solve the problem to open mqax file
exec { '/etc/default/nginx':
  command => "sed -i 's/15/4000/g' /etc/default/nginx",
  path    => '/bin/',
}

service { 'nginx':
  ensure    => running,
  subscribe => Exec['/etc/default/nginx'],
}
