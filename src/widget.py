def mask_account_card(num_card_account: str | int) -> str:

    num_card_account = str(num_card_account)
    list_alpha = ""
    list_num = ""

    count = 0
    for i in num_card_account:
        if i.isalpha():
            list_alpha += i
        if i.isdigit():
            list_num += i
            count += 1

    if count == 16:
        list_summ = f"{list_num[0:4]} {list_num[4:6]}** **** {list_num[-4:]}"
    elif count == 20:
        list_summ = f"**{list_num[-4:]}"
    else:
        return f"{list_num} не является номером аккаунта или карты!"
    return f"{list_alpha} {list_summ}"


def get_date(date: str) -> str:
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
