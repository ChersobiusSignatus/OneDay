
define x = Character ("Сяо", color= "#ffdb4d" )
define p = Character ("[pname]", color= "#ffdb4d")

# The game starts here.
#yes im crazy with this line
label start:
    $ pname = renpy.input("Пожалуйста, введите своё имя", length=12, allow="qwertyuiopasdfghjklzxcvbnmMNBVCXZLKJHGFDSAPOIUYTREWQёйцукенгшщзхъфывапролджэячсмитьбюЮБЬТИМСЧЯЭЖДЛОРПАВЫФЪХЗЩШГНЕКУЦЙЁ").strip()

    if pname == "":
        $ pname = "Геге"


    play music "audio/bgmusic.mp3"

    scene bg_start with dissolve

    p "Сяо!"
    p "Хм..? Он спит?"
    p "Надо подойти поближе..."

    show xiao looking1 with dissolve
    voice "xiao/itsyou.mp3"
    x "О, это ты, [pname]."

    voice "xiao/question.mp3"
    x "Хм?"

    voice "xiao/waddup.mp3"
    x "Что-то случилось?"

    hide xiao looking1 with dissolve

    p ""

    menu:
        "Я в порядке!":
            jump imfine

        "Мне не очень хорошо...":
            jump imnot

    return

    label imfine:

        voice "xiao/sigh.mp3"
        x "Не надо много брать на себя."
        show xiao looking1 with dissolve
        x "Я вижу что что-то не так"

        hide xiao looking1
        show xiao fluttered1
        x "Я всегда рядом. Лишь назови мое имя - и я приду"
        x ""

        hide xiao fluttered1
        show xiao looking1
        x "Ты правда дорогой мне человек"
        x "Я..."

        hide xiao looking1
        show xiao fluttered2

        voice "xiao/wanted_to_confess1.mp3"
        x "Я давн-..."
        voice "xiao/wanted_to_confess2.mp3"
        x "Я давно хотел тебе признаться в кое-чем"
        x ""

        hide xiao fluttered2
        show xiao looking1

        x ""

        voice "xiao/confession.mp3"
        x "Не знаю, связано ли это с тобой, но причиняемая кармой боль последнее время не так нестерпима"
        x "Выносить ее стало легче"

        p ""
        p "Я тоже тебя люблю"

        hide xiao looking1
        show xiao looking2

        voice "xiao/smirk.mp3"
        x "В таком случае..."

        hide xiao looking1
        show xiao lesgo with dissolve

        x "...Пошли, я соберу тебе кристальных бабочек"

        hide xiao lesgo
        window hide



        pause

        centered "{size=+50}{cps=8}Sketches by:\n\n@woolfik{/cps}{/size}{p=5.0}{nw}"
        centered "{size=+50}{cps=8}Music by:\n\nChaconneScott_ACG on Piano{/cps}{/size}{p=5.0}{nw}"

        return

    label imnot:

        show xiao looking1
        voice "xiao/hmmm.mp3"
        x "Вот оно как"
        x ""

        hide xiao looking1
        show xiao fluttered1
        voice "xiao/wanted_to_confess1.mp3"
        x "Я хотел бы забрать всю боль что есть в тебе"
        x ""

        hide xiao fluttered1
        show xiao looking1
        voice "xiao/wanted_to_confess2.mp3"
        x "Но как бы мне не хотелось этого - каждый должен бороться сам"

        p "..."

        hide xiao looking1
        show xiao fluttered1
        voice "xiao/poddershka.mp3"
        x "Несмотря на это - каждому нужна поддержка в борьбе"

        hide xiao fluttered1
        show xiao fluttered2
        voice "xiao/vedtak.mp3"
        x "{size=15}Ведь так поступают когда кого-то л-...{/size}"

        p "Я тоже тебя люблю, Сяо"

        hide xiao fluttered2
        show xiao looking2
        voice "xiao/smirk.mp3"
        x "Пошли, посмотрим на звезды"

        hide xiao looking2
        show xiao flirting
        x "Мне нравится как они отражаются в твоих глазах"

        hide xiao flirting
        window hide

        pause

        centered "{size=+50}{cps=8}Sketches by:\n\n@woolfik{/cps}{/size}{p=5.0}{nw}"
        centered "{size=+50}{cps=8}Music by:\n\nChaconneScott_ACG on Piano{/cps}{/size}{p=5.0}{nw}"

        return
