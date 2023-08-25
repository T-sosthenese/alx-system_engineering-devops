# Create a manifest that kills a process called killmenow
exec { 'pkill -f killmenow':
  provider => 'shell',
}
