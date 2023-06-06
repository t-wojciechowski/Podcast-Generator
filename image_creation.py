from PIL import Image, ImageDraw, ImageFont, ImageShow
import random, os, requests
from io import BytesIO


def pick_bg_image():
    f_path = "bg_images"

    image_files = [file for file in os.listdir(f_path) if file.endswith(".jpg")]

    if image_files:
        background_photo = random.choice(image_files)
        return os.path.join(f_path, background_photo)
    else:
        raise ValueError("No .jpg files had been found")


bg = Image.open(pick_bg_image())

# font = ImageFont.truetype("font/kaushan_script_regular.ttf",  300)

def apple_logo():

    open_logo = Image.open("bg_images/apple_podcast_logo.png")

    position_apple_logo = (3500, 5500) # zaczynamy w lewym górnym rogu jako (0, 0)

    bg.paste(open_logo, position_apple_logo)
    ImageShow.show(bg)


def show_category():

    category_text = ImageDraw.Draw(bg)
    category_font = ImageFont.truetype("font/kaushan_script_regular.ttf",  180)
    category_postion = (3000 , 100) # Ma być to Prawy górny róg

    category_text.text(category_postion, "Your genre:\n True Crime", font=category_font, fill=(238, 232, 170))

show_category()


def first_podcast():

    first_podcast_img_url = "https://is2-ssl.mzstatic.com/image/thumb/Podcasts116/v4/4a/98/23/4a9823fa-3b4a-d634-0c87-39b2d0762ff3/mza_11730200731241651487.jpeg/55x55bb.png"
    response_first_podcast = requests.get(first_podcast_img_url)
    first_podcast_img = Image.open(BytesIO(response_first_podcast.content))
    first_podcast_img_position = (3000 ,630) # Wysokość autora #1
    resizing_img_width = 500  # Zmiana wielkości szer
    resizing_img_height = 500 # Zmiana wielkości wys
    first_podcast_img = first_podcast_img.resize((resizing_img_width, resizing_img_height))
    bg.paste(first_podcast_img, first_podcast_img_position)

    first_window_podcast = ImageDraw.Draw(bg)
    first_window_podcast_font = ImageFont.truetype("font/kaushan_script_regular.ttf",  250)
    first_window_podcast_postion = (100 , 400) # 1 wsze okno 1/3 wysokości, w zależności od wielkości obrazków
    first_window_podcast.text(first_window_podcast_postion, "·Author: Justyna Mazur\n"
                                                            "Name: Piąte: Nie zabijaj", font=first_window_podcast_font, fill=(173,255,47))

    first_window_podcast_summary_postion = (100, 960)
    first_window_podcast.text(first_window_podcast_summary_postion, "Summary: Życia,\nktóre skończyły się zbyt wcześnie"
                                                            "\nZaginięcia bez śladu.", font=first_window_podcast_font, fill=(255, 255, 255))

first_podcast()


def second_podcast():

    second_podcast_img_url = "https://is5-ssl.mzstatic.com/image/thumb/Podcasts125/v4/26/ff/2f/26ff2f79-f5bc-76c2-79e0-b86c3d95f92a/mza_6805873388653922940.jpg/55x55bb.png"
    response_second_podcast = requests.get(second_podcast_img_url)
    second_podcast_img = Image.open(BytesIO(response_second_podcast.content))
    second_podcast_img_position = (3000, 1900)  # Wysokość autora #2
    resizing_img_width = 500
    resizing_img_height = 500
    second_podcast_img = second_podcast_img.resize((resizing_img_width, resizing_img_height))
    bg.paste(second_podcast_img, second_podcast_img_position)

    second_window_podcast = ImageDraw.Draw(bg)
    second_window_podcast_font = ImageFont.truetype("font/kaushan_script_regular.ttf", 250)
    second_window_podcast_postion = (100, 1900)
    second_window_podcast.text(second_window_podcast_postion, "·Author: Zbrodnie Prowincjonalne\nName: Zbrodnie Prowincjonalne",
                                  font=second_window_podcast_font, fill=(173, 255, 47))

    second_window_podcast_summary_postion = (100, 2500)
    second_window_podcast.text(second_window_podcast_summary_postion,
                                  "Summary: Wykup subskrypcję:\nhttps://podcasters/ spotify", font=second_window_podcast_font, fill=(255, 255, 255))

second_podcast()


def third_podcast():

    third_podcast_img_url = "https://is5-ssl.mzstatic.com/image/thumb/Podcasts124/v4/db/2a/a7/db2aa702-8969-e6d3-f234-b8f91ce54ae5/mza_5524213472430200856.jpg/55x55bb.png"
    response_third_podcast = requests.get(third_podcast_img_url)
    third_podcast_img = Image.open(BytesIO(response_third_podcast.content))
    third_podcast_img_position = (3000, 3200)  # Wysokość autora #3
    resizing_img_width = 500
    resizing_img_height = 500
    third_podcast_img = third_podcast_img.resize((resizing_img_width, resizing_img_height))
    bg.paste(third_podcast_img, third_podcast_img_position)

    third_window_podcast = ImageDraw.Draw(bg)
    third_window_podcast_font = ImageFont.truetype("font/kaushan_script_regular.ttf", 250)
    third_window_podcast_postion = (100, 3200)
    third_window_podcast.text(third_window_podcast_postion, "·Author: Karolina Anna\n"
                                                              "Name: Zagadki Kryminalne",
                                  font=third_window_podcast_font, fill=(173, 255, 47))

    third_window_podcast_summary_postion = (100, 3800)
    third_window_podcast.text(third_window_podcast_summary_postion,
                                  'Summary: Odcinki "Zagadek\nKryminalnych" z kanału\nKarolina Anna w formie podcastu\n'
                                  'W filmach przedstawiam sprawy\nkryminalne z całego światam\n(porwania, zaginięcia, morderstwa,\nzjawiska paranormalne).', font=third_window_podcast_font, fill=(255, 255, 255))

third_podcast()


apple_logo()

# if apple_logo.size[0] < bg.size[0] and apple_logo.size[1] < bg.size[1]:
#
#     x = bg.size[0] - apple_logo.size[0]
#     y = bg.size[1] - apple_logo.size[1]
#
#     ready_bg = Image.new("RGB", bg.size)
#     ready_bg.paste(bg, (0, 0))
#     ready_bg.paste(apple_logo, (x, y))
#     ImageShow.show(bg)
#
# else :
#     print("Logo might be too big. Danger of overlapping")





