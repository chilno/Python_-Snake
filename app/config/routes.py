
from system.core.router import routes

routes['default_controller'] = 'Users'
routes['/register'] = 'Users#register'
routes['POST']['/create'] = 'Users#create'
routes['/user/show/<id>'] = 'Users#show'
routes['POST']['/login'] = 'Users#login'
routes['/dashboard'] = 'Users#dashboard'
routes['/clear'] = 'Users#clear'
routes['POST']['/post/<id>'] = 'Users#post'
routes['POST']['/comment/<id>/<msg_id>'] = 'Users#comment'
routes['/edit/<id>'] = 'Users#edit'
routes['POST']['/update_info/<id>'] = 'Users#update_info'
routes['POST']['/update_password/<id>'] = 'Users#update_password'
routes['POST']['/update_description/<id>'] = 'Users#update_description'
routes['POST']['/delete/<id>'] = 'Users#delete'
routes['POST']['/add_user'] = 'Users#add_user'
routes['POST']['/locate'] ='Users#locate'
routes['/show_map'] = 'Users#show_map'
routes['POST']['/marker'] ='Users#marker'

