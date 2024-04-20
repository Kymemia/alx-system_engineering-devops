#!/usr/bin/env bash

#configuration file path
$ssh_config_file = '/etc/ssh/ssh_config'

#SSH client uses ~/.ssh/school
file_line { 'Set SSH Identity FIle':
   path   => $ssh_config_file,
   line   => '	IdentityFile ~/.ssh/school',
   match  => '^ *IdentityFile.*$',
   ensure => present,
}

#SSH client configuration refuses pwd configuration
file_line {  'Disable Password Authentication':
    path    => $ssh_config_file,
    line    => '    PasswordAuthentication no',
    match   => '^  *PasswordAuthentication.*$',
    ensure  => present,
}
