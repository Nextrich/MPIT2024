from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout 
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics import Rectangle
from kivy.uix.dropdown import DropDown
import sqlite3
Window.size = (428, 926)
#129307!
#Для тех, кто будет читать: я решил писать на каждой строчке, т. к. взгляд мылился при позиционировании виджетов. 
#Для каждого виджета в функциях change есть 2 условия, чтобы они не накладывались, я убираю им scale на 0, создавать и удалять их способа не нашёл(((
#Алгоритм приложил бы фоткой, да не могу, из-за этого стоп-кода и сбора презентаций чисто не успеваю.
#Встретились как-то русский, немец и американец...
class MyApp(App):
    '''public_voids = []
    def recomendation():   #Анализатор
        global public_voids

        self.addit_height_lbl.opacity = 0
        self.addit_height.opacity = 0
        self.addit_body_lbl.opacity = 0
        self.addit_body_type.opacity = 0
        self.addit_patience_lbl.opacity = 0
        self.addit_patience.opacity = 0
        self.final_reg_btn.opacity = 0
        self.addit_height.size_hint = (.0, .0)
        self.addit_body_type.size_hint = (.0, .0)
        self.addit_patience.size_hint = (.0, .0)
        self.final_reg_btn.size_hint = (.0,.0)'''

        #рост/телосложение(худой, мускулистый, полноватый)/терпение(5)
        a = int(self.addit_height.text)
        else: print('error')
        b = self.addit_body_type.text
        c = int(self.addit_patience.text)
        else: print('error')
        dbn = 'app_users_data.db'
        conn = sqlite3.connect(dbn)
        cursor = conn.cursor()
        sqlite_users = f"""INSERT INTO user_public_data(height,  body_type,  patience) VALUES ({a},  '{b}',  {c})"""
        cursor.execute(sqlite_users)
        conn.commit()
        conn.close()

	def set_bg(self, *args):
		self.root_window.bind(size=self.do_resize)
		with self.root_window.canvas.before:
			self.bg = Rectangle(source='UI\\bg.png', pos=(0,0), size=(self.root_window.size))
	
	def __init__(self):
		super().__init__()

	def on_focus(self, instance, value):
		if value and self.reg_name.text == 'Имя' or self.reg_name.text == 'Пусто':
			self.reg_name.text = ''
			self.reg_name.color = 'black'
		elif value and self.reg_email.text == 'Эл. почта' or self.reg_email.text == 'Пусто':
			self.reg_email.text = ''
			self.reg_email.color = 'black'
		elif value and self.reg_pass.text == 'Пароль' or self.reg_pass.text == 'Пароли не совпадают' or self.reg_pass.text == 'Пусто'or self.reg_pass.text == 'Неправильное имя или пароль':
			self.reg_pass.text = ''
			self.reg_pass.color = 'black'
		elif value and self.reg_pass_confirm.text == 'Пароль ещё раз' or self.reg_pass.text == 'Пароли не совпадают' or self.reg_pass_confirm.text == 'Пусто':
			self.reg_pass_confirm.text = ''
			self.reg_pass_confirm.color = 'black'

		else:
			if self.reg_name.text == '':
				if self.reg_name.text == '':
					self.reg_name.text = 'Имя'
				elif self.reg_name.text == ' ':
					a = self.reg_name.text
					self.reg_name.text = a.replace(' ', '')
			if self.reg_email.text == '':
				if self.reg_email.text == '':
					self.reg_email.text = 'Эл. почта'
				elif self.reg_email.text == ' ':
					a = self.reg_email.text
					self.reg_email.text = a.replace(' ', '')
			if self.reg_pass.text == '':
				if self.reg_pass.text == '':
					self.reg_pass.text = 'Пароль'
				elif self.reg_pass.text == ' ':
					a = self.reg_pass.text
					self.reg_pass.text = a.replace(' ', '')
			if self.reg_pass_confirm.text == '':
				if self.reg_pass_confirm.text == '':
					self.reg_pass_confirm.text = 'Пароль ещё раз'
				elif self.reg_pass_confirm.text == ' ':
					a = self.reg_pass_confirm.text
					self.reg_pass_confirm.text = a.replace(' ', '')

	def do_resize(self, *args):
		self.bg.size = self.root_window.size
	
	def login_account(self, instance):
		if self.reg_name.text == '' or self.reg_name.text == 'Пусто':	#name(login)
			self.reg_name.text = 'Пусто'
		elif self.reg_pass.text == '' or self.reg_pass.text == 'Пусто':	#pass(login)
			self.reg_pass.text = 'Пусто'

		elif self.reg_name.text != '' and self.reg_pass != '':
			dbn = 'app_users_data.db'
			conn = sqlite3.connect(dbn)
			cursor = conn.cursor()
			sqlite_names = """SELECT name FROM user_private_data"""
			cursor.execute(sqlite_names)
			sqlite_names = cursor.fetchall()
			sqlite_pass = """SELECT password FROM user_private_data"""
			cursor.execute(sqlite_pass)
			sqlite_pass = cursor.fetchall()
			conn.commit()
			conn.close()

			key = False
			name = self.reg_name.text.replace(' ', '')
			password = self.reg_pass.text.replace(' ', '')
			for a in sqlite_names:
				print(a[0])
				if a[0] == name:
					for b in sqlite_pass:
						if password == b[0]:
							key = True
							self.reg_lbl.opacity =0
							self.reg_name.opacity =0
							self.reg_email.opacity =0
							self.reg_pass.opacity =0
							self.reg_pass_confirm.opacity =0
							self.next_reg_btn.opacity =0
							self.reg_lbl.size_hint=(.0, .0)
							self.reg_lbl.size_hint = (.0, .0)
							self.reg_name.size_hint = (.0, .0)
							self.reg_pass.size_hint = (.0, .0)
							self.reg_email.size_hint = (.0, .0)
							self.reg_pass_confirm.size_hint = (.0, .0)
							self.next_reg_btn.size_hint = (.0, .0)

							self.welcome.opacity =1
							self.card_salan.opacity =1
							self.card_ugus.opacity =1
							self.card_teeth.opacity =1
							self.card_megalits.opacity =1
							self.card_shoria.opacity =1
							self.small_full_map.opacity =1

				if key == False:
					self.reg_pass.text  ='Неправильное имя или пароль'

	def register_accounts(self, instance):
		self.reg_name.text = self.reg_name.text.replace(' ', '')
		self.reg_email.text = self.reg_email.text.replace(' ', '')
		if self.reg_pass.text != self.reg_pass_confirm.text:

			self.reg_pass_confirm.color = 'red'
			self.reg_pass.color = 'red'
			self.reg_pass_confirm.text = 'Пароли не совпадают'
			self.reg_pass.text = 'Пароли не совпадают'
			self.reg_pass_confirm.color = 'black'
			self.reg_pass.color = 'black'

		elif self.reg_name.text == '' or self.reg_name.text == 'Пусто':	#name(login)
			self.reg_name.text = 'Пусто'
		elif self.reg_pass.text == '' or self.reg_pass.text == 'Пусто':	#pass(login)
			self.reg_pass.text = 'Пусто'
		elif self.reg_email.text == '' or self.reg_email.text == 'Пусто': #email(register)
			self.reg_email.text = 'Пусто'
		elif self.reg_pass_confirm.text == '' or self.reg_pass_confirm.text == 'Пусто': #pass_confirm(register)
			self.reg_pass_confirm.text = 'Пусто'

		else: #INSERT INTO user_private_data(name,  email,  password) VALUES ('Алёна',  'skudarnovaalena0@gmail.com',  'skudarnova2009')
			dbn = 'app_users_data.db'
			conn = sqlite3.connect(dbn)
			cursor = conn.cursor()
			sqlite_users = f"""INSERT INTO user_private_data(name,  email,  password) VALUES ('{self.reg_name.text}',  '{self.reg_email.text}',  '{self.reg_pass.text}')"""
			cursor.execute(sqlite_users)
			conn.commit()
			conn.close()
			file = open('local.txt', "w+")
			file.write(f'username:{self.reg_name.text};email:{self.reg_email.text};password:{self.reg_pass.text}')
			file.close()
			self.reg_lbl.opacity =0
			self.reg_name.opacity =0
			self.reg_email.opacity =0
			self.reg_pass.opacity =0
			self.reg_pass_confirm.opacity =0
			self.next_reg_btn.opacity =0
			self.reg_lbl.size_hint = (.0, .0)
			self.reg_lbl.size_hint = (.0, .0)
			self.reg_name.size_hint = (.0, .0)
			self.reg_pass.size_hint = (.0, .0)
			self.reg_email.size_hint = (.0, .0)
			self.reg_pass_confirm.size_hint = (.0, .0)
			self.next_reg_btn.size_hint = (.0, .0)


			self.welcome.opacity =1
			self.card_salan.opacity =1
			self.card_ugus.opacity =1
			self.card_teeth.opacity =1
			self.card_megalits.opacity =1
			self.card_shoria.opacity =1
			self.small_full_map.opacity =1

	def salan_map_open(self, instance):
		self.salan_map.opacity = 1
		self.salan_info_text.size_hint = (1,1)

	def ugus_map_open(self, instance):
		self.ugus_map.opacity = 1
		self.ugus_info_text.size_hint = (1,1)

	def teeth_map_open(self, instance):
		self.teeth_map.opacity = 1
		self.teeth_info_text.size_hint = (1,1)

	def megalits_map_open(self, instance):
		self.megalits_map.opacity = 1
		self.megalits_info_text.size_hint = (1,1)

	def shoria_map_open(self, instance):
		self.shoria_map.opacity = 1
		self.shoria_info_text.size_hint = (1,1)

	def map_close(self, instance):
		self.salan_map.opacity = 0
		self.salan_info_text.size_hint = (.0,.0)

		self.ugus_map.opacity = 0
		self.ugus_info_text.size_hint = (.0,.0)

		self.teeth_map.opacity = 0
		self.teeth_info_text.size_hint = (.0,.0)

		self.megalits_map.opacity = 0
		self.megalits_info_text.size_hint = (.0,.0)

		self.shoria_map.opacity = 0
		self.shoria_info_text.size_hint = (.0,.0)

	def change_reg(self,instance): #change как продавец в пятёрочке - берёт ваше и меняет на аналогичоне, но с большей стоимостью(ха-ха-ха)
		self.logo.opacity=0
		self.about_lbl.opacity = 0
		self.about_text.opacity = 0
		self.register.opacity = 0
		self.if_register.opacity = 0
		self.login.opacity = 0
		self.logo.size_hint =(.0,.0)
		self.about_lbl.size_hint = (.0, .0)
		self.about_text.size_hint = (.0, .0)
		self.register.size_hint = (.0, .0)
		self.if_register.size_hint = (.0, .0)
		self.login.size_hint = (.0, .0)

		self.reg_lbl.opacity =1
		self.reg_name.opacity =1
		self.reg_email.opacity =1
		self.reg_pass.opacity =1
		self.reg_pass_confirm.opacity =1
		self.next_reg_btn.opacity =1

		self.reg_lbl.text = 'Регистрация'
		self.next_reg_btn.bind(on_press=self.register_accounts)
	
	def change_log(self, instance):
		self.logo.opacity=0
		self.about_lbl.opacity =0
		self.about_text.opacity =0
		self.register.opacity =0
		self.if_register.opacity =0
		self.login.opacity =0
		self.logo.size_hint = (.0,.0)
		self.about_lbl.size_hint =(.0,.0)
		self.about_text.size_hint =(.0,.0)
		self.register.size_hint =(.0,.0)
		self.if_register.size_hint =(.0,.0)
		self.login.size_hint =(.0,.0)

		self.reg_lbl.opacity =1
		self.reg_name.opacity =1
		self.reg_pass.opacity =1
		self.next_reg_btn.opacity =1

		self.reg_lbl.text = 'Вход'
		self.next_reg_btn.bind(on_press=self.login_account)

	def change_welcome(self, instance):
		self.reg_lbl.opacity =0
		self.reg_name.opacity =0
		self.reg_email.opacity =0
		self.reg_pass.opacity =0
		self.reg_pass_confirm.opacity =0
		self.next_reg_btn.opacity =0
		#self.logo.size_hint=(.0, .0)
		self.reg_lbl.size_hint = (.0, .0)
		self.reg_lbl.size_hint = (.0, .0)
		self.reg_name.size_hint = (.0, .0)
		self.reg_pass.size_hint = (.0, .0)
		self.reg_email.size_hint = (.0, .0)
		self.reg_pass_confirm.size_hint = (.0, .0)
		self.next_reg_btn.size_hint = (.0, .0)
		#salan
		self.salan_img.opacity =0
		self.salan_info_img.opacity = 0
		self.salan_info_lbl.opacity = 0
		self.salan_mini_img.opacity = 0
		self.salan_info_text.opacity = 0
		self.back_btn.opacity = 0
		self.salan_go_lbl.opacity = 0
		self.salan_go_btn.opacity = 0
		self.salan_img.size_hint = (.0, .0)
		self.salan_info_img.size_hint = (.0, .0)
		self.salan_mini_img.size_hint = (.0, .0)
		self.back_btn.size_hint = (.0, .0)
		#ugus
		self.ugus_img.opacity =0
		self.ugus_info_img.opacity = 0
		self.ugus_info_lbl.opacity = 0
		self.ugus_mini_img.opacity = 0
		self.ugus_info_text.opacity = 0
		self.back_btn.opacity = 0
		self.ugus_go_lbl.opacity = 0
		self.ugus_go_btn.opacity = 0
		self.ugus_img.size_hint = (.0, .0)
		self.ugus_info_img.size_hint = (.0, .0)
		self.ugus_mini_img.size_hint = (.0, .0)
		self.back_btn.size_hint = (.0, .0)
		#teeth
		self.teeth_img.opacity =0
		self.teeth_info_img.opacity = 0
		self.teeth_info_lbl.opacity = 0
		self.teeth_mini_img.opacity = 0
		self.teeth_info_text.opacity = 0
		self.teeth_go_lbl.opacity = 0
		self.teeth_go_btn.opacity = 0
		self.back_btn.opacity = 0
		self.teeth_img.size_hint = (.0, .0)
		self.teeth_info_img.size_hint = (.0, .0)
		self.teeth_mini_img.size_hint = (.0, .0)
		self.back_btn.size_hint = (.0, .0)
		#megalits
		self.megalits_img.opacity =0
		self.megalits_info_img.opacity = 0
		self.megalits_info_lbl.opacity = 0
		self.megalits_mini_img.opacity = 0
		self.megalits_info_text.opacity = 0
		self.megalits_go_lbl.opacity = 0
		self.megalits_go_btn.opacity = 0
		self.back_btn.opacity = 0
		self.megalits_img.size_hint = (.0, .0)
		self.megalits_info_img.size_hint = (.0, .0)
		self.megalits_mini_img.size_hint = (.0, .0)
		self.back_btn.size_hint = (.0, .0)
		#shoria
		self.shoria_img.opacity =0
		self.shoria_info_img.opacity = 0
		self.shoria_info_lbl.opacity = 0
		self.shoria_mini_img.opacity = 0
		self.shoria_info_text.opacity = 0
		self.back_btn.opacity = 0
		self.shoria_go_lbl.opacity = 0
		self.shoria_go_btn.opacity = 0
		self.shoria_img.size_hint = (.0, .0)
		self.shoria_info_img.size_hint = (.0, .0)
		self.shoria_mini_img.size_hint = (.0, .0)
		self.back_btn.size_hint = (.0, .0)

		self.welcome.opacity =1
		self.card_salan.opacity =1
		self.card_ugus.opacity =1
		self.card_teeth.opacity =1
		self.card_megalits.opacity =1
		self.card_shoria.opacity =1
		self.small_full_map.opacity =1
		self.welcome.size_hint =(.7,.7)
		self.card_salan.size_hint = (1.0, .12)
		self.card_ugus.size_hint = (1.0, .12)
		self.card_teeth.size_hint = (1.0, .12)
		self.card_megalits.size_hint = (1.0, .12)
		self.card_shoria.size_hint = (1.0, .12)
		self.small_full_map.size_hint = (1.0, .25)

	def change_salan(self,instance):
		self.welcome.opacity = 0
		self.card_salan.opacity = 0
		self.card_ugus.opacity = 0
		self.card_teeth.opacity = 0
		self.card_megalits.opacity = 0
		self.card_shoria.opacity = 0
		self.small_full_map.opacity = 0
		self.welcome.size_hint = (.0, .0)
		self.card_salan.size_hint = (.0, .0)
		self.card_ugus.size_hint = (.0, .0)
		self.card_teeth.size_hint = (.0, .0)
		self.card_megalits.size_hint = (.0, .0)
		self.card_shoria.size_hint = (.0, .0)
		self.small_full_map.size_hint = (.0, .0)

		self.salan_img.opacity = 1
		self.salan_info_img.opacity = 1
		self.salan_info_text.opacity = 1
		self.salan_info_lbl.opacity = 1
		self.salan_mini_img.opacity = 1
		self.salan_go_lbl.opacity = 1
		self.salan_go_btn.opacity = 1
		self.back_btn.opacity = 1
		self.salan_img.size_hint = (.9, .25)
		self.salan_info_img.size_hint = (.4, .2)
		self.salan_mini_img.size_hint =(.3, .1)
		self.back_btn.size_hint = (.3, .1)

	def change_ugus(self,instance):
		self.welcome.opacity = 0
		self.card_salan.opacity = 0
		self.card_ugus.opacity = 0
		self.card_teeth.opacity = 0
		self.card_megalits.opacity = 0
		self.card_shoria.opacity = 0
		self.small_full_map.opacity = 0
		self.welcome.size_hint = (.0, .0)
		self.card_salan.size_hint = (.0, .0)
		self.card_ugus.size_hint = (.0, .0)
		self.card_teeth.size_hint = (.0, .0)
		self.card_megalits.size_hint = (.0, .0)
		self.card_shoria.size_hint = (.0, .0)
		self.small_full_map.size_hint = (.0, .0)

		self.ugus_img.opacity = 1
		self.ugus_info_img.opacity = 1
		self.ugus_info_text.opacity = 1
		self.ugus_info_lbl.opacity = 1
		self.ugus_mini_img.opacity = 1
		self.ugus_go_lbl.opacity = 1
		self.ugus_go_btn.opacity = 1
		self.back_btn.opacity = 1
		self.ugus_img.size_hint = (.9, .25)
		self.ugus_info_img.size_hint = (.4, .2)
		self.ugus_mini_img.size_hint =(.3, .1)
		self.back_btn.size_hint = (.3, .1)

	def change_teeth(self,instance):
		self.welcome.opacity = 0
		self.card_salan.opacity = 0
		self.card_ugus.opacity = 0
		self.card_teeth.opacity = 0
		self.card_megalits.opacity = 0
		self.card_shoria.opacity = 0
		self.small_full_map.opacity = 0
		self.welcome.size_hint = (.0, .0)
		self.card_salan.size_hint = (.0, .0)
		self.card_ugus.size_hint = (.0, .0)
		self.card_teeth.size_hint = (.0, .0)
		self.card_megalits.size_hint = (.0, .0)
		self.card_shoria.size_hint = (.0, .0)
		self.small_full_map.size_hint = (.0, .0)

		self.teeth_img.opacity = 1
		self.teeth_info_img.opacity = 1
		self.teeth_info_text.opacity = 1
		self.teeth_info_lbl.opacity = 1
		self.teeth_mini_img.opacity = 1
		self.teeth_go_lbl.opacity = 1
		self.teeth_go_btn.opacity = 1
		self.back_btn.opacity = 1
		self.teeth_img.size_hint = (.9, .25)
		self.teeth_info_img.size_hint = (.4, .2)
		self.teeth_mini_img.size_hint =(.3, .1)
		self.back_btn.size_hint = (.3, .1)

	def change_megalits(self,instance):
		self.welcome.opacity = 0
		self.card_salan.opacity = 0
		self.card_ugus.opacity = 0
		self.card_teeth.opacity = 0
		self.card_megalits.opacity = 0
		self.card_shoria.opacity = 0
		self.small_full_map.opacity = 0
		self.welcome.size_hint = (.0, .0)
		self.card_salan.size_hint = (.0, .0)
		self.card_ugus.size_hint = (.0, .0)
		self.card_teeth.size_hint = (.0, .0)
		self.card_megalits.size_hint = (.0, .0)
		self.card_shoria.size_hint = (.0, .0)
		self.small_full_map.size_hint = (.0, .0)

		self.megalits_img.opacity = 1
		self.megalits_info_img.opacity = 1
		self.megalits_info_text.opacity = 1
		self.megalits_info_lbl.opacity = 1
		self.megalits_mini_img.opacity = 1
		self.megalits_go_lbl.opacity = 1
		self.megalits_go_btn.opacity = 1
		self.back_btn.opacity = 1
		self.megalits_img.size_hint = (.9, .25)
		self.megalits_info_img.size_hint = (.4, .2)
		self.megalits_mini_img.size_hint =(.3, .1)
		self.back_btn.size_hint = (.3, .1)

	def change_shoria(self,instance):
		self.welcome.opacity = 0
		self.card_salan.opacity = 0
		self.card_ugus.opacity = 0
		self.card_teeth.opacity = 0
		self.card_megalits.opacity = 0
		self.card_shoria.opacity = 0
		self.small_full_map.opacity = 0
		self.welcome.size_hint = (.0, .0)
		self.card_salan.size_hint = (.0, .0)
		self.card_ugus.size_hint = (.0, .0)
		self.card_teeth.size_hint = (.0, .0)
		self.card_megalits.size_hint = (.0, .0)
		self.card_shoria.size_hint = (.0, .0)
		self.small_full_map.size_hint = (.0, .0)

		self.shoria_img.opacity = 1
		self.shoria_info_img.opacity = 1
		self.shoria_info_text.opacity = 1
		self.shoria_info_lbl.opacity = 1
		self.shoria_mini_img.opacity = 1
		self.shoria_go_lbl.opacity = 1
		self.shoria_go_btn.opacity = 1
		self.back_btn.opacity = 1
		self.shoria_img.size_hint = (.9, .25)
		self.shoria_info_img.size_hint = (.4, .2)
		self.shoria_mini_img.size_hint =(.3, .1)
		self.back_btn.size_hint = (.3, .1)


	def build(self):
		Clock.schedule_once(self.set_bg, 0)
		buttons_layout = RelativeLayout()
		#image = Image(source='logo.jpg')
		#Я знаю, что Югус и Шория как минимум с заглавной буквы, но так неудобно😭😭😭(плак-плак)
		#back_arrow находится в блоке с карточкой Салана

		#maps------------------------------------------------------------------------------------------------------------------------------------------
		self.salan_map = Button(size_hint =(.0, .0), background_normal='maps\\salan_map.png', opacity=0)
		self.ugus_map = Button(size_hint =(.0, .0), background_normal='maps\\ugus_map.png', opacity=0)
		self.teeth_map = Button(size_hint =(.0, .0), background_normal='maps\\teeth_map.png', opacity=0)
		self.megalits_map = Button(size_hint =(.0, .0), background_normal='maps\\megalits_map.png', opacity=0)
		self.shoria_map = Button(size_hint =(.0, .0), background_normal='maps\\shoria_map.png', opacity=0)

		self.salan_map.bind(on_press=self.map_close)
		self.ugus_map.bind(on_press=self.map_close)
		self.teeth_map.bind(on_press=self.map_close)
		self.megalits_map.bind(on_press=self.map_close)
		self.shoria_map.bind(on_press=self.map_close)

		#front----------------------------------------------------------------------------------------------------------------------------------------
		buttons_layout.add_widget(self.megalits_map)
		buttons_layout.add_widget(self.ugus_map)
		buttons_layout.add_widget(self.teeth_map)
		buttons_layout.add_widget(self.salan_map)
		buttons_layout.add_widget(self.shoria_map)

		#card_shoria-----------------------------------------------------------------------------------------------------------------------------------
		self.shoria_img = Button(background_normal='places\\shoria\\shoria.png', pos_hint ={'center_x':.5}, size_hint =(.9, .25), pos =(214.0, 850.0), opacity=0)
		self.shoria_info_img = Button(background_normal='places\\shoria\\shoria_info.png', pos_hint ={'center_x':.25}, size_hint =(.4, .2), pos =(214.0, 600.0), opacity=0)
		self.shoria_info_text = Label(text='В Шории особенная атмосфера красоты тайги – пожалуй, самой суровой и неприступной в Сибири. Небоскрёбы кедров и сосен, море тайги градиентов в небо, сибирские джунгли и звонкие горные реки. Здесь чувствуешь себя гостем и невольно следуешь закону тайги.', pos_hint={'center_x':.75}, size_hint =(.1, .1), pos =(214.0, 660.0), text_size=(250, None), opacity=0)
		self.shoria_info_lbl = Label(text='В шорских горах у вершин\nНа одной стороне лежит снег,\nНа другой - цветут цветы.Так и в жизни:Одной рукою ты держишь цветы,\nА в другой – слезою тающий снег.',text_size=(250, None), pos_hint ={'center_x':.35}, size_hint =(.9, .22), pos =(214.0, 375.0), opacity=0)
		self.shoria_mini_img = Button(background_normal='places\\shoria\\shoria_mini_img.png', pos_hint ={'center_x':.82}, size_hint =(.3, .1), pos =(214.0, 440.0), opacity=0)
		self.shoria_go_lbl = Label(text="Маршрут до места ", pos_hint ={'center_x':.25}, size_hint =(.3, .1), pos =(214.0, 300.0), opacity=0)
		self.shoria_go_btn = Button(text="здесь ", pos_hint ={'center_x':.45}, size_hint =(.1, .1), background_normal='UI\\squre.jpg', pos =(214.0, 300.0), opacity=0, bold=True, color='yellow')

		self.shoria_go_btn.bind(on_press=self.shoria_map_open)
		#front----------------------------------------------------------------------------------------------------------------------------------------
		buttons_layout.add_widget(self.shoria_img)
		buttons_layout.add_widget(self.shoria_info_img)
		buttons_layout.add_widget(self.shoria_info_text)
		buttons_layout.add_widget(self.shoria_info_lbl)
		buttons_layout.add_widget(self.shoria_mini_img)
		buttons_layout.add_widget(self.shoria_go_lbl)
		buttons_layout.add_widget(self.shoria_go_btn)

		#card_megalits-----------------------------------------------------------------------------------------------------------------------------------
		self.megalits_img = Button(background_normal='places\\megalits\\megalits.jpeg', pos_hint ={'center_x':.5}, size_hint =(.9, .25), pos =(214.0, 850.0), opacity=0)
		self.megalits_info_img = Button(background_normal='places\\megalits\\megalits_info.png', pos_hint ={'center_x':.25}, size_hint =(.4, .2), pos =(214.0, 600.0), opacity=0)
		self.megalits_info_text = Label(text='Скалы идеальной формы настолько похожи на инопланетный космический корабль, что придется изучить их как следует. Окружающая красота и энергетика доброй тайги накроет вас с головой.', pos_hint={'center_x':.75}, size_hint =(.1, .1), pos =(214.0, 660.0), text_size=(250, None), opacity=0)
		self.megalits_info_lbl = Label(text='ЭТО СТОИТ УВИДЕТЬ\nЛегендарные Мегалиты привлекают тысячи людей со всей России своими секретами, легендами и невероятной энергетикой',text_size=(250, None), pos_hint ={'center_x':.35}, size_hint =(.9, .22), pos =(214.0, 375.0), opacity=0)
		self.megalits_mini_img = Button(background_normal='places\\megalits\\megalits_mini_img.png', pos_hint ={'center_x':.82}, size_hint =(.3, .1), pos =(214.0, 440.0), opacity=0)
		self.megalits_go_lbl = Label(text="Маршрут до места ", pos_hint ={'center_x':.25}, size_hint =(.3, .1), pos =(214.0, 300.0), opacity=0)
		self.megalits_go_btn = Button(text="здесь ", pos_hint ={'center_x':.45}, size_hint =(.1, .1), background_normal='UI\\squre.jpg', pos =(214.0, 300.0), opacity=0, bold=True, color='yellow')

		self.megalits_go_btn.bind(on_press=self.megalits_map_open)

		#front----------------------------------------------------------------------------------------------------------------------------------------
		buttons_layout.add_widget(self.megalits_img)
		buttons_layout.add_widget(self.megalits_info_img)
		buttons_layout.add_widget(self.megalits_info_text)
		buttons_layout.add_widget(self.megalits_info_lbl)
		buttons_layout.add_widget(self.megalits_mini_img)
		buttons_layout.add_widget(self.megalits_go_lbl)
		buttons_layout.add_widget(self.megalits_go_btn)

		#card_teeth-----------------------------------------------------------------------------------------------------------------------------------
		self.teeth_img = Button(background_normal='places\\teeth\\teeth.jpeg', pos_hint ={'center_x':.5}, size_hint =(.9, .25), pos =(214.0, 850.0), opacity=0)
		self.teeth_info_img = Button(background_normal='places\\teeth\\teeth_info.png', pos_hint ={'center_x':.25}, size_hint =(.4, .2), pos =(214.0, 600.0), opacity=0)
		self.teeth_info_text = Label(text='Туристическая мекка с десятками маршрутов по главным вершинам Шории, горным озёрам и бурным рекам летом и рай фрирайда по полям бескрайнего пухляка зимой.', pos_hint={'center_x':.75}, size_hint =(.1, .1), pos =(214.0, 660.0), text_size=(200, None), opacity=0)
		self.teeth_info_lbl = Label(text='2OOкм - туристских троп\n30000 - поток туристов на Поднебесных\n2045м - Высота пика Большой Зуб',text_size=(250, None), pos_hint ={'center_x':.35}, size_hint =(.9, .22), pos =(214.0, 375.0), opacity=0)
		self.teeth_mini_img = Button(background_normal='places\\teeth\\teeth_mini_img.png', pos_hint ={'center_x':.82}, size_hint =(.3, .1), pos =(214.0, 440.0), opacity=0)
		self.teeth_go_lbl = Label(text="Маршрут до места ", pos_hint ={'center_x':.25}, size_hint =(.3, .1), pos =(214.0, 300.0), opacity=0)
		self.teeth_go_btn = Button(text="здесь ", pos_hint ={'center_x':.45}, size_hint =(.1, .1), background_normal='UI\\squre.jpg', pos =(214.0, 300.0), opacity=0, bold=True, color='yellow')

		self.teeth_go_btn.bind(on_press=self.teeth_map_open)

		#front----------------------------------------------------------------------------------------------------------------------------------------
		buttons_layout.add_widget(self.teeth_img)
		buttons_layout.add_widget(self.teeth_info_img)
		buttons_layout.add_widget(self.teeth_info_text)
		buttons_layout.add_widget(self.teeth_info_lbl)
		buttons_layout.add_widget(self.teeth_mini_img)
		buttons_layout.add_widget(self.teeth_go_lbl)
		buttons_layout.add_widget(self.teeth_go_btn)

		#card_ugus-----------------------------------------------------------------------------------------------------------------------------------
		self.ugus_img = Button(background_normal='places\\ugus\\ugus.jpeg', pos_hint ={'center_x':.5}, size_hint =(.9, .25), pos =(214.0, 850.0), opacity=0)
		self.ugus_info_img = Button(background_normal='places\\ugus\\ugus_info.png', pos_hint ={'center_x':.25}, size_hint =(.4, .2), pos =(214.0, 600.0), opacity=0)
		self.ugus_info_text = Label(text='Гора Югус — первый в Сибири горнолыжный комплекс. Его история началась в 1962 году, когда началось строительство первых трасс и образовалась первая спортивная школа.', pos_hint={'center_x':.72}, size_hint =(.1, .1), pos =(214.0, 660.0), text_size=(250, None), opacity=0)
		self.ugus_info_lbl = Label(text='310м - перепад высот на горе\nдо 1400м - протяженность трасс\n25 км - длина тропы терренкур', text_size=(250, None), pos_hint ={'center_x':.35}, size_hint =(.9, .22), pos =(214.0, 375.0), opacity=0)
		self.ugus_mini_img = Button(background_normal='places\\ugus\\ugus_mini_img.png', pos_hint ={'center_x':.82}, size_hint =(.3, .1), pos =(214.0, 440.0), opacity=0)
		self.ugus_go_lbl = Label(text="Маршрут до места ", pos_hint ={'center_x':.25}, size_hint =(.3, .1), pos =(214.0, 300.0), opacity=0)
		self.ugus_go_btn = Button(text="здесь ", pos_hint ={'center_x':.45}, size_hint =(.1, .1), background_normal='UI\\squre.jpg', pos =(214.0, 300.0), opacity=0, bold=True, color='yellow')

		self.ugus_go_btn.bind(on_press=self.ugus_map_open)

		#front----------------------------------------------------------------------------------------------------------------------------------------
		buttons_layout.add_widget(self.ugus_img)
		buttons_layout.add_widget(self.ugus_info_img)
		buttons_layout.add_widget(self.ugus_info_text)
		buttons_layout.add_widget(self.ugus_info_lbl)
		buttons_layout.add_widget(self.ugus_mini_img)
		buttons_layout.add_widget(self.ugus_go_lbl)
		buttons_layout.add_widget(self.ugus_go_btn)

		#card_salan-----------------------------------------------------------------------------------------------------------------------------------
		self.salan_img = Button(background_normal='places\\salan\\salan.jpeg', pos_hint ={'center_x':.5}, size_hint =(.9, .25), pos =(214.0, 850.0), opacity=0)
		self.salan_info_img = Button(background_normal='places\\salan\\salan_info.png', pos_hint ={'center_x':.25}, size_hint =(.4, .2), pos =(214.0, 600.0), opacity=0)
		self.salan_info_text = Label(text='Одна из 20 гор в мире с идеальными для горных лыж склонами размером с район города потрясает своими масштабами. Хрустальная горная Теба и дизайнерские дырявые камни — отличное дополнение для тех, кто ищет новые места для приключений', pos_hint={'center_x':.75}, size_hint =(.1, .1), pos =(214.0, 660.0), text_size=(250, None), opacity=0)
		self.salan_info_lbl = Label(text='950м-Перепад высот Чёрного Салана\n5км-Длина фрирайд-спусков\n39км-Длина реки Теба', pos_hint ={'center_x':.35}, size_hint =(.05, .22), pos =(214.0, 375.0), opacity=0)
		self.salan_mini_img = Button(background_normal='places\\salan\\salan_mini_img.png', pos_hint ={'center_x':.82}, size_hint =(.3, .1), pos =(214.0, 440.0), opacity=0)
		self.salan_go_lbl = Label(text="Маршрут до места ", pos_hint ={'center_x':.25}, size_hint =(.3, .1), pos =(214.0, 300.0), opacity=0)
		self.salan_go_btn = Button(text="здесь ", pos_hint ={'center_x':.45}, size_hint =(.1, .1), background_normal='UI\\squre.jpg', pos =(214.0, 300.0), opacity=0, bold=True, color='yellow')
		self.back_btn=Button(background_normal='UI\\back_arrow.png', pos_hint={'center_x':.15}, size_hint=(.3, .1), pos=(214.0, 5.0), opacity=0)

		self.back_btn.bind(on_press=self.change_welcome)
		self.salan_go_btn.bind(on_press=self.salan_map_open)

		#front----------------------------------------------------------------------------------------------------------------------------------------
		buttons_layout.add_widget(self.salan_img)
		buttons_layout.add_widget(self.salan_info_img)
		buttons_layout.add_widget(self.salan_info_text)
		buttons_layout.add_widget(self.salan_info_lbl)
		buttons_layout.add_widget(self.salan_mini_img)
		buttons_layout.add_widget(self.back_btn)
		buttons_layout.add_widget(self.salan_go_lbl)
		buttons_layout.add_widget(self.salan_go_btn)

		#account_list---------------------------------------------------------------------------------------------------------------------------------
		self.welcome = Label(text='Междуреченский турист', pos_hint ={'center_x':.5}, pos =(214.0, 900.0), size_hint =(.7, .4), opacity=0)
		self.card_salan = Button(pos_hint ={'center_x':.5}, background_normal='UI\\salan.png', size_hint =(1.0, .12), pos =(214.0, 850.0), border=(10, 10, 10, 10), opacity=0)
		self.card_ugus = Button(pos_hint ={'center_x':.5}, background_normal='UI\\Ugus.png', size_hint =(1.0, .12), pos =(214.0, 700.0), border=(10, 10, 10, 10), opacity=0)
		self.card_teeth = Button(pos_hint ={'center_x':.5}, background_normal='UI\\teeth.png', size_hint =(1.0, .12), pos =(214.0, 550.0), border=(10, 10, 10, 10), opacity=0)
		self.card_megalits = Button(pos_hint ={'center_x':.5}, background_normal='UI\\megalits.png', size_hint =(1.0, .12), pos =(214.0, 400.0), border=(10, 10, 10, 10), opacity=0)
		self.card_shoria = Button(pos_hint ={'center_x':.5}, background_normal='UI\\Shoria.png', size_hint =(1.0, .12), pos =(214.0, 250.0), border=(10, 10, 10, 10), opacity=0)
		self.small_full_map = Button(pos_hint ={'center_x':.5}, background_normal='UI\\map_mini.png', size_hint =(1.0, .25), pos =(214.0, 10.0), border=(10, 10, 10, 10), opacity=0)

		self.card_salan.bind(on_press=self.change_salan)
		self.card_ugus.bind(on_press=self.change_ugus)
		self.card_teeth.bind(on_press=self.change_teeth)
		self.card_megalits.bind(on_press=self.change_megalits)
		self.card_shoria.bind(on_press=self.change_shoria)

		#front----------------------------------------------------------------------------------------------------------------------------------------
		buttons_layout.add_widget(self.welcome)
		buttons_layout.add_widget(self.card_salan)
		buttons_layout.add_widget(self.card_ugus)
		buttons_layout.add_widget(self.card_teeth)
		buttons_layout.add_widget(self.card_megalits)
		buttons_layout.add_widget(self.card_shoria)
		buttons_layout.add_widget(self.small_full_map)

        #register_form_public------------------------------------------------------------------------------------------------------------------------
        self.addit_height_lbl = Label(text='Укажите возраст:(только цифры)', bold=True, pos_hint ={'center_x':.5}, size_hint =(.7, .4), pos =(214.0, 425.0), opacity=0)
        self.addit_height = TextInput(size_hint =(.7, .03), multiline = False, pos =(214.0, 570.0), pos_hint ={'center_x':.5}, text='Имя', opacity=0)
        self.addit_body_lbl = Label(text='Укажите телосложение(худой, мускулистый, полноватый)', bold=True, pos_hint ={'center_x':.5}, size_hint =(.7, .4), pos =(214.0, 425.0), opacity=0)
        self.addit_body_type = TextInput(size_hint =(.7, .03), pos =(214.0, 510.0), multiline = False, pos_hint ={'center_x':.5}, text='Эл. почта', opacity=0
        self.addit_patience_lbl = Label(text='Укажите уровень терпения (от 1 до 5):', bold=True, pos_hint ={'center_x':.5}, size_hint =(.7, .4), pos =(214.0, 425.0), opacity=0)
        self.addit_patience = TextInput(size_hint =(.7, .03), pos =(214.0, 450.0), multiline = False, pos_hint ={'center_x':.5}, text='Пароль', opacity=0)
        self.final_reg_btn = Button(pos_hint ={'center_x':.5}, background_normal='UI\\next.png', size_hint =(.55, .1), pos =(214.0, 250.0), opacity=0)

        #front----------------------------------------------------------------------------------------------------------------------------------------
        buttons_layout.add_widget(self.reg_lbl)
        buttons_layout.add_widget(self.reg_name)
        buttons_layout.add_widget(self.reg_email)
        buttons_layout.add_widget(self.reg_pass)
        buttons_layout.add_widget(self.reg_pass_confirm)
        buttons_layout.add_widget(self.final_reg_btn)

		#register_form_private-------------------------------------------------------------------------------------------------------------------------
		self.reg_lbl = Label(text='Регистрация', bold=True, pos_hint ={'center_x':.5}, size_hint =(.7, .4), pos =(214.0, 425.0), opacity=0)
		self.reg_name = TextInput(size_hint =(.7, .03), multiline = False, pos =(214.0, 570.0), pos_hint ={'center_x':.5}, text='Имя', opacity=0)
		self.reg_email = TextInput(size_hint =(.7, .03), pos =(214.0, 510.0), multiline = False, pos_hint ={'center_x':.5}, text='Эл. почта', opacity=0)
		self.reg_pass = TextInput(size_hint =(.7, .03), pos =(214.0, 450.0), multiline = False, pos_hint ={'center_x':.5}, text='Пароль', opacity=0)
		self.reg_pass_confirm = TextInput(size_hint =(.7, .03), pos =(214.0, 390.0), multiline = False, pos_hint ={'center_x':.5}, text='Пароль ещё раз', opacity=0)
		self.next_reg_btn = Button(pos_hint ={'center_x':.5}, background_normal='UI\\next.png', size_hint =(.55, .1), pos =(214.0, 250.0), opacity=0)

		self.reg_name.bind(focus=self.on_focus)
		self.reg_email.bind(focus=self.on_focus)
		self.reg_pass.bind(focus=self.on_focus)
		self.reg_pass_confirm.bind(focus=self.on_focus)

		#front----------------------------------------------------------------------------------------------------------------------------------------
		buttons_layout.add_widget(self.reg_lbl)
		buttons_layout.add_widget(self.reg_name)
		buttons_layout.add_widget(self.reg_email)
		buttons_layout.add_widget(self.reg_pass)
		buttons_layout.add_widget(self.reg_pass_confirm)
		buttons_layout.add_widget(self.next_reg_btn)

		#first_page-----------------------------------------------------------------------------------------------------------------------------------
		self.logo = Button(text='', color='black', pos_hint ={'center_x':.5}, background_normal='UI\\logo.jpg', size_hint =(.7, .4), pos =(214.0, 675.0), opacity=1)
		self.about_lbl = Label(text='О нас:', bold=True, size_hint =(.7, .4), pos =(214.0, 385.0), pos_hint ={'center_x':.5})   #, background_normal='btn_bg.png')
		self.about_text = Label(text='Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit. Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit.', text_size=(350, None), size_hint =(.7, .4), pos =(214.0, 325.0), pos_hint ={'center_x':.5})
		self.if_register = Label(text='Уже есть аккаунт?', size_hint =(.7, .4), pos =(214.0, -5.0), pos_hint ={'center_x':.425})
		self.login = Button(text='Вход', bold=True, size_hint =(.1, .01), pos =(214.0, 202.0), pos_hint ={'center_x':.625}, background_normal='UI\\squre.jpg')
		self.register = Button(text='', pos_hint ={'center_x':.5}, background_normal='UI\\reg_btn.jpg', size_hint =(.85, .15), pos =(214.0, 225.0))

		self.register.bind(on_press=self.change_reg)
		self.login.bind(on_press=self.change_log)
		#front----------------------------------------------------------------------------------------------------------------------------------------
		buttons_layout.add_widget(self.logo)
		buttons_layout.add_widget(self.about_lbl)
		buttons_layout.add_widget(self.about_text)
		buttons_layout.add_widget(self.register)
		buttons_layout.add_widget(self.if_register)
		buttons_layout.add_widget(self.login)

		return buttons_layout
		
if __name__ == '__main__':
	MyApp().run()