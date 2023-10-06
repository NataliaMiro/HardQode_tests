import sender_stand_request



def list_id_category():
    limit = sender_stand_request.get_category().json()["count"]
    params = {"limit": limit}
    res = sender_stand_request.get_category(params).json()["results"]
    list_category_id = [i["id"] for i in res]
    return list_category_id


def list_name_category(delete=None):
    limit = sender_stand_request.get_category().json()["count"]
    params = {"limit": limit}
    resp = sender_stand_request.get_category(params).json()["results"]
    list_category_name = [i["name"] for i in res]
    if delete in list_pet_name:
        del list_pet_name[list_pet_name.index(delete)]
    return list_category_name



