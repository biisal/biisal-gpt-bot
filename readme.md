# ChatGPT Telegram Bot

Welcome to the **ChatGPT Bot** repository! This bot allows users to chat with an AI directly in Telegram. Whether you're in a private chat or a group, the bot provides seamless interactions powered by the latest AI models.


Best thing is you don't need any API key to create this bot.

## Features

- **Private Chat**: Users can chat with the bot directly without using any commands. The bot stores up to the last 50 messages in the conversation, allowing for continuous, context-aware responses.
  
- **Fast Responses**: The bot is optimized for speed, offering the most efficient and fast replies.

- **Fully Asynchronous**: No blocking or delays. Everything runs smoothly and asynchronously for a fluid experience.

- **Image Generation**: Using the `/gen` command, users can generate high-quality images with AI.

- **Group Chat Support**: In group chats, you can interact with the bot using the `/ai` command.

- **Reset Chat History**: Users can reset their chat history using the `/reset` command.

- **Database Integration**: All chats and user details are stored in a database for easy management and reference.

- **Broadcast Command**: Admins can use the broadcast command to send messages to all users at once.

## AI Model Credits

- **Mistral**
- **Llama**
- **Stable Diffusion**

These powerful AI models provide high-quality responses and image generation capabilities.

## Dependencies

This bot uses **Pyrogram** library for Telegram interactions,**Motor** for async database operations and
runs on **Python 3.12+** for optimal performance.

### Installation

To set up the bot on your local machine, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/biisal/chatgpt-bot.git
   cd chatgpt-bot
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with your bot token and other configuration details:

   ```bash
    API_ID=your-telegram-api-id
    API_HASH=your-telegram-api-hash
    BOT_TOKEN=your-telegram-bot-token
    ADMIN=your-telegram-user-id
    CHAT_GROUP=your-telegram-group-id
    LOG_CHANNEL=your-telegram-channel-id-for-logs
    MONGO_URL=your-mongodb-connection-string
   ```

4. Run the bot:

   ```bash
   python bot.py
   ```
   - For mac or linux users use ->
   `python3 bot.py`

### Deploying this bot Repository in Koyeb or Render - 
#### Deploying this bot in Render is Almost same as deploying it in Koyeb. You Just need to Follow the Steps.

- Fork the repo and import it in Koyeb or Render by choosing web services.
- Choose python if any server asks for it.
- For Koyeb, in the builder section, choose the buildpack option.
- For Render, use this as build command: `pip install -r requirements.txt`
- For Koyeb, you don't need to add any build command.
- For run or start command, use this command: `gunicorn app:app & python3 bot.py`
- Add all env variables in environment variables section.


### Commands

- `/gen [prompt]`: Generate high-quality images using AI.
- `/ai [text]`: Use this command in group chats to interact with the bot.
- `/broadcast`: Admins can broadcast a message to all users.
- `/reset`: Reset the chat history.

## Contribution

Feel free to fork the repository and contribute by creating pull requests. If you find any issues or have suggestions for improvements, please open an issue.

## License

This project is licensed under the MIT License.

---

Enjoy chatting with the AI!