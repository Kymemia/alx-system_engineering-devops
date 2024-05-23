# install and configure Nginx

package { 'nginx':
   ensure => 'installed',
}

# define index.html's content
file { '/var/www/html/index.html':
   ensure => file,
   content => 'Hello World!',
   require => Package['nginx'],
}

# configure nginx
file {'/etc/nginx/sites-available/default':
   ensure => file,
   content => template('nginx/default.erb'),
   require => Package['nginx'],
   notify => Service['nginx'],
}

# ensure nginx is running and is enabled
service { 'nginx':
   ensure => 'running',
   enable => true,
   require => Package['nginx'],
}
