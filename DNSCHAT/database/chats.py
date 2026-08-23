from DNSCHAT import db

chatsdb = db.chatsdb

async def get_served_chats() -> list:
    """
    Saare served group chats ki list return karega
    Sirf chat_id < 0 wale yani group/supergroup
    """
    chats_list = []
    async for chat in chatsdb.find({"chat_id": {"$lt": 0}}):
        chats_list.append(chat)
    return chats_list

async def is_served_chat(chat_id: int) -> bool:
    """
    Check karega ki chat DB me hai ya nahi
    """
    chat = await chatsdb.find_one({"chat_id": chat_id})
    return chat is not None

async def add_served_chat(chat_id: int):
    """
    Naya group add hone par DB me add karega
    Duplicate nahi banega
    """
    is_served = await is_served_chat(chat_id)
    if is_served:
        return
    return await chatsdb.insert_one({"chat_id": chat_id})

async def remove_served_chat(chat_id: int):
    """
    Bot kick/leave hone par DB se hata dega
    """
    is_served = await is_served_chat(chat_id)
    if not is_served:
        return
    return await chatsdb.delete_one({"chat_id": chat_id})
