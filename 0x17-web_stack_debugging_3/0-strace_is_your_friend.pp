# This script fixes a 500 error and automates it

exec { 'fix_err':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => ['/bin/', '/usr/bin'],
  onlyif  => 'grep -q "phpp" /var/www/html/wp-settings.php',
}
