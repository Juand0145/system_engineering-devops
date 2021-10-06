# fixing removing hard and soft file limits
exec { 'del hard lim':
  command => "sed -i '/holberton hard nofile 5/d' /etc/security/limits.conf",
  path    => '/bin/',
}

exec { 'del soft lim':
  command => "sed -i '/holberton soft nofile 4/d' /etc/security/limits.conf",
  path    => '/bin/',
}
