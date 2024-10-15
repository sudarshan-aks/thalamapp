import flet as fl
import time
import threading

sharp = fl.Audio(src = "/jalra_sharp.wav", autoplay = False, volume = 100, release_mode = fl.audio.ReleaseMode.STOP)
flat = fl.Audio(src = "/jalra_flat.wav", autoplay = False, volume = 109, release_mode = fl.audio.ReleaseMode.STOP)

bpm_count = 90 

# colors:

unlit_circle = '#8fb9ff'
lit_circle = '#ff8e1c'
primary_color = '#6d99e3'
secondary_color = '#f4f4fc'
dark = '#252a3e'
dark_sec = '#2f3855'
light = '#f4f4fc'
light_sec = '#d7d8de'
bgcolor_sec = dark_sec
bgcolor = dark


lit_up_circle = fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = fl.colors.BLUE, width = 25, height = 25)

anudhrutham_row = [fl.Container(shape = fl.BoxShape.CIRCLE, content = fl.Text("C"), alignment = fl.alignment.center ,bgcolor = unlit_circle, width = 25, height = 25)]

chapu = [fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = fl.colors.BLUE, width = 25, height = 25), fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = fl.colors.BLUE, width = 25, height = 25), fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = fl.colors.BLUE, width = 25, height = 25)]

laghu_chaturasram_row = [fl.Container(shape = fl.BoxShape.CIRCLE, content = fl.Text("I"), alignment = fl.alignment.center ,bgcolor = unlit_circle, width = 25, height = 25), 
                         fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25)]

laghu_thisram_row = [fl.Container(shape = fl.BoxShape.CIRCLE, content = fl.Text("I"), alignment = fl.alignment.center ,bgcolor = unlit_circle, width = 25, height = 25), 
                         fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25)]

laghu_thisram_row_twice = [fl.Container(shape = fl.BoxShape.CIRCLE, content = fl.Text("I"), alignment = fl.alignment.center ,bgcolor = unlit_circle, width = 25, height = 25), 
                         fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, content = fl.Text("I"), alignment = fl.alignment.center ,bgcolor = unlit_circle, width = 25, height = 25), 
                         fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25)]

laghu_khandam_row = [fl.Container(shape = fl.BoxShape.CIRCLE, content = fl.Text("I"), alignment = fl.alignment.center ,bgcolor = unlit_circle, width = 25, height = 25), 
                         fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25)]

laghu_khandam_row_twice = [fl.Container(shape = fl.BoxShape.CIRCLE, content = fl.Text("I"), alignment = fl.alignment.center ,bgcolor = unlit_circle, width = 25, height = 25), 
                         fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, content = fl.Text("I"), alignment = fl.alignment.center ,bgcolor = unlit_circle, width = 25, height = 25), 
                         fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25)]

laghu_misram_row = [fl.Container(shape = fl.BoxShape.CIRCLE, content = fl.Text("I"), alignment = fl.alignment.center ,bgcolor = unlit_circle, width = 25, height = 25), 
                         fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),]

laghu_misram_row_twice = [fl.Container(shape = fl.BoxShape.CIRCLE, content = fl.Text("I"), alignment = fl.alignment.center ,bgcolor = unlit_circle, width = 25, height = 25), 
                         fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, content = fl.Text("I"), alignment = fl.alignment.center ,bgcolor = unlit_circle, width = 25, height = 25), 
                         fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),]

laghu_sankeernam_row = [fl.Container(shape = fl.BoxShape.CIRCLE, content = fl.Text("I"), alignment = fl.alignment.center ,bgcolor = unlit_circle, width = 25, height = 25), 
                         fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),]

laghu_sankeernam_row_twice = [fl.Container(shape = fl.BoxShape.CIRCLE, content = fl.Text("I"), alignment = fl.alignment.center ,bgcolor = unlit_circle, width = 25, height = 25), 
                         fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, content = fl.Text("I"), alignment = fl.alignment.center ,bgcolor = unlit_circle, width = 25, height = 25), 
                         fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),]

dhrutham_row = [fl.Container(shape = fl.BoxShape.CIRCLE, content = fl.Text("O"), 
                             alignment = fl.alignment.center ,bgcolor = unlit_circle, width = 25, height = 25), 
                         fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25)]

dhrutham_row_twice = [fl.Container(shape = fl.BoxShape.CIRCLE, content = fl.Text("O"), 
                             alignment = fl.alignment.center ,bgcolor = unlit_circle, width = 25, height = 25), 
                         fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                         fl.Container(shape = fl.BoxShape.CIRCLE, content = fl.Text("O"), 
                             alignment = fl.alignment.center ,bgcolor = unlit_circle, width = 25, height = 25), 
                         fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25)]

laghu_chaturasram_row_twice =  [fl.Container(shape = fl.BoxShape.CIRCLE, content = fl.Text("I"), alignment = fl.alignment.center ,bgcolor = unlit_circle, width = 25, height = 25), 
                         fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, content = fl.Text("I"), alignment = fl.alignment.center ,bgcolor = unlit_circle, width = 25, height = 25), 
                         fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25)]

selected_thalam = "Aadhi"
thalam_playing = False

button_style_light = fl.ButtonStyle(color = primary_color, overlay_color = dark_sec)
button_style_dark = fl.ButtonStyle(color = primary_color, overlay_color = light_sec)

current_thalam_row = (laghu_chaturasram_row + dhrutham_row_twice)

class ThalamTiles(fl.ListTile):
    def __init__(self, thalam_name, thalam_selected):
        super().__init__()
        self.thalam_name = thalam_name
        self.title = fl.Text(thalam_name, color = secondary_color, size = 15)
        self.toggle_inputs = True
        self.bgcolor = bgcolor_sec
        self.selected_tile_color = primary_color
        self.on_click = lambda _: thalam_selected(e = self, thalam_name = self.thalam_name)
        self.visible = True
        self.selected = False
        if self.thalam_name == "Aadhi" or self.thalam_name == "Jampa":
            self.selected = True 
        self.dense = True

def main(page: fl.Page):


# thalam functions
    def adhi2kala(e):
        time.sleep(60/bpm_count)
        sharp.play()
        thalam_row.controls[e-1].bgcolor = unlit_circle
        thalam_row.controls[e].bgcolor = lit_circle
        thalam_row.update() 
        time.sleep(60/bpm_count)
        sharp.play()
        time.sleep(60/bpm_count)
        flat.play()
        thalam_row.controls[e].bgcolor = unlit_circle
        thalam_row.controls[e+1].bgcolor = lit_circle
        thalam_row.update()
        time.sleep(60/bpm_count)
        flat.play()
        time.sleep(60/bpm_count)
        flat.play()
        thalam_row.controls[e+1].bgcolor = unlit_circle
        thalam_row.controls[e+2].bgcolor = lit_circle
        thalam_row.update()
        time.sleep(60/bpm_count)
        flat.play()
        time.sleep(60/bpm_count)
        flat.play()
        thalam_row.controls[e+2].bgcolor = unlit_circle
        thalam_row.controls[e+3].bgcolor = lit_circle
        thalam_row.update()
        time.sleep(60/bpm_count)
        flat.play()
        time.sleep(60/bpm_count)
# -----------DHRUTHAM-----------------
        sharp.play()
        thalam_row.controls[e+3].bgcolor = unlit_circle
        thalam_row.controls[e+4].bgcolor = lit_circle
        thalam_row.update()
        time.sleep(60/bpm_count)
        sharp.play()
        time.sleep(60/bpm_count)
        flat.play()
        thalam_row.controls[e+4].bgcolor = unlit_circle
        thalam_row.controls[e+5].bgcolor = lit_circle
        thalam_row.update()
        time.sleep(60/bpm_count)
        flat.play()
        time.sleep(60/bpm_count)
        sharp.play()
        thalam_row.controls[e+5].bgcolor = unlit_circle
        thalam_row.controls[e+6].bgcolor = lit_circle
        thalam_row.update()
        time.sleep(60/bpm_count)
        sharp.play()
        time.sleep(60/bpm_count)
        flat.play()
        thalam_row.controls[e+6].bgcolor = unlit_circle
        thalam_row.controls[e+7].bgcolor = lit_circle
        thalam_row.update()
        time.sleep(60/bpm_count)
        flat.play()

    def laghu_chaturasram(e):
        time.sleep(60/bpm_count)
        sharp.play()
        thalam_row.controls[e-1].bgcolor = unlit_circle
        thalam_row.controls[e].bgcolor = lit_circle
        thalam_row.update()    
        time.sleep(60/bpm_count)
        flat.play()
        thalam_row.controls[e].bgcolor = unlit_circle
        thalam_row.controls[e+1].bgcolor = lit_circle
        thalam_row.update()
        time.sleep(60/bpm_count)
        flat.play()
        thalam_row.controls[e+1].bgcolor = unlit_circle
        thalam_row.controls[e+2].bgcolor = lit_circle
        thalam_row.update()
        time.sleep(60/bpm_count)
        flat.play()
        thalam_row.controls[e+2].bgcolor = unlit_circle
        thalam_row.controls[e+3].bgcolor = lit_circle
        thalam_row.update()
            
    def laghu_thisram(e):
        time.sleep(60/bpm_count)
        sharp.play()
        thalam_row.controls[e-1].bgcolor = unlit_circle
        thalam_row.controls[e].bgcolor = lit_circle
        thalam_row.update()    
        e+=1
        for x in range(2):
            time.sleep(60/bpm_count)
            flat.play()
            thalam_row.controls[e-1].bgcolor = unlit_circle
            thalam_row.controls[e].bgcolor = lit_circle
            thalam_row.update()
            e+=1

    def laghu_khandam(e):
        time.sleep(60/bpm_count)
        sharp.play()
        thalam_row.controls[e-1].bgcolor = unlit_circle
        thalam_row.controls[e].bgcolor = lit_circle
        thalam_row.update()    
        e+=1
        for x in range(4):
            time.sleep(60/bpm_count)
            flat.play()
            thalam_row.controls[e-1].bgcolor = unlit_circle
            thalam_row.controls[e].bgcolor = lit_circle
            thalam_row.update()
            e+=1

    def laghu_misram(e):
        time.sleep(60/bpm_count)
        sharp.play()
        thalam_row.controls[e-1].bgcolor = unlit_circle
        thalam_row.controls[e].bgcolor = lit_circle
        thalam_row.update()    
        e+=1
        for x in range(6):
            time.sleep(60/bpm_count)
            flat.play()
            thalam_row.controls[e-1].bgcolor = unlit_circle
            thalam_row.controls[e].bgcolor = lit_circle
            thalam_row.update()
            e+=1

    def laghu_sankeernam(e):
        time.sleep(60/bpm_count)
        sharp.play()
        thalam_row.controls[e-1].bgcolor = unlit_circle
        thalam_row.controls[e].bgcolor = lit_circle
        thalam_row.update()    
        e+=1
        for x in range(8):
            time.sleep(60/bpm_count)
            flat.play()
            thalam_row.controls[e-1].bgcolor = unlit_circle
            thalam_row.controls[e].bgcolor = lit_circle
            thalam_row.update()
            e+=1

    def dhrutham(e):
        time.sleep(60/bpm_count)
        sharp.play()
        thalam_row.controls[e-1].bgcolor = unlit_circle
        thalam_row.controls[e].bgcolor = lit_circle
        thalam_row.update()
        time.sleep(60/bpm_count)
        flat.play()
        thalam_row.controls[e].bgcolor = unlit_circle
        thalam_row.controls[e+1].bgcolor = lit_circle
        thalam_row.update()

    def anudhrutham_flat(e):
        time.sleep(60/bpm_count)
        flat.play()
        thalam_row.controls[e-1].bgcolor = unlit_circle
        thalam_row.controls[e].bgcolor = lit_circle
        thalam_row.update()

    def anudhrutham_sharp(e):
        time.sleep(60/bpm_count)
        sharp.play()
        thalam_row.controls[e-1].bgcolor = unlit_circle
        thalam_row.controls[e].bgcolor = lit_circle
        thalam_row.update()


    page.theme_mode = fl.ThemeMode.LIGHT
    page.bgcolor = bgcolor
    page.theme = fl.Theme(
        color_scheme = fl.ColorScheme(
            primary = primary_color,
            primary_container = primary_color,
            secondary = secondary_color,
        ))

    def theme_changed(new_bgcolor, new_secondary):
        if new_bgcolor == light:
            dark_light_button.icon = fl.icons.DARK_MODE
            new_bgcolor = dark
            new_secondary = light
            new_bgcolor_sec = dark_sec
            buttons.style = button_style_dark
        else:
            dark_light_button.icon = fl.icons.LIGHT_MODE
            new_bgcolor = light
            new_secondary = dark
            new_bgcolor_sec = light_sec
            buttons.style = button_style_light
        global bgcolor_sec
        global bgcolor
        global secondary_color
        bgcolor_sec = new_bgcolor_sec
        bgcolor = new_bgcolor
        secondary_color = new_secondary
        for x in thalam_selection_final.controls:
            x.bgcolor = bgcolor_sec
            x.title.color = secondary_color
            x.update()
        # if default_button.bgcolor == primary_color:
        #     sooladhi_button.bgcolor = bgcolor_sec
        # else:
        #     default_button.bgcolor = bgcolor_sec

        

        page.bgcolor = bgcolor
        page.update()

    dark_light_button = fl.IconButton(fl.icons.DARK_MODE, icon_color = '#ecf1f7', on_click = lambda e: theme_changed(new_bgcolor = page.bgcolor, new_secondary = secondary_color))

    Appbar = fl.AppBar(
        leading = dark_light_button,
        bgcolor = '#5a8ee6',
        title = fl.Text("Wonder Box", color = '#ecf1f7'),
        surface_tint_color = lit_circle, 
        shadow_color = lit_circle,
        elevation = 4)
    
    page.overlay.append(flat)
    page.overlay.append(sharp)



# BPM DISPLAY ROW

    bpm_display = fl.Container(
        content = fl.Text(f"{bpm_count} BPM", scale = 1.25, color = fl.colors.WHITE),
        margin = 10,
        padding = 10,
        alignment = fl.alignment.center,
        width = 115, height = 75,
        border_radius = 10,
        ink = True,
        bgcolor = primary_color,
        shadow=fl.BoxShadow(
                    spread_radius=1,
                    blur_radius=13,
                    color=lit_circle,
                    offset=fl.Offset(2,2),
                    blur_style=fl.ShadowBlurStyle.INNER,),
        on_click = None
    )

    def add_bpm(e):
        global bpm_count
        bpm_count+=1
        bpm_display.content.value = f"{bpm_count} BPM"
        bpm_display.update()
    
    def minus_bpm(e):
        global bpm_count
        bpm_count-=1
        bpm_display.content.value = f"{bpm_count} BPM"
        bpm_display.update()

    def minus_5_bpm(e):
        global bpm_count
        bpm_count-=5
        bpm_display.content.value = f"{bpm_count} BPM"
        bpm_display.update()

    def add_5_bpm(e):
        global bpm_count
        bpm_count+=5
        bpm_display.content.value = f"{bpm_count} BPM"
        bpm_display.update()

    add1button = fl.TextButton(content = fl.Text("+1", size = 20), on_click = add_bpm)
    minus1button = fl.TextButton(content = fl.Text("-1", size = 20), on_click = minus_bpm)
    add5button = fl.TextButton(content = fl.Text("+5", size = 20), on_click = add_5_bpm)
    minus5button = fl.TextButton(content = fl.Text("-5", size = 20), on_click = minus_5_bpm)

    bpm_row = fl.Row([
        fl.Column([minus1button, minus5button]),
        bpm_display,
        fl.Column([add1button, add5button]), 
    ], alignment = 'CENTER')



# Tap Button

    def start_tap(e):
        global start_time
        start_time = time.time()
        
        tap_button_new.on_click = stop_tap
        tap_button_new.text = "Tap 2"
        tap_button_new.update()

    def stop_tap(e):
        global bpm_count
        stop_time = time.time() - start_time
        
        bpm_count = int(60/stop_time)
       
        tap_button_new.on_click = start_tap
        tap_button_new.text = "Tap"
        bpm_display.content.value = f"{bpm_count} BPM"
        bpm_display.update()
        tap_button_new.update()

    tap_button_new = fl.ElevatedButton(text = "Tap", on_click = start_tap, width = 75)


# Volume Column

    def volume_change(e):
        sharp.volume = e.control.value/100
        flat.volume = e.control.value/100
        sharp.update()
        flat.update()

    volume_text = fl.Text("Volume", color = light, size = 16)
    volume_slider =fl.Slider(min = 0, max = 100, divisions = 100, 
                                    label = "{value}%", 
                                on_change = volume_change, value = 50, width = 250)
    
    volume_column = fl.Column([
        fl.Row([fl.Container(content = None, bgcolor = dark, width = 10), volume_text]),
        fl.Row([volume_slider, tap_button_new], alignment = fl.MainAxisAlignment.SPACE_EVENLY)
    ], spacing = 2)

# THALAM SELECTION

    # default_button = fl.CupertinoFilledButton(content = fl.Text("Default", color = light), 
    #                                           bgcolor = primary_color)

    # sooladhi_button = fl.CupertinoFilledButton(content = fl.Text("Sooladhi", color = primary_color), 
    #                                            bgcolor = light)

    # def default_changed(e):
    #     if default_button.bgcolor == bgcolor_sec:
    #         default_button.bgcolor = primary_color
    #         default_button.color = light
    #         sooladhi_button.bgcolor = bgcolor_sec
    #         sooladhi_button.color = primary_color
    #         thalam_jathi_dropdown.disabled = True
    #         thalam_selection_final.controls = [ThalamTiles("Aadhi", thalam_selected), 
    #                    ThalamTiles("Aadhi 2 Kala", thalam_selected),
    #                    ThalamTiles("Roopakam", thalam_selected),
    #                    ThalamTiles("Misra Chapu", thalam_selected),
    #                     ThalamTiles("Khanda Chapu", thalam_selected)]
            
    #     elif default_button.bgcolor == primary_color:
    #         default_button.bgcolor = bgcolor_sec
    #         default_button.color = primary_color
    #         sooladhi_button.bgcolor = primary_color
    #         sooladhi_button.color = light
    #         thalam_jathi_dropdown.disabled = False
    #         thalam_selection_final.controls = [ThalamTiles("Dhruva", thalam_selected), 
    #                    ThalamTiles("Matya", thalam_selected),
    #                    ThalamTiles("Roopaka", thalam_selected),
    #                    ThalamTiles("Jampa", thalam_selected),
    #                     ThalamTiles("Thripuda", thalam_selected),
    #                     ThalamTiles("Ata", thalam_selected),
    #                     ThalamTiles("Eka", thalam_selected)]
    #     page.update()

    thalam_jathi_dropdown = fl.Dropdown(
        scale = 0.9,
        width = 150,
        options = [
            fl.dropdown.Option("Thisram"),
            fl.dropdown.Option("Chaturasram"),
            fl.dropdown.Option("Khandam"),
            fl.dropdown.Option("Misram"),
            fl.dropdown.Option("Sankeernam")
        ], value = "Chaturasram", bgcolor = light, border_color = lit_circle, hint_text = "Jaathi", disabled = True)

    def default_sooladhi_changed(e):

        if default_sooladhi_button.selected == {"sooladhi"}:
            thalam_selection_final.controls = [ThalamTiles("Dhruva", thalam_selected), 
                       ThalamTiles("Matya", thalam_selected),
                       ThalamTiles("Roopaka", thalam_selected),
                       ThalamTiles("Jampa", thalam_selected),
                        ThalamTiles("Thripuda", thalam_selected),
                        ThalamTiles("Ata", thalam_selected),
                        ThalamTiles("Eka", thalam_selected)]
            thalam_jathi_dropdown.disabled = False
        
        elif default_sooladhi_button.selected == {"default"}:
            thalam_selection_final.controls = [ThalamTiles("Aadhi", thalam_selected), 
                       ThalamTiles("Aadhi 2 Kala", thalam_selected),
                       ThalamTiles("Roopakam", thalam_selected),
                       ThalamTiles("Misra Chapu", thalam_selected),
                        ThalamTiles("Khanda Chapu", thalam_selected)]
            thalam_jathi_dropdown.disabled = True
        thalam_selection_final.update()
        thalam_jathi_dropdown.update()    
        

    default_sooladhi_button = fl.SegmentedButton(
        selected = {"default"},
        show_selected_icon = False, 
        on_change = default_sooladhi_changed,
        allow_multiple_selection = False,
        segments = [
            fl.Segment(
                value = "default",
                label = fl.Text("Default")
            ),
            fl.Segment(
                value = "sooladhi",
                label = fl.Text("Sooladhi")
            )], style = button_style_dark
    )

    # default_button = fl.ElevatedButton(text = "Default", bgcolor = primary_color, on_click = default_changed, color = light)
    # sooladhi_button = fl.ElevatedButton(text = "Sooladhi", bgcolor = bgcolor_sec, on_click = default_changed, color = primary_color)
    default_sooladhi_selection = fl.Row([fl.Row([default_sooladhi_button]), thalam_jathi_dropdown], alignment = fl.MainAxisAlignment.SPACE_AROUND)

    @staticmethod
    def thalam_selected(e, thalam_name):
        for x in thalam_selection_final.controls:
            x.selected = False
            x.update()
        global selected_thalam
        selected_thalam = thalam_name
        e.selected = True
        e.update()

    thalam_selection_final = fl.Column(controls = [ThalamTiles("Aadhi", thalam_selected), 
                       ThalamTiles("Aadhi 2 Kala", thalam_selected),
                       ThalamTiles("Roopakam", thalam_selected),
                       ThalamTiles("Misra Chapu", thalam_selected),
                        ThalamTiles("Khanda Chapu", thalam_selected)],
                          scroll = fl.ScrollMode.HIDDEN)


    page.scroll = fl.ScrollMode.HIDDEN

# METRONOME CIRCLES

    thalam_row = fl.thalam_row = fl.Row(controls = (laghu_chaturasram_row + dhrutham_row_twice), spacing = 19, wrap = True, run_spacing = 10,alignment = fl.MainAxisAlignment.CENTER, width =500)

    def play_thalam(thalam_name):
        print(flat.src)
        print(sharp.src)
        play_button.icon = fl.icons.PAUSE
        play_button.on_click = pause_thalam
        play_button.update()
        global thalam_playing
        thalam_playing = True
        if thalam_name == "Aadhi" or thalam_name == "Aadhi 2 Kala":
            thalam_row.controls = laghu_chaturasram_row + dhrutham_row_twice
        elif thalam_name == "Roopakam" or thalam_name == "Khanda Chapu" or thalam_name == "Misra Chapu":
            thalam_row.controls = chapu
        elif thalam_name == "Dhruva" and thalam_jathi_dropdown.value == "Chaturasram":
            thalam_row.controls = (laghu_chaturasram_row + dhrutham_row + laghu_chaturasram_row_twice)
        elif thalam_name == "Dhruva" and thalam_jathi_dropdown.value == "Thisram":
            thalam_row.controls = (laghu_thisram_row + dhrutham_row + laghu_thisram_row_twice)
        elif thalam_name == "Dhruva" and thalam_jathi_dropdown.value == "Misram":
            thalam_row.controls = (laghu_misram_row + dhrutham_row + laghu_misram_row_twice)
        elif thalam_name == "Dhruva" and thalam_jathi_dropdown.value == "Khandam":
            thalam_row.controls = (laghu_khandam_row + dhrutham_row + laghu_khandam_row_twice)
        elif thalam_name == "Dhruva" and thalam_jathi_dropdown.value == "Sankeernam":
            thalam_row.controls = (laghu_sankeernam_row + dhrutham_row + laghu_sankeernam_row_twice)
        elif thalam_name == "Matya" and thalam_jathi_dropdown.value == "Chaturasram":
            thalam_row.controls = (laghu_chaturasram_row + dhrutham_row + [fl.Container(shape = fl.BoxShape.CIRCLE, content = fl.Text("I"), alignment = fl.alignment.center ,bgcolor = fl.colors.BLUE, width = 25, height = 25), 
                         fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                           fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25)])
        elif thalam_name == "Matya" and thalam_jathi_dropdown.value == "Thisram":
            thalam_row.controls = (laghu_thisram_row + dhrutham_row + [fl.Container(shape = fl.BoxShape.CIRCLE, content = fl.Text("I"), alignment = fl.alignment.center ,bgcolor = unlit_circle, width = 25, height = 25), 
                         fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25)])
        elif thalam_name == "Matya" and thalam_jathi_dropdown.value == "Khandam":
            thalam_row.controls = (laghu_khandam_row + dhrutham_row + [fl.Container(shape = fl.BoxShape.CIRCLE, content = fl.Text("I"), alignment = fl.alignment.center ,bgcolor = unlit_circle, width = 25, height = 25), 
                         fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25)])
        elif thalam_name == "Matya" and thalam_jathi_dropdown.value == "Misram":
            thalam_row.controls = (laghu_misram_row + dhrutham_row + [fl.Container(shape = fl.BoxShape.CIRCLE, content = fl.Text("I"), alignment = fl.alignment.center ,bgcolor = unlit_circle, width = 25, height = 25), 
                         fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25)])
        elif thalam_name == "Matya" and thalam_jathi_dropdown.value == "Sankeernam":
            thalam_row.controls = (laghu_sankeernam_row + dhrutham_row + [fl.Container(shape = fl.BoxShape.CIRCLE, content = fl.Text("I"), alignment = fl.alignment.center ,bgcolor = unlit_circle, width = 25, height = 25), 
                         fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),
                          fl.Container(shape = fl.BoxShape.CIRCLE, bgcolor = unlit_circle, width = 25, height = 25),])
        elif thalam_name == "Roopaka" and thalam_jathi_dropdown.value == "Chaturasram":
            thalam_row.controls = (dhrutham_row + laghu_chaturasram_row)
        elif thalam_name == "Roopaka" and thalam_jathi_dropdown.value == "Thisram":
            thalam_row.controls = (dhrutham_row + laghu_thisram_row)
        elif thalam_name == "Roopaka" and thalam_jathi_dropdown.value == "Khandam":
            thalam_row.controls = (dhrutham_row + laghu_khandam_row)
        elif thalam_name == "Roopaka" and thalam_jathi_dropdown.value == "Misram":
            thalam_row.controls = (dhrutham_row + laghu_misram_row)
        elif thalam_name == "Roopaka" and thalam_jathi_dropdown.value == "Sankeernam":
            thalam_row.controls = (dhrutham_row + laghu_sankeernam_row)
        elif thalam_name == "Jampa" and thalam_jathi_dropdown.value == "Chaturasram":
            thalam_row.controls = (laghu_chaturasram_row + anudhrutham_row + dhrutham_row)
        elif thalam_name == "Jampa" and thalam_jathi_dropdown.value == "Thisram":
            thalam_row.controls = (laghu_thisram_row + anudhrutham_row + dhrutham_row)
        elif thalam_name == "Jampa" and thalam_jathi_dropdown.value == "Misram":
            thalam_row.controls = (laghu_misram_row + anudhrutham_row + dhrutham_row)
        elif thalam_name == "Jampa" and thalam_jathi_dropdown.value == "Khandam":
            thalam_row.controls = (laghu_khandam_row + anudhrutham_row + dhrutham_row)
        elif thalam_name == "Jampa" and thalam_jathi_dropdown.value == "Sankeernam":
            thalam_row.controls = (laghu_sankeernam_row + anudhrutham_row + dhrutham_row)
        elif thalam_name == "Thripuda" and thalam_jathi_dropdown.value == "Chaturasram":
            thalam_row.controls = (laghu_chaturasram_row + dhrutham_row_twice)
        elif thalam_name == "Thripuda" and thalam_jathi_dropdown.value == "Thisram":
            thalam_row.controls = (laghu_thisram_row + dhrutham_row_twice)
        elif thalam_name == "Thripuda" and thalam_jathi_dropdown.value == "Khandam":
            thalam_row.controls = (laghu_khandam_row + dhrutham_row_twice)
        elif thalam_name == "Thripuda" and thalam_jathi_dropdown.value == "Misram":
            thalam_row.controls = (laghu_misram_row + dhrutham_row_twice)
        elif thalam_name == "Thripuda" and thalam_jathi_dropdown.value == "Sankeernam":
            thalam_row.controls = (laghu_sankeernam_row + dhrutham_row_twice)
        elif thalam_name == "Ata" and thalam_jathi_dropdown.value == "Chaturasram":
            thalam_row.controls = (laghu_chaturasram_row_twice + dhrutham_row_twice)
        elif thalam_name == "Ata" and thalam_jathi_dropdown.value == "Thisram":
            thalam_row.controls = (laghu_thisram_row_twice + dhrutham_row_twice)
        elif thalam_name == "Ata" and thalam_jathi_dropdown.value == "Khandam":
            thalam_row.controls = (laghu_khandam_row_twice + dhrutham_row_twice)
        elif thalam_name == "Ata" and thalam_jathi_dropdown.value == "Misram":
            thalam_row.controls = (laghu_misram_row_twice + dhrutham_row_twice)
        elif thalam_name == "Ata" and thalam_jathi_dropdown.value == "Sankeernam":
            thalam_row.controls = (laghu_sankeernam_row_twice + dhrutham_row_twice)
        elif thalam_name == "Eka" and thalam_jathi_dropdown.value == "Chaturasram":
            thalam_row.controls = (laghu_chaturasram_row)
        elif thalam_name == "Eka" and thalam_jathi_dropdown.value == "Thisram":
            thalam_row.controls = (laghu_thisram_row)
        elif thalam_name == "Eka" and thalam_jathi_dropdown.value == "Khandam":
            thalam_row.controls = (laghu_khandam_row)
        elif thalam_name == "Eka" and thalam_jathi_dropdown.value == "Misram":
            thalam_row.controls = (laghu_misram_row)
        elif thalam_name == "Eka" and thalam_jathi_dropdown.value == "Sankeernam":
            thalam_row.controls = (laghu_sankeernam_row)
        thalam_row.update()
        while thalam_playing:
            if thalam_name == "Aadhi":
                laghu_chaturasram(0)
                dhrutham(4)
                dhrutham(6)
            elif thalam_name == "Aadhi 2 Kala":
                adhi2kala(0)
            elif thalam_name == "Roopakam":
                anudhrutham_sharp(0)
                dhrutham(1)
            elif thalam_name == "Misra Chapu":
                time.sleep(60/bpm_count)
                sharp.play()
                thalam_row.controls[-1].bgcolor = unlit_circle
                thalam_row.controls[0].bgcolor = lit_circle
                thalam_row.update()
                time.sleep(30/bpm_count)
                flat.play()
                
                anudhrutham_flat(1)
                anudhrutham_flat(2)
            elif thalam_name == "Khanda Chapu":
                anudhrutham_sharp(0)
                time.sleep(60/bpm_count)
                sharp.play()
                thalam_row.controls[0].bgcolor = unlit_circle
                thalam_row.controls[1].bgcolor = lit_circle
                thalam_row.update()
                time.sleep(30/bpm_count)
                sharp.play()
                thalam_row.controls[1].bgcolor = unlit_circle
                thalam_row.controls[2].bgcolor = lit_circle
                thalam_row.update()
            elif thalam_name == "Dhruva":
                if thalam_jathi_dropdown.value == "Chaturasram":
                    laghu_chaturasram(0)
                    dhrutham(4)
                    laghu_chaturasram(6)
                    laghu_chaturasram(10)
                elif thalam_jathi_dropdown.value == "Thisram":
                    laghu_thisram(0)
                    dhrutham(3)
                    laghu_thisram(5)
                    laghu_thisram(8)
                elif thalam_jathi_dropdown.value == "Khandam":
                    laghu_khandam(0)
                    dhrutham(5)
                    laghu_khandam(7)
                    laghu_khandam(12)
                elif thalam_jathi_dropdown.value == "Misram":
                    laghu_misram(0)
                    dhrutham(7)
                    laghu_misram(9)
                    laghu_misram(16)
                elif thalam_jathi_dropdown.value == "Sankeernam":
                    laghu_sankeernam(0)
                    dhrutham(9)
                    laghu_sankeernam(11)
                    laghu_sankeernam(20)
            elif thalam_name == "Matya":
                if thalam_jathi_dropdown.value == "Chaturasram":
                    laghu_chaturasram(0)
                    dhrutham(4)
                    laghu_chaturasram(6)
                elif thalam_jathi_dropdown.value == "Thisram":
                    laghu_thisram(0)
                    dhrutham(3)
                    laghu_thisram(5)
                elif thalam_jathi_dropdown.value == "Khandam":
                    laghu_khandam(0)
                    dhrutham(5)
                    laghu_khandam(7)
                elif thalam_jathi_dropdown.value == "Misram":
                    laghu_misram(0)
                    dhrutham(7)
                    laghu_misram(9)
                elif thalam_jathi_dropdown.value == "Sankeernam":
                    laghu_sankeernam(0)
                    dhrutham(9)
                    laghu_sankeernam(11)
            elif thalam_name == "Roopaka":
                if thalam_jathi_dropdown.value == "Chaturasram":
                    dhrutham(0)
                    laghu_chaturasram(2)
                elif thalam_jathi_dropdown.value == "Thisram":
                    dhrutham(0)
                    laghu_thisram(2)
                elif thalam_jathi_dropdown.value == "Khandam":
                    dhrutham(0)
                    laghu_khandam(2)
                elif thalam_jathi_dropdown.value == "Misram":
                    dhrutham(0)
                    laghu_misram(2)
                elif thalam_jathi_dropdown.value == "Sankeernam":
                    dhrutham(0)
                    laghu_sankeernam(2)
            elif thalam_name == "Jampa":
                if thalam_jathi_dropdown.value == "Chaturasram":
                    laghu_chaturasram(0)
                    anudhrutham_sharp(4)
                    dhrutham(5)
                    
                elif thalam_jathi_dropdown.value == "Thisram":
                    laghu_thisram(0)
                    anudhrutham_sharp(3)
                    dhrutham(4)
                    
                elif thalam_jathi_dropdown.value == "Khandam":
                    laghu_khandam(0)
                    anudhrutham_sharp(5)
                    dhrutham(6)
                    
                elif thalam_jathi_dropdown.value == "Misram":
                    laghu_misram(0)
                    anudhrutham_sharp(7)
                    dhrutham(8)
                    
                elif thalam_jathi_dropdown.value == "Sankeernam":
                    laghu_sankeernam(0)
                    anudhrutham_sharp(9)
                    dhrutham(10)
            elif thalam_name == "Thripuda":
                if thalam_jathi_dropdown.value == "Chaturasram":
                    laghu_chaturasram(0)
                    dhrutham(4)
                    dhrutham(6)
                    
                elif thalam_jathi_dropdown.value == "Thisram":
                    laghu_thisram(0)
                    dhrutham(3)
                    dhrutham(5)
                    
                elif thalam_jathi_dropdown.value == "Khandam":
                    laghu_khandam(0)
                    dhrutham(5)
                    dhrutham(7)
                    
                elif thalam_jathi_dropdown.value == "Misram":
                    laghu_misram(0)
                    dhrutham(7)
                    dhrutham(9)
                    
                elif thalam_jathi_dropdown.value == "Sankeernam":
                    laghu_sankeernam(0)
                    dhrutham(9)
                    dhrutham(11)
            elif thalam_name == "Ata":
                if thalam_jathi_dropdown.value == "Chaturasram":
                    laghu_chaturasram(0)
                    laghu_chaturasram(4)
                    dhrutham(8)
                    dhrutham(10)
                    
                elif thalam_jathi_dropdown.value == "Thisram":
                    laghu_thisram(0)
                    laghu_thisram(3)
                    dhrutham(6)
                    dhrutham(8)
                    
                elif thalam_jathi_dropdown.value == "Khandam":
                    laghu_khandam(0)
                    laghu_khandam(5)
                    dhrutham(10)
                    dhrutham(12)
                    
                elif thalam_jathi_dropdown.value == "Misram":
                    laghu_misram(0)
                    laghu_misram(7)
                    dhrutham(14)
                    dhrutham(16)
                    
                elif thalam_jathi_dropdown.value == "Sankeernam":
                    laghu_sankeernam(0)
                    laghu_sankeernam(9)
                    dhrutham(18)
                    dhrutham(20)
            elif thalam_name == "Eka":
                if thalam_jathi_dropdown.value == "Chaturasram":
                    laghu_chaturasram(0)
                    
                elif thalam_jathi_dropdown.value == "Thisram":
                    laghu_thisram(0)
                    
                elif thalam_jathi_dropdown.value == "Khandam":
                    laghu_khandam(0)
                    
                elif thalam_jathi_dropdown.value == "Misram":
                    laghu_misram(0)
                    
                elif thalam_jathi_dropdown.value == "Sankeernam":
                    laghu_sankeernam(0)
        anudhrutham_sharp(0)          
        thalam_playing = False

    def pause_thalam(e):
        global thalam_playing
        thalam_playing = False
        play_button.icon = fl.icons.PLAY_ARROW
        play_button.on_click = lambda _: play_thalam(selected_thalam)
        play_button.update()

# PLAY BUTTON, NEXT PREV THALAM

    play_button = fl.IconButton(fl.icons.PLAY_ARROW, on_click = lambda e: play_thalam(selected_thalam), bgcolor = primary_color, icon_color = light)

    def sound_changed(e):
        for x in clap_jalra_drums:
            x.bgcolor = bgcolor_sec
            x.color = primary_color
        e.bgcolor = primary_color
        e.color = light
        page.update()
        text = e.text
        text = text.lower()
        flat.src = f"/{text}_flat.wav"
        sharp.src = f"/{text}_sharp.wav"
        flat.update()
        sharp.update()
        page.update()

    def sound_button_clicked(e):
        text = str(buttons.selected)
        text = text.lower()
        text = text.strip('{')
        text = text.strip('}')
        text = text.strip("'")
        flat.src = f"/{text}_flat.wav"
        sharp.src = f"/{text}_sharp.wav"
        flat.update()
        sharp.update()

    buttons = fl.SegmentedButton(
            show_selected_icon = False,
            selected={"jalra"},
            allow_multiple_selection=False,
            on_change = sound_button_clicked,
            segments=[
                fl.Segment(
                    value="clap",
                    label=fl.Text("Clap")),
                fl.Segment(
                    value = "jalra",
                    label=fl.Text("Jalra")),
                fl.Segment(
                    value="drums",
                    label=fl.Text("Drums"))],
            style = button_style_dark)    

        

    clap_button = fl.ElevatedButton("Clap", bgcolor = bgcolor_sec, color = primary_color ,on_click = lambda _: sound_changed(clap_button))
    jalra_button = fl.ElevatedButton("Jalra", bgcolor = primary_color, color = light, on_click = lambda _: sound_changed(jalra_button))
    drums_button = fl.ElevatedButton("Drums", bgcolor = bgcolor_sec, color = primary_color, on_click = lambda _: sound_changed(drums_button))

    clap_jalra_drums = [buttons]

    play_sound_selection = fl.Row([fl.Row([play_button]), fl.Row(clap_jalra_drums)], alignment = fl.MainAxisAlignment.SPACE_AROUND)

    page.add(Appbar,
             fl.Column([fl.Row([bpm_row], alignment = fl.MainAxisAlignment.SPACE_AROUND), 
                        volume_column,
                        play_sound_selection,
                        thalam_row,
                        default_sooladhi_selection,
                        thalam_selection_final]))
    


fl.app(target = main, assets_dir = 'assets')
    
