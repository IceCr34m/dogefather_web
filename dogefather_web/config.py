
choice = 'local'

if choice=='local':
    current_site_url = 'http://127.0.0.1:8000'
    allowed_hosts = []
    protocol = 'http'
elif choice=='h4k333m_test_deploy':
    current_site_url = 'https://dogefather.h4k333m.art'
    allowed_hosts = ['dogefather.h4k333m.art', 'localhost', '127.0.0.1', '[::1]']
    protocol = 'https'

