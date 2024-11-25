# ©️biisal jai shree krishna 😎
import asyncio
from io import BytesIO
from operator import is_
import os
import tempfile
import base64
import random
from pyrogram import filters
from pyrogram.client import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton 
import httpx
from pyrogram.errors import FloodWait
from info import * 
from .db import *
from .fsub import get_fsub

cl = httpx.AsyncClient(base_url="https://core.avisek.online" , timeout=20) 

@Client.on_message(filters.command("start") & filters.incoming) # type:ignore
async def startcmd(client, message):
    userMention = message.from_user.mention()
    if await users.get_user(message.from_user.id) is None:
        await users.addUser(message.from_user.id, message.from_user.first_name)
        await client.send_message(
            LOG_CHANNEL,
            text=f"#New_user_started\n\nUser: {message.from_user.mention()}\nid :{message.from_user.id}",
        )
    if FSUB and not await get_fsub(client, message):return
    await message.reply_photo(
        photo="https://telegra.ph/file/595e38a4d76848c01b110.jpg",
        caption=f"<b>Jai Shree Krishna {userMention},\n\nIᴍ Hᴇʀᴇ Tᴏ Rᴇᴅᴜᴄᴇ Yᴏᴜʀ Pʀᴏʙʟᴇᴍs..\nYᴏᴜ Cᴀɴ Usᴇ Mᴇ As ʏᴏᴜʀ Pʀɪᴠᴀᴛᴇ Assɪsᴛᴀɴᴛ..\nAsᴋ Mᴇ Aɴʏᴛʜɪɴɢ...Dɪʀᴇᴄᴛʟʏ..\n\nMʏ Cʀᴇᴀᴛᴏʀ : <a href=https://t.me/biisal>Bɪɪsᴀʟ</a>\nMʏ Lᴏᴠᴇʀ : <a href=tg://settings/>Tʜɪs Pᴇʀsᴏɴ</a></b>",
    )
    return


@Client.on_message(filters.command("broadcast") & (filters.private) & filters.user(ADMIN)) # type:ignore
async def broadcasting_func(client, message):
    msg = await message.reply_text("Wait a second!")
    if not message.reply_to_message:
        return await msg.edit("<b>Please reply to a message to broadcast.</b>")
    await msg.edit("Processing ...")
    completed = 0
    failed = 0
    to_copy_msg = message.reply_to_message
    users_list = await users.get_all_users()
    for i , userDoc in enumerate(users_list):
        if i % 20 == 0:
            await msg.edit(f"Total : {i} \nCompleted : {completed} \nFailed : {failed}")
        user_id = userDoc.get("user_id")
        if not user_id:
            continue
        try:
            await to_copy_msg.copy(user_id , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🎭 ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ 🎗️", url='https://t.me/bisal_files_talk')]]))
            completed += 1
        except FloodWait as e:
            if isinstance(e.value , int | float):
                await asyncio.sleep(e.value)
                await to_copy_msg.copy(user_id , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🎭 ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ 🎗️", url='https://t.me/bisal_files_talk')]]))
                completed += 1
        except Exception as e:
            print("Error in broadcasting:", e) 
            failed += 1
            pass
    await msg.edit(f"Successfully Broadcasted\nTotal : {i} \nCompleted : {completed} \nFailed : {failed}")
    



@Client.on_message(filters.command("ai") & filters.chat(CHAT_GROUP)) # type:ignore
async def grp_ai(client: Client, message: Message):
    query : str | None = (
        message.text.split(" ", 1)[1] if len(message.text.split(" ", 1)) > 1 else None
    )
    if not query:
        return await message.reply_text(
            "<b>Abe gadhe /ai k baad kuch likh to le !!.\n\nExample Use:\n<code>/ai Who is lord krshna??</code>\n\nHope you got it.Try it now..</b>"
        )
    if FSUB and not await get_fsub(client, message):return
    message.text = query # type:ignore
    return await ai_res(client, message)


@Client.on_message(filters.command("reset") &  filters.private) # type:ignore
async def reset(client: Client, message: Message):
    try:
        await users.get_or_add_user(message.from_user.id, message.from_user.first_name)
        if FSUB and not await get_fsub(client, message):return
        is_reset = await chat_history.reset_history(message.from_user.id)
        if not is_reset:
            return await message.reply_text("Unable to reset chat history.")
        await message.reply_text("<b>Chat history has been reset.</b>")
    except Exception as e:
        print("Error in reset: ", e)
        return await message.reply_text("Sorry, Failed to reset chat history.")

@Client.on_message(filters.command("gen") & filters.private)  # type:ignore
async def gen_image(client: Client, message: Message):
    sticker = None
    try:
        await users.get_or_add_user(message.from_user.id, message.from_user.first_name)
        if FSUB and not await get_fsub(client, message):return
        sticker = await message.reply_sticker(random.choice(STICKERS_IDS))
        prompt = message.text.replace("/gen", "").strip()
        encoded_prompt = prompt.replace("\n", " ")
        if not prompt:
            return await message.reply_text("Please provide a prompt.")
        response = await cl.get(f"/image/?prompt={encoded_prompt}")
        base64_image = response.json()["image"]
        image_data = base64.b64decode(base64_image)
        image_file = BytesIO(image_data)
        await message.reply_photo(photo=image_file , caption=f"Generated Image for prompt: {prompt[:150]}...")
        image_file.close() 
    except Exception as e:
        print("Error in gen_image: ", e)
        return await message.reply_text("Sorry, I am not Available right now.")
    finally:
        if sticker:await sticker.delete()

@Client.on_message(filters.text & filters.incoming & filters.private) # type:ignore
async def ai_res(client: Client, message: Message ):
    sticker = None
    reply = None
    try:
        await users.get_or_add_user(message.from_user.id, message.from_user.first_name)
        if FSUB and not await get_fsub(client, message):return
        sticker = await message.reply_sticker(random.choice(STICKERS_IDS))
        text = message.text
        if text.startswith('/'):
            return
        user_id = message.from_user.id
        history = await chat_history.get_history(user_id)
        history.append({"role": "user", "content": text})
        response = await cl.post("/ai/", json=history , headers={"Content-Type": "application/json"}) 
        response_json = response.json()
        reply = response_json["response"]
        history.append({"role": "assistant", "content": reply})
        await message.reply_text(reply)
        await chat_history.add_history(user_id, history)
    except Exception as e:
        print("Error in ai_res: ", e)
        reply = "Sorry, I am not available right now."
        await message.reply_text(reply)
    finally:
        if sticker:
            await sticker.delete()