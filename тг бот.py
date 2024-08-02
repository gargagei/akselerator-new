import telebot

botTimeWeb = telebot.TeleBot('6721737699:AAGiSXFOx1OVdiZtYQKqPTimWAmIhfXDBH4')

from telebot import types

@botTimeWeb.message_handler(commands=['start'])
def startBot(message):
  first_mess = f"<b>{message.from_user.first_name}</b>, Привет!\nЯ телеграмм-бот ляляляляя *тут типо пояснение че за тг-бот* \nПри возникших вопросах обращайтесь к @killamrg\nВы желайте продолжить?"
  markup = types.InlineKeyboardMarkup()
  button_yes = types.InlineKeyboardButton(text = 'Привет!\n Да, желаю продолжить!', callback_data='yes')
  markup.add(button_yes)
  botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)

@botTimeWeb.callback_query_handler(func=lambda call:True)
def response(function_call2):
   if function_call2.message:
      if function_call2.data == "yes":
         third_mess = "Ознакомьтесь, пожалуйста, с информацией ниже!\n*информация*"
         markup = types.InlineKeyboardMarkup()
         button_neinformatsia = types.InlineKeyboardButton(text='Я ознакомился(сь) с ин-ей!', callback_data='yes2')
         markup.add(button_neinformatsia)
         botTimeWeb.send_message(function_call2.message.chat.id, third_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes2":
         fourth_mess = "Ответьте на вопрос\nКакого ваше моральное состояние?"
         markup = types.InlineKeyboardMarkup()
         button_neinformatsia2 = types.InlineKeyboardButton(text='Все плохо, нужна поддержка!', callback_data='yes3')
         markup.add(button_neinformatsia2)
         button_neinformatsia3 = types.InlineKeyboardButton(text='Все супер, справляюсь!', callback_data='yes4')
         markup.add(button_neinformatsia3)
         botTimeWeb.send_message(function_call2.message.chat.id, fourth_mess, parse_mode='html', reply_markup=markup)
      #поотрицательным
      if function_call2.data == "yes3":
         f_mess = "Выберите свой тип состояния (*можно примерно*)"
         markup = types.InlineKeyboardMarkup()
         button_temperament = types.InlineKeyboardButton(text='1. Тип состояния', callback_data='yes5')
         markup.add(button_temperament)
         button_temperament2 = types.InlineKeyboardButton(text='2. Тип состояния', callback_data='yes6')
         markup.add(button_temperament2)
         button_temperament3 = types.InlineKeyboardButton(text='3. Тип состояния', callback_data='yes7')
         markup.add(button_temperament3)
         button_temperament4 = types.InlineKeyboardButton(text='4. Тип состояния', callback_data='yes8')
         markup.add(button_temperament4)
         button_temperament5 = types.InlineKeyboardButton(text='5. Тип состояния', callback_data='yes9')
         markup.add(button_temperament5)
         button_temperament6 = types.InlineKeyboardButton(text='6. Тип состояния', callback_data='yes10')
         markup.add(button_temperament6)
         button_temperament7 = types.InlineKeyboardButton(text='7. Тип состояния', callback_data='yes11')
         markup.add(button_temperament7)
         button_temperament8 = types.InlineKeyboardButton(text='8. Тип состояния', callback_data='yes12')
         markup.add(button_temperament8)
         botTimeWeb.send_message(function_call2.message.chat.id, f_mess, parse_mode='html', reply_markup=markup)
      #поположительным
      if function_call2.data == "yes4":
         s_mess = "Выберите свой тип состояния (*можно примерно*)"
         markup = types.InlineKeyboardMarkup()
         button_temperamentforhappy = types.InlineKeyboardButton(text='1. Тип состояния', callback_data='yes13')
         markup.add(button_temperamentforhappy)
         button_temperamentforhappy1 = types.InlineKeyboardButton(text='2. Тип состояния', callback_data='yes14')
         markup.add(button_temperamentforhappy1)
         button_temperamentforhappy2 = types.InlineKeyboardButton(text='3. Тип состояния', callback_data='yes15')
         markup.add(button_temperamentforhappy2)
         button_temperamentforhappy3 = types.InlineKeyboardButton(text='4. Тип состояния', callback_data='yes16')
         markup.add(button_temperamentforhappy3)
         button_temperamentforhappy4 = types.InlineKeyboardButton(text='5. Тип состояния', callback_data='yes17')
         markup.add(button_temperamentforhappy4)
         button_temperamentforhappy5 = types.InlineKeyboardButton(text='6. Тип состояния', callback_data='yes18')
         markup.add(button_temperamentforhappy5)
         button_temperamentforhappy6 = types.InlineKeyboardButton(text='7. Тип состояния', callback_data='yes19')
         markup.add(button_temperamentforhappy6)
         button_temperamentforhappy7 = types.InlineKeyboardButton(text='8. Тип состояния', callback_data='yes20')
         markup.add(button_temperamentforhappy7)
         botTimeWeb.send_message(function_call2.message.chat.id, s_mess, parse_mode='html', reply_markup=markup)
      #поотрицательным
      if function_call2.data == "yes5":
         seven_mess = "Ляляля трополя *пояснение типа состояния и то как решить *\nВаше моральное состояние совпадает с утверждениями выше?"
         markup = types.InlineKeyboardMarkup()
         button_sure = types.InlineKeyboardButton(text='Да, это про меня!', callback_data='yes21')
         markup.add(button_sure)
         button_no = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes22')
         markup.add(button_no)
         botTimeWeb.send_message(function_call2.message.chat.id, seven_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes21":
         eight_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure2 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes23')
         markup.add(button_sure2)
         botTimeWeb.send_message(function_call2.message.chat.id, eight_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes22":
         nine_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure3 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes24')
         markup.add(button_sure3)
         botTimeWeb.send_message(function_call2.message.chat.id, nine_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes6":
         seven_mess = "Ляляля трополя *пояснение типа состояния и то как решить*\nВаше моральное состояние совпадает с утверждениями выше?"
         markup = types.InlineKeyboardMarkup()
         button_sure4 = types.InlineKeyboardButton(text='Да, это про меня!', callback_data='yes25')
         markup.add(button_sure4)
         button_no4 = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes26')
         markup.add(button_no4)
         botTimeWeb.send_message(function_call2.message.chat.id, seven_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes25":
         eight_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure5 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes27')
         markup.add(button_sure5)
         botTimeWeb.send_message(function_call2.message.chat.id, eight_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes26":
         nine_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure6 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes28')
         markup.add(button_sure6)
         botTimeWeb.send_message(function_call2.message.chat.id, nine_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes7":
         ten_mess = "Ляляля трополя *пояснение типа состояния и то как решить*\nВаше моральное состояние совпадает с утверждениями выше?"
         markup = types.InlineKeyboardMarkup()
         button_sure7 = types.InlineKeyboardButton(text='Да, это про меня!', callback_data='yes29')
         markup.add(button_sure7)
         button_no8 = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes30')
         markup.add(button_no8)
         botTimeWeb.send_message(function_call2.message.chat.id, ten_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes29":
         elvn_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure9 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes31')
         markup.add(button_sure9)
         botTimeWeb.send_message(function_call2.message.chat.id, elvn_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes30":
         tw_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure10 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes32')
         markup.add(button_sure10)
         botTimeWeb.send_message(function_call2.message.chat.id, tw_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes8":
         thrt_mess = "Ляляля трополя *пояснение типа состояния и то как решить*\nВаше моральное состояние совпадает с утверждениями выше?"
         markup = types.InlineKeyboardMarkup()
         button_sure11 = types.InlineKeyboardButton(text='Да, это про меня!', callback_data='yes33')
         markup.add(button_sure11)
         button_no12 = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes34')
         markup.add(button_no12)
         botTimeWeb.send_message(function_call2.message.chat.id, thrt_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes33":
         fourteen_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure13 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes35')
         markup.add(button_sure13)
         botTimeWeb.send_message(function_call2.message.chat.id, fourteen_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes34":
         fifteen_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure14 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes36')
         markup.add(button_sure14)
         botTimeWeb.send_message(function_call2.message.chat.id, fifteen_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes9":
         sixteen_mess = "Ляляля трополя *пояснение типа состояния и то как решить*\nВаше моральное состояние совпадает с утверждениями выше?"
         markup = types.InlineKeyboardMarkup()
         button_sure16 = types.InlineKeyboardButton(text='Да, это про меня!', callback_data='yes37')
         markup.add(button_sure16)
         button_no17 = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes38')
         markup.add(button_no17)
         botTimeWeb.send_message(function_call2.message.chat.id, sixteen_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes37":
         seventeen_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure18 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes39')
         markup.add(button_sure18)
         botTimeWeb.send_message(function_call2.message.chat.id, seventeen_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes38":
         eighteen_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure19 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes40')
         markup.add(button_sure19)
         botTimeWeb.send_message(function_call2.message.chat.id, eighteen_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes10":
         nineyeen_mess = "Ляляля трополя *пояснение типа состояния и то как решить*\nВаше моральное состояние совпадает с утверждениями выше?"
         markup = types.InlineKeyboardMarkup()
         button_sure16 = types.InlineKeyboardButton(text='Да, это про меня!', callback_data='yes41')
         markup.add(button_sure16)
         button_no17 = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes42')
         markup.add(button_no17)
         botTimeWeb.send_message(function_call2.message.chat.id, nineyeen_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes41":
         twony_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure18 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes43')
         markup.add(button_sure18)
         botTimeWeb.send_message(function_call2.message.chat.id, twony_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes42":
         twony1_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure19 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes44')
         markup.add(button_sure19)
         botTimeWeb.send_message(function_call2.message.chat.id, twony1_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes11":
         twony2_mess = "Ляляля трополя *пояснение типа состояния и то как решить*\nВаше моральное состояние совпадает с утверждениями выше?"
         markup = types.InlineKeyboardMarkup()
         button_sure20 = types.InlineKeyboardButton(text='Да, это про меня!', callback_data='yes45')
         markup.add(button_sure20)
         button_no21 = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes46')
         markup.add(button_no21)
         botTimeWeb.send_message(function_call2.message.chat.id, twony2_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes45":
         twony3_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure21 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes52')
         markup.add(button_sure21)
         botTimeWeb.send_message(function_call2.message.chat.id, twony3_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes46":
         twony4_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure22 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes51')
         markup.add(button_sure22)
         botTimeWeb.send_message(function_call2.message.chat.id, twony4_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes12":
         twony5_mess = "Ляляля трополя *пояснение типа состояния и то как решить*\nВаше моральное состояние совпадает с утверждениями выше?"
         markup = types.InlineKeyboardMarkup()
         button_sure23 = types.InlineKeyboardButton(text='Да, это про меня!', callback_data='yes49')
         markup.add(button_sure23)
         button_no21 = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes50')
         markup.add(button_no21)
         botTimeWeb.send_message(function_call2.message.chat.id, twony5_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes49":
         twony6_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure24 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes47')
         markup.add(button_sure24)
         botTimeWeb.send_message(function_call2.message.chat.id, twony6_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes50":
         twony7_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure25 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes48')
         markup.add(button_sure25)
         botTimeWeb.send_message(function_call2.message.chat.id, twony7_mess, parse_mode='html', reply_markup=markup)
      #поположительным
      if function_call2.data == "yes13":
         seven_mess = "Ляляля трополя *пояснение типа состояния и то как решить*\nВаше моральное состояние совпадает с утверждениями выше?"
         markup = types.InlineKeyboardMarkup()
         button_sure = types.InlineKeyboardButton(text='Да, это про меня!', callback_data='yes53')
         markup.add(button_sure)
         button_no = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes54')
         markup.add(button_no)
         botTimeWeb.send_message(function_call2.message.chat.id, seven_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes53":
         eight_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure2 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes23')
         markup.add(button_sure2)
         botTimeWeb.send_message(function_call2.message.chat.id, eight_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes54":
         nine_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure3 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes24')
         markup.add(button_sure3)
         botTimeWeb.send_message(function_call2.message.chat.id, nine_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes14":
         seven_mess = "Ляляля трополя *пояснение типа состояния и то как решить*\nВаше моральное состояние совпадает с утверждениями выше?"
         markup = types.InlineKeyboardMarkup()
         button_sure4 = types.InlineKeyboardButton(text='Да, это про меня!', callback_data='yes55')
         markup.add(button_sure4)
         button_no4 = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes56')
         markup.add(button_no4)
         botTimeWeb.send_message(function_call2.message.chat.id, seven_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes55":
         eight_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure5 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes27')
         markup.add(button_sure5)
         botTimeWeb.send_message(function_call2.message.chat.id, eight_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes56":
         nine_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure6 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes28')
         markup.add(button_sure6)
         botTimeWeb.send_message(function_call2.message.chat.id, nine_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes15":
         ten_mess = "Ляляля трополя *пояснение типа состояния и то как решить*\nВаше моральное состояние совпадает с утверждениями выше?"
         markup = types.InlineKeyboardMarkup()
         button_sure7 = types.InlineKeyboardButton(text='Да, это про меня!', callback_data='yes57')
         markup.add(button_sure7)
         button_no8 = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes58')
         markup.add(button_no8)
         botTimeWeb.send_message(function_call2.message.chat.id, ten_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes57":
         elvn_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure9 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes31')
         markup.add(button_sure9)
         botTimeWeb.send_message(function_call2.message.chat.id, elvn_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes58":
         tw_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure10 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes32')
         markup.add(button_sure10)
         botTimeWeb.send_message(function_call2.message.chat.id, tw_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes16":
         thrt_mess = "Ляляля трополя *пояснение типа состояния и то как решить*\nВаше моральное состояние совпадает с утверждениями выше?"
         markup = types.InlineKeyboardMarkup()
         button_sure11 = types.InlineKeyboardButton(text='Да, это про меня!', callback_data='yes59')
         markup.add(button_sure11)
         button_no12 = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes60')
         markup.add(button_no12)
         botTimeWeb.send_message(function_call2.message.chat.id, thrt_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes59":
         fourteen_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure13 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes35')
         markup.add(button_sure13)
         botTimeWeb.send_message(function_call2.message.chat.id, fourteen_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes60":
         fifteen_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure14 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes36')
         markup.add(button_sure14)
         botTimeWeb.send_message(function_call2.message.chat.id, fifteen_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes17":
         sixteen_mess = "Ляляля трополя *пояснение типа состояния и то как решить*\nВаше моральное состояние совпадает с утверждениями выше?"
         markup = types.InlineKeyboardMarkup()
         button_sure16 = types.InlineKeyboardButton(text='Да, это про меня!', callback_data='yes61')
         markup.add(button_sure16)
         button_no17 = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes62')
         markup.add(button_no17)
         botTimeWeb.send_message(function_call2.message.chat.id, sixteen_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes61":
         seventeen_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure18 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes39')
         markup.add(button_sure18)
         botTimeWeb.send_message(function_call2.message.chat.id, seventeen_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes62":
         eighteen_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure19 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes40')
         markup.add(button_sure19)
         botTimeWeb.send_message(function_call2.message.chat.id, eighteen_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes18":
         nineyeen_mess = "Ляляля трополя *пояснение типа состояния и то как решить*\nВаше моральное состояние совпадает с утверждениями выше?"
         markup = types.InlineKeyboardMarkup()
         button_sure16 = types.InlineKeyboardButton(text='Да, это про меня!', callback_data='yes63')
         markup.add(button_sure16)
         button_no17 = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes64')
         markup.add(button_no17)
         botTimeWeb.send_message(function_call2.message.chat.id, nineyeen_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes63":
         twony_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure18 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes43')
         markup.add(button_sure18)
         botTimeWeb.send_message(function_call2.message.chat.id, twony_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes64":
         twony1_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure19 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes44')
         markup.add(button_sure19)
         botTimeWeb.send_message(function_call2.message.chat.id, twony1_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes19":
         twony2_mess = "Ляляля трополя *пояснение типа состояния* и то как решить\nВаше моральное состояние совпадает с утверждениями выше?"
         markup = types.InlineKeyboardMarkup()
         button_sure20 = types.InlineKeyboardButton(text='Да, это про меня!', callback_data='yes65')
         markup.add(button_sure20)
         button_no21 = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes66')
         markup.add(button_no21)
         botTimeWeb.send_message(function_call2.message.chat.id, twony2_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes65":
         twony3_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure21 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes47')
         markup.add(button_sure21)
         botTimeWeb.send_message(function_call2.message.chat.id, twony3_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes66":
         twony4_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure22 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes48')
         markup.add(button_sure22)
         botTimeWeb.send_message(function_call2.message.chat.id, twony4_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes20":
         twony5_mess = "Ляляля трополя *пояснение типа состояния* и то как решить\nВаше моральное состояние совпадает с утверждениями выше?"
         markup = types.InlineKeyboardMarkup()
         button_sure23 = types.InlineKeyboardButton(text='Да, это про меня!', callback_data='yes67')
         markup.add(button_sure23)
         button_no21 = types.InlineKeyboardButton(text='Нет, не совсем.', callback_data='yes68')
         markup.add(button_no21)
         botTimeWeb.send_message(function_call2.message.chat.id, twony5_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes67":
         twony6_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure24 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes47')
         markup.add(button_sure24)
         botTimeWeb.send_message(function_call2.message.chat.id, twony6_mess, parse_mode='html', reply_markup=markup)
      if function_call2.data == "yes68":
         twony7_mess = "Ну, в таком случае получай картинку *она ниже будет как раз*\nТут короче текст типо поддерживающий и вообще полный чиназес"
         markup = types.InlineKeyboardMarkup()
         button_sure25 = types.InlineKeyboardButton(text='Спасибо за хорошее настроение!', callback_data='yes48')
         markup.add(button_sure25)
         botTimeWeb.send_message(function_call2.message.chat.id, twony7_mess, parse_mode='html', reply_markup=markup)


botTimeWeb.polling(none_stop=True)
# <У меня постоянно депрессивное настроение, мен не радует> \n2. <У меня очень переменчивое настроение, может быть как депрессивным, так и веселым!>  \n3. <Чаще всего я не хожу грустным, а наоборот пытаюсь казаться веселым, думаю, что грустного(ую) меня общество не примет!  \n4. Я вообще случайно нажал, все хорошо!"