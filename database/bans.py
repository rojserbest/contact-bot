from database import db

bans = db["bans"]

f_ = bans.find()
f_ = [ban_["user_id"] for ban_ in f_] if f_ else []
cache = [f_]


def is_banned(user_id) -> bool:
    return int(user_id) in cache[0]


def ban(user_id) -> None:
    user_id = int(user_id)

    bans.update_one(
        {
            "user_id": user_id,
        },
        {
            "$set": {
                "user_id": user_id
            }
        },
        upsert=True
    )

    find = bans.find()
    find = list(find) if find else []
    cache[0] = [ban_["user_id"] for ban_ in find]


def unban(user_id) -> None:
    bans.delete_one({"user_id": int(user_id)})

    find = bans.find()
    find = list(find) if find else []
    cache[0] = [ban_["user_id"] for ban_ in find]
