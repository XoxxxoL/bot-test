import pathlib

from PIL import Image, ImageDraw, ImageFont

from misc.convert_money import convert_stats
from misc.user_misc import get_user_business_profit

from image_generate.profile.generate_bomj import generate_bomj_image


async def generate_profile_user(db_session, user, house):
    if user.custom_image:
        try:
            profile = Image.open(f'{pathlib.Path().absolute()}/image/profile/profile_{user.telegram_id}_photo.png')
        except FileNotFoundError:
            profile = Image.open(f'{pathlib.Path().absolute()}/image/profile/2_house.png')
    else:
        profile = Image.open(f'{pathlib.Path().absolute()}/image/profile/{user.house}_house.png')
    profile = profile.resize((800, 499), Image.ANTIALIAS)
    info = Image.open(f'{pathlib.Path().absolute()}/image/profile/info.png')
    profile.paste(info, info)
    draw_image = ImageDraw.Draw(profile)
    font = ImageFont.truetype(f'{pathlib.Path().absolute()}/image/font.otf', size=18)
    business_profit = await get_user_business_profit(db_session, user.info)
    # Вставка текста на картинку
    draw_image.text(
        (99, 55),
        user.name,
        font=font,
        fill=('#000000')
    )
    draw_image.text(
        (137, 80),
        f'{user.lvl} | exp: {user.exp} / {user.lvl * 50 if user.lvl != 0 else 50}',
        font=font,
        fill=('#000000')
    )
    draw_image.text(
        (133, 105),
        f'{user.rating}',
        font=font,
        fill=('#000000')
    )
    draw_image.text(
        (128, 218),
        f"{convert_stats(money=user.money)}",
        font=font,
        fill=('#000000')
    )
    draw_image.text(
        (140, 245),
        f"{convert_stats(money=user.bottle)}",
        font=font,
        fill=('#000000')
    )
    draw_image.text(
        (141, 271),
        f'{convert_stats(money=business_profit.get("money"))} руб. • {convert_stats(money=business_profit.get("bottle"))} бут. в чаc',
        font=font,
        fill=('#000000')
    )
    draw_image.text(
        (167, 319),
        f'{house.name}',
        font=font,
        fill=('#000000')
    )
    draw_image.text(
        (167, 347),
        f'{user.bomj}',
        font=font,
        fill=('#000000')
    )
    draw_image.text(
        (150, 393),
        f'{user.health}%',
        font=font,
        fill=('#000000')
    )
    draw_image.text(
        (115, 421),
        f'{user.eat}%',
        font=font,
        fill=('#000000')
    )
    draw_image.text(
        (138, 447),
        f'{user.luck}%',
        font=font,
        fill=('#000000')
    )
    try:
        user_photo = Image.open(f'{pathlib.Path().absolute()}/image/profile/{user.telegram_id}_image.png')
        user_photo = user_photo.resize((70, 70), Image.ANTIALIAS)
        profile.paste(user_photo, (713, 27))
        pathlib.Path(f'{pathlib.Path().absolute()}/image/profile/{user.telegram_id}_image.png').unlink()
    except:
        pass
    if user.vip:
        vip = Image.open(f'{pathlib.Path().absolute()}/image/profile/vip.png')
        profile.paste(vip, (621, 27), vip)
    await generate_bomj_image(db_session, user)
    bomj_img = Image.open(f'{pathlib.Path().absolute()}/image/profile/{user.telegram_id}_bomj.png')
    profile.paste(bomj_img, (577, 138), bomj_img)
    profile.save(f'{pathlib.Path().absolute()}/image/profile/{user.telegram_id}_profile.png')
