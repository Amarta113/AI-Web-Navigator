css = '''
<style>
.chat-message {
    padding: 1.5rem;
    border-radius: 0.5rem; 
    margin-bottom: 1rem; 
    display: flex;
    background_color: red;
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

# set your bot avatar by setting the url of the image in src
bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="bot-image-url">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

# set your user avatar by setting the url of the image in src
user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="user-image-url">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
