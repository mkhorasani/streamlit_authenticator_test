import yaml
import streamlit as st
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

st.set_page_config(layout='centered')

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Creating the authenticator object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'], 
    config['cookie']['key'], 
    config['cookie']['expiry_days'],
    config['preauthorized']
)

#hashed_passwords = stauth.Hasher(['123']).generate()

col1, col2 = st.columns([1,2])

with col1:
    st.code('''
    Credentials:
    ____________
    Name: John Smith
    Username: jsmith
    Password: 123

    Name: Rebecca Briggs
    Username: rbriggs
    Password: 456
    '''
    )

with col2:
# creating a login widget
    name, authentication_status, username = authenticator.login('Login', 'main')
    if authentication_status:
        authenticator.logout('Logout', 'main')
        st.write(f'Welcome *{name}*')
        st.title('Some content')
    elif authentication_status == False:
        st.error('Username/password is incorrect')
    elif authentication_status == None:
        st.warning('Please enter your username and password')

# # Creating a password reset widget
# if authentication_status:
#     try:
#         if authenticator.reset_password(username, 'Reset password'):
#             st.success('Password modified successfully')
#     except Exception as e:
#         st.error(e)

# # Creating a new user registration widget
# try:
#     if authenticator.register_user('Register user', preauthorization=False):
#         st.success('User registered successfully')
# except Exception as e:
#     st.error(e)

# # Creating a forgot password widget
# try:
#     username_forgot_pw, email_forgot_password, random_password = authenticator.forgot_password('Forgot password')
#     if username_forgot_pw:
#         st.success('New password sent securely')
#         st.write(random_password)
#         # Random password to be transferred to user securely
#     elif username_forgot_pw == False:
#         st.error('Username not found')
# except Exception as e:
#     st.error(e)

# # Creating a forgot username widget
# try:
#     username_forgot_username, email_forgot_username = authenticator.forgot_username('Forgot username')
#     if username_forgot_username:
#         st.success('Username sent securely')
#         st.write(username_forgot_username)
#         # Username to be transferred to user securely
#     elif username_forgot_username == False:
#         st.error('Email not found')
# except Exception as e:
#     st.error(e)

# # Creating an update user details widget
# if authentication_status:
#     try:
#         if authenticator.update_user_details(username, 'Update user details'):
#             st.success('Entries updated successfully')
#     except Exception as e:
#         st.error(e)

# # Saving config file
# with open('config.yaml', 'w') as file:
#     yaml.dump(config, file, default_flow_style=False)
