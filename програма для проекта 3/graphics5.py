from tkinter import *
from tkinter import ttk
from random import *
from tkhtmlview import *
from base import *
root = Tk()
root.geometry("600x300")
root.resizable(width = False, height = False)
root.title("log1.4.5")
s = ttk.Style()
s.configure(".", font=('Verdana', 18))
s.configure("TButton", font = ("Verdana", 14))
s.configure("My.TLabel", font = ("Verdana", 40))
s.configure("stepen.TLabel", font = ("Verdana", 14))
s.configure("Right_otv_l.TLabel", background='PaleGreen')
s.configure("not_right_otv_l.TLabel", background='IndianRed')
s.configure("sub.TLabel", font = ("Veranda", 13))
s.configure("Osn_v_stepen.TLabel", font = ("Verdana", 10))
#функции
def to_1():
	tab_control.select(tab2)
def to_2():
	tab_control.select(tab3)
def to_3():
	tab_control.select(tab4)
def to_4():
	tab_control.select(tab5)
def to_5():
	tab_control.select(tab6)
def to_6():
	tab_control.select(tab7)
def to_7():
	tab_control.select(tab8)
def to_8():
	tab_control.select(tab9)
def to_9():
	tab_control.select(tab10)
def to_10():
	tab_control.select(tab11)
def back2():
	global tab3, tab4, tab2, tab1, tab_control, tab5, result
	tab1 = ttk.Frame(tab_control)
	tab_control.add(tab1, text = "главное меню")
	#содержимое
	btn = ttk.Button(tab1, text = "старт", command = prog)
	btn.place(relx = 0.30, rely = 0.2)
	btn2 = ttk.Button(tab1, text = "инструкция", command = info)
	btn2.place(relx = 0.6, rely = 0.2)
	l1 = ttk.Label(tab1,text = "Приветствуем в программе log1.4.5!")
	l1.place(relx = 0.05, rely = 0.04)
	#форгеты
	tab_control.forget(result)
def alert_back():
	global alert
	alert = Toplevel()
	alert.geometry("300x150")
	alert.grab_set()
	alert_label = ttk.Label(alert, text = "Выйти в меню?")
	alert_label.pack()
	alert_exit = ttk.Button(alert, text = "выйти", command = back)
	alert_exit.pack()
	alert_no_exit = ttk.Button(alert, text = "нет", command = no_exit)
	alert_no_exit.pack()
def no_exit():
	alert.destroy()
def back():
	global tab3, tab4, tab2, tab1, tab_control, tab5, result
	tab1 = ttk.Frame(tab_control)
	tab_control.add(tab1, text = "главное меню")
	#содержимое
	btn = ttk.Button(tab1, text = "старт", command = prog)
	btn.place(relx = 0.3, rely = 0.2)
	btn2 = ttk.Button(tab1, text = "инструкция", command = info)
	btn2.place(relx = 0.6, rely = 0.2)
	l1 = ttk.Label(tab1,text = "Приветствуем в программе log1.4.5!")
	l1.place(relx = 0.05, rely = 0.04)
	alert.destroy()
	#форгеты
	tab_control.forget(tab2)
	tab_control.forget(tab3)
	tab_control.forget(tab4)
	tab_control.forget(tab5)
	tab_control.forget(tab6)
	tab_control.forget(tab7)
	tab_control.forget(tab8)
	tab_control.forget(tab9)
	tab_control.forget(tab10)
	tab_control.forget(tab11)
def error_alert_exit():
	error_alert.destroy()
def alert_proverka_destroy():
	alert_proverka_w.destroy()
def alert_proverka():
	global alert_proverka_w
	alert_proverka_w = Toplevel()
	alert_proverka_w.geometry("300x150")
	alert_proverka_w.resizable(width = False, height = False)
	alert_proverka_w.grab_set()
	proverka_l = ttk.Label(alert_proverka_w, text = "Завершить весь тест?")
	proverka_l.pack()
	proverka_btn = ttk.Button(alert_proverka_w, text = "завершить", command = proverka)
	proverka_btn.pack()
	proverka_btn2 = ttk.Button(alert_proverka_w, text = "нет", command = alert_proverka_destroy)
	proverka_btn2.pack()
def proverka():
	global tab5, tab3, tab4, tab2, tab1, tab_control, result, otvety, right_otvety, error_alert
	otvety = [ans1.get(), ans2.get(), ans3.get(), ans4.get(), ans5.get(), ans6.get(), ans7.get(), ans8.get(), ans9.get(), ans10.get()]
	right_otvety = [base1[random1][-1], base2[random2][-1], base3[random3][-1], base4[random4][-1], base5[random5][-1], base6[random6][-1], base7[random7][-1], base8[random8][-1], base9[random9][-1], base10[random10][-1]]
	simb = ["0","1","2","3","4","5","6","7","8","9","/","","-"]
	for o in otvety:
		for o1 in o:
			if o1 not in simb:
				error_alert = Toplevel()
				error_alert.grab_set()
				error_alert.resizable(height = False, width = False)
				error_alert.geometry("500x200")
				error_label = ttk.Label(error_alert, text = "обнаружен некорректный ответ")
				error_label.pack()
				error_label2 = HTMLLabel(error_alert, html = """
					<p><b>
					Проверьте ответы на наличие пустых пробелов, точек, запятых и других символов
					</b></p>
					""")
				error_label2.pack()
				error_btn = ttk.Button(error_alert, text = "закрыть", command = error_alert_exit)
				error_btn.place(relx = 0.6, rely = 0.7)
				alert_proverka_destroy()
				return False
	print(otvety)
	print(right_otvety)
	result = ttk.Frame()
	tab_control.add(result, text = "результат")
	tab_control.select(result)
	score = 0
	for i in range(len(otvety)):
		if otvety[i] == right_otvety[i]:
			score +=1
		else:
			pass
	score_ = ttk.Label(result, text = score)
	score_.grid(column = 1, row = 0)
	vash_res = ttk.Label(result, text = "ваш реузльтат: ")
	vash_res.grid(column = 0, row = 0)
	iz_4 = ttk.Label(result, text = "из 10", font= "Arial 20")
	iz_4.grid(column = 2, row = 0)
	btn2 = ttk.Button(result, text = "В меню", command = back2)
	btn2.place(relx = 0.7, rely = 0.8)
	podrobney_btn = ttk.Button(result, text = "подробнее", command = podrobney)
	podrobney_btn.grid(column = 0, row = 1)
	#форгеты
	tab_control.forget(tab2)
	tab_control.forget(tab3)
	tab_control.forget(tab4)
	tab_control.forget(tab5)
	tab_control.forget(tab6)
	tab_control.forget(tab7)
	tab_control.forget(tab8)
	tab_control.forget(tab9)
	tab_control.forget(tab10)
	tab_control.forget(tab11)
	alert_proverka_w.destroy()
def podrobney():
	proverka_tab = Toplevel()
	proverka_tab.grab_set()
	proverka_tab.resizable(height = False, width = False)
	colunm_num = 0
	row_num = 1
	right_otv = ttk.Label(proverka_tab,text = "правильный ответ")
	right_otv.grid(column  = 1, row = 0, padx = (20,20))
	vas_otv = ttk.Label(proverka_tab,text = "ваш ответ")
	vas_otv.grid(column  = 2, row = 0, padx = (20,20))
	zad_ = ttk.Label(proverka_tab,text = "задание")
	zad_.grid(column  = 0, row = 0, padx = (20,20))
	for k in range(len(right_otvety)):
		zad_num = ttk.Label(proverka_tab, text = k + 1)
		zad_num.grid(column = 0, row = row_num)
		row_num +=1
	row_num = 1
	for j in range(len(right_otvety)):
		right_otvet  = ttk.Label(proverka_tab, text = right_otvety[j])
		right_otvet.grid(column = 1, row = row_num)
		row_num += 1
	row_num = 1
	for p in range(len(right_otvety)):
		if otvety[p] == "":
			vas_otv_ = ttk.Label(proverka_tab, text = otvety[p], width = 8)
			vas_otv_.grid(column = 2, row = row_num)
		else:
			if otvety[p] == right_otvety[p]:
				vas_otv_ = ttk.Label(proverka_tab, text = otvety[p], style = "Right_otv_l.TLabel", width = 8)
				vas_otv_.grid(column = 2, row = row_num)
			else:
				vas_otv_ = ttk.Label(proverka_tab, text = otvety[p], style = "not_right_otv_l.TLabel", width = 8)
				vas_otv_.grid(column = 2, row = row_num)
		row_num += 1
def info_exit():
	info_.destroy()
def info():
	global info_
	info_ = Toplevel()
	info_.geometry("740x500")
	info_.resizable(width = False, height = False)
	info_.grab_set()
	l_info = ttk.Label(info_, text="инструкция по программе")
	l_info.pack()
	l_info2 = HTMLScrolledText(info_, html = """
		<h4>Версия программы</h4>
		<p>
		Приветствуем в программе log версии 1.4.6!
		Здесь вы познакомитесь с правилами пользования программы.
		</p>
		<h4>Запуск и работа программы</h4>
		<p>
		Для начала тестирования нажмите кнопку "старт" в главном меню. 
		Название окна, в котором вы находитесь, отображается в верхней части программы.
		</p>
		<p>
		После нажатия кнопки старт вы появитесь на вкладке первого задания.
		На каждой вкладке присутствует: Задание, окно для ввода ответа, кнопки для перемещения
		к предыдущему и следующему заданию, кнопка выходы в главное меню, кнопка завершения тестирования. 
		В верхней части программы вы можете видеть вкладки других заданий. Для более быстрого перемещения
		на конкретные задания вы можете использовать их.
		Стоит отметить, что возвращение в главное меню полностью сбросит ваши ответы и перезапустит тестирование.
		</p>
		<h4>Форма записи ответов (обязательно к прочтению!)</h4>
		<p>
		Программа принимает ответы только в виде целого числа, правильной и неправильной дроби.
		Пример: Ответом к задаче "0,5 * log₃₂4" будет значение 1/5, которое можно так же записать в виде
		десятично дроби 0.2 или 0,2, но их программа засчитает неверными. Ответом к задаче "log₈128"
		будет значение 7/3, которое можно записать в виде 2 1/3, но этот ответ программа засчитает неверным.
		Eсли ответом является отрицательное число, то знак минус должен стоять перед числом без,
		отделять минус от числа пробелом не нужно. Если ответом является отрицательная дробь, то минус должн стоять
		перед всей дробью, отделять дробь от минуса пробелом не нужно.
		</p>
		<p>
		Если в ответах присутствуют некорректные символы, то при нажатии кнопки завершения теста
		вам высветится окно предупреждения о некорректном ответе. Проверьте ответы на наличие
		указанных символов.
		</p>
		""")
	l_info2.pack()
	info_btn = ttk.Button(info_, text = "закрыть", command = info_exit )
	info_btn.pack()
def prog():
	global tab11,tab10,tab9,tab8,tab7,tab6,tab5, tab3, tab4, tab2, tab1, tab_control, random1, ans1, random2, ans2, random3, ans3, random4,random5,random7, ans7, ans4, ans5, ans6, random8, ans8, random6,random9, ans9,random10, ans10, result
	tab2 = ttk.Frame(tab_control)
	tab_control.add(tab2, text = " 1 ")
	tab3 = ttk.Frame(tab_control)
	tab_control.add(tab3, text = " 2 ")
	tab4 = ttk.Frame(tab_control)
	tab_control.add(tab4, text = " 3 ")
	tab5 = ttk.Frame(tab_control)
	tab_control.add(tab5, text = " 4 ")
	tab6 = ttk.Frame(tab_control)
	tab_control.add(tab6, text = " 5 ")
	tab7 = ttk.Frame(tab_control)
	tab_control.add(tab7, text = " 6 ")
	tab8 = ttk.Frame(tab_control)
	tab_control.add(tab8, text = " 7 ")
	tab9 = ttk.Frame(tab_control)
	tab_control.add(tab9, text = " 8 ")
	tab10 = ttk.Frame(tab_control)
	tab_control.add(tab10, text = " 9 ")
	tab11 = ttk.Frame(tab_control)
	tab_control.add(tab11, text = "10")
	#содержимое
	##кнопка выхода
	btn2 = ttk.Button(tab2, text = "В меню", command = alert_back)
	btn2.place(relx = 0.7, rely = 0.8)
	btn2 = ttk.Button(tab3, text = "В меню", command = alert_back)
	btn2.place(relx = 0.7, rely = 0.8)
	btn2 = ttk.Button(tab4, text = "В меню", command = alert_back)
	btn2.place(relx = 0.7, rely = 0.8)
	btn2 = ttk.Button(tab5, text = "В меню", command = alert_back)
	btn2.place(relx = 0.7, rely = 0.8)
	btn2 = ttk.Button(tab6, text = "В меню", command = alert_back)
	btn2.place(relx = 0.7, rely = 0.8)
	btn2 = ttk.Button(tab7, text = "В меню", command = alert_back)
	btn2.place(relx = 0.7, rely = 0.8)
	btn2 = ttk.Button(tab8, text = "В меню", command = alert_back)
	btn2.place(relx = 0.7, rely = 0.8)
	btn2 = ttk.Button(tab9, text = "В меню", command = alert_back)
	btn2.place(relx = 0.7, rely = 0.8)
	btn2 = ttk.Button(tab10, text = "В меню", command = alert_back)
	btn2.place(relx = 0.7, rely = 0.8)
	btn2 = ttk.Button(tab11, text = "В меню", command = alert_back)
	btn2.place(relx = 0.7, rely = 0.8)
	#задание 1
	random1 = randint(0, len(base1) - 1)
	zad_cont1 = Canvas(tab2, height = 300, width = 500)
	zad_cont1.place(relx = 0.35, rely = 0.1)
	#контейнер
	log_zad_1_1 = ttk.Label(zad_cont1, text = base1[random1][0])
	log_zad_1_1.grid(row = 0, column = 0)
	osn_zad1_1 = ttk.Label(zad_cont1, text = base1[random1][1], style = "sub.TLabel")
	osn_zad1_1.grid(row = 0, column = 1, sticky = S)
	chis_zad1_1 = ttk.Label(zad_cont1, text = base1[random1][2])
	chis_zad1_1.grid(row = 0, column = 2)
	znak_zad1 = ttk.Label(zad_cont1, text = base1[random1][3])
	znak_zad1.grid(row = 0, column = 3)
	log_zad_1_2 = ttk.Label(zad_cont1, text = base1[random1][4])
	log_zad_1_2.grid(row = 0, column = 4)
	osn_zad1_2 = ttk.Label(zad_cont1, text = base1[random1][5], style = "sub.TLabel")
	osn_zad1_2.grid(row = 0, column = 5, sticky = S)
	chis_zad1_2 = ttk.Label(zad_cont1, text = base1[random1][6])
	chis_zad1_2.grid(row = 0, column = 6)
	#кнопки
	ans1 = ttk.Entry(tab2)
	ans1.place(relx = 0.4, rely = 0.25)
	next_q = ttk.Button(tab2, text = "След.", command = to_2)
	next_q.place(relx = 0.4, rely = 0.8)
	otvetit = ttk.Button(tab2, text = "завершить", command = alert_proverka)
	otvetit.place(relx = 0.7, rely = 0.55)
	#задание 2
	random2 = randint(0, len(base2) - 1)
	zad_cont2 = Canvas(tab3, height = 300, width = 500)
	zad_cont2.place(relx = 0.35, rely = 0.1)
	zad_cont2_2 = Canvas(zad_cont2)
	zad_cont2_2.grid(row = 0, column = 0, columnspan = 3)
	zad_cont2_3 = Canvas(zad_cont2)
	zad_cont2_3.grid(row = 2, column = 0, columnspan = 3)
	#Контейнер
	log_zad2_1 = ttk.Label(zad_cont2_2, text = base2[random2][0])
	log_zad2_1.grid(row = 0, column = 0)
	osn_zad_2_1 = ttk.Label(zad_cont2_2, text = base2[random2][1], style  = "sub.TLabel")
	osn_zad_2_1.grid(row = 0, column = 1, sticky = S)
	chis_zad2_1 = ttk.Label(zad_cont2_2, text = base2[random2][2])
	chis_zad2_1.grid(row = 0, column = 2)
	under_l = Canvas(zad_cont2, width = 110, height = 5)
	under_l.create_line(1, 2, 100, 2, width = 5)
	under_l.grid(row = 1, column = 0, columnspan = 110)
	log_zad2_2 = ttk.Label(zad_cont2_3, text = base2[random2][3])
	log_zad2_2.grid(row = 2, column = 0)
	osn_zad2_2 = ttk.Label(zad_cont2_3, text = base2[random2][4], style = "sub.TLabel")
	osn_zad2_2.grid(row = 2, column = 1, sticky = S)
	chis_zad2_2 = ttk.Label(zad_cont2_3, text = base2[random2][5])
	chis_zad2_2.grid(row =2, column = 2)
	#кнопки
	ans2 = ttk.Entry(tab3)
	ans2.place(relx = 0.3, rely = 0.6)
	next_q = ttk.Button(tab3, text = "След.", command = to_3)
	next_q.place(relx = 0.4, rely = 0.8)
	last_q = ttk.Button(tab3, text = "Пред.", command = to_1)
	last_q.place(relx = 0.1, rely = 0.8)
	otvetit = ttk.Button(tab3, text = "завершить", command = alert_proverka)
	otvetit.place(relx = 0.7, rely = 0.55)
	#задание 3
	random3 = randint(0,len(base3) - 1)
	zad_cont3 = Canvas(tab4, height = 200, width = 300)
	zad_cont3.place(relx = 0.35, rely = 0.1)
	#контейнер
	log_zad3_1 = ttk.Label(zad_cont3, text = base3[random3][0])
	log_zad3_1.grid(row = 0, column = 0)
	osn_zad3_1 = ttk.Label(zad_cont3, text = base3[random3][1], style = "sub.TLabel")
	osn_zad3_1.grid(row = 0, column = 1, sticky = S)
	chis_zad3_1 = ttk.Label(zad_cont3, text = base3[random3][2])
	chis_zad3_1.grid(row = 0, column = 2)
	znak_zad3 = ttk.Label(zad_cont3, text = base3[random3][3])
	znak_zad3.grid(row = 0, column = 3)
	log_zad3_2 = ttk.Label(zad_cont3, text = base3[random3][4])
	log_zad3_2.grid(row = 0, column = 4)
	osn_zad3_2 = ttk.Label(zad_cont3, text = base3[random3][5], style = "sub.TLabel")
	osn_zad3_2.grid(row = 0, column = 5, sticky = S)
	chis_zad3_2 = ttk.Label(zad_cont3, text = base3[random3][6])
	chis_zad3_2.grid(row = 0, column = 6)
	#кнопки
	ans3 = ttk.Entry(tab4)
	ans3.place(relx = 0.4, rely = 0.25)
	next_q = ttk.Button(tab4, text = "След.", command = to_4)
	next_q.place(relx = 0.4, rely = 0.8)
	last_q = ttk.Button(tab4, text = "Пред.", command = to_2)
	last_q.place(relx = 0.1, rely = 0.8)
	otvetit = ttk.Button(tab4, text = "завершить", command = alert_proverka)
	otvetit.place(relx = 0.7, rely = 0.55)
	#задание 4
	random4 = randint(0,len(base4) - 1)
	zad_cont4 = Canvas(tab5, width = 200, height = 200)
	zad_cont4.place(relx = 0.35, rely = 0.1)
	#контейнер
	log_zad4 = ttk.Label(zad_cont4, text = base4[random4][0])
	log_zad4.grid(row = 0, column = 0)
	osn_zad4 = ttk.Label(zad_cont4, text = base4[random4][1], style = "sub.TLabel")
	osn_zad4.grid(row = 0, column = 1, sticky = S)
	chis_zad4 = ttk.Label(zad_cont4, text = base4[random4][2])
	chis_zad4.grid(row = 0, column = 2)
	#кнопки
	ans4 = ttk.Entry(tab5)
	ans4.place( relx = 0.3, rely = 0.3)
	next_q = ttk.Button(tab5, text = "След.", command = to_5)
	next_q.place(relx = 0.4, rely = 0.8)
	last_q = ttk.Button(tab5, text = "Пред.", command = to_3)
	last_q.place(relx = 0.1, rely = 0.8)
	otvetit = ttk.Button(tab5, text = "завершить", command = alert_proverka)
	otvetit.place(relx = 0.7, rely = 0.55)
	#задание 5
	random5 = randint(0,len(base5) - 1)
	zad_cont5 = Canvas(tab6, height = 300, width = 500)
	zad_cont5.place(relx = 0.35, rely = 0.1)
	#Содержимое
	log_zad_5_1 = ttk.Label(zad_cont5, text = base5[random5][0])
	log_zad_5_1.grid(row = 0, column = 0)
	osn_zad5_1 = ttk.Label(zad_cont5, text = base5[random5][1], style = "sub.TLabel")
	osn_zad5_1.grid(row = 0, column = 1, sticky = S)
	chis_zad5_1 = ttk.Label(zad_cont5, text = base5[random5][2])
	chis_zad5_1.grid(row = 0, column = 2)
	znak_zad5 = ttk.Label(zad_cont5, text = base5[random5][3])
	znak_zad5.grid(row = 0, column = 3)
	log_zad_5_2 = ttk.Label(zad_cont5, text = base5[random5][4])
	log_zad_5_2.grid(row = 0, column = 4)
	osn_zad5_2 = ttk.Label(zad_cont5, text = base5[random5][5], style = "sub.TLabel")
	osn_zad5_2.grid(row = 0, column = 5, sticky = S)
	chis_zad5_2 = ttk.Label(zad_cont5, text = base5[random5][6])
	chis_zad5_2.grid(row = 0, column = 6)
	#Кнопки
	ans5 = ttk.Entry(tab6)
	ans5.place(relx = 0.4, rely = 0.25)
	next_q = ttk.Button(tab6, text = "След.", command = to_6)
	next_q.place(relx = 0.4, rely = 0.8)
	last_q = ttk.Button(tab6, text = "Пред.", command = to_4)
	last_q.place(relx = 0.1, rely = 0.8)
	otvetit = ttk.Button(tab6, text = "завершить", command = alert_proverka)
	otvetit.place(relx = 0.7, rely = 0.55)
	#задание 6
	random6 = randint(0,len(base6) - 1)
	zad_cont6 = Canvas(tab7, height = 300, width = 500)
	zad_cont6.place(relx = 0.35, rely = 0.1)
	#Содержимое
	mnoj = ttk.Label(zad_cont6, text = base6[random6][0])
	mnoj.grid(row = 0, column = 0)
	znak_zad6 = ttk.Label(zad_cont6, text = base6[random6][1])
	znak_zad6.grid(row = 0, column = 1)
	log_zad6 = ttk.Label(zad_cont6, text = base6[random6][2])
	log_zad6.grid(row = 0, column = 2)
	osn_zad6 = ttk.Label(zad_cont6, text = base6[random6][3], style = "sub.TLabel")
	osn_zad6. grid(row = 0, column = 3, sticky = S)
	chis_zad6 = ttk.Label(zad_cont6, text = base6[random6][4])
	chis_zad6.grid(row = 0, column = 4)
	#Кнопки
	ans6 = ttk.Entry(tab7)
	ans6.place(relx = 0.4, rely = 0.25)
	next_q = ttk.Button(tab7, text = "След.", command = to_7)
	next_q.place(relx = 0.4, rely = 0.8)
	last_q = ttk.Button(tab7, text = "Пред.", command = to_5)
	last_q.place(relx = 0.1, rely = 0.8)
	otvetit = ttk.Button(tab7, text = "завершить", command = alert_proverka)
	otvetit.place(relx = 0.7, rely = 0.55)
	#задание 7
	random7 = randint(0,len(base7) - 1)
	zad_cont7 = Canvas(tab8,height = 300, width = 500)
	zad_cont7.place(relx = 0.40, rely = 0.1)
	zad_cont7_2 = Canvas(zad_cont7)
	zad_cont7_2.grid(row = 0, column = 1)
	#Содержимое
	niz_chis7 = ttk.Label(zad_cont7, text = base7[random7][0])
	niz_chis7.grid(row = 1, column = 0, rowspan = 2)
	log_zad7 = ttk.Label(zad_cont7_2, text = base7[random7][1], style = "stepen.TLabel")
	log_zad7.grid(row = 0, column = 0)
	osn_zad7 = ttk.Label(zad_cont7_2, text = base7[random7][2], style = "Osn_v_stepen.TLabel")
	osn_zad7.grid(row = 0, column = 1, sticky = S)
	chis_zad7 = ttk.Label(zad_cont7_2, text = base7[random7][3], style = "stepen.TLabel")
	chis_zad7.grid(row = 0, column = 2)
	#Кнопки
	ans7 = ttk.Entry(tab8)
	ans7.place(relx = 0.4, rely = 0.35)
	next_q = ttk.Button(tab8, text = "След.", command = to_8)
	next_q.place(relx = 0.4, rely = 0.8)
	last_q = ttk.Button(tab8, text = "Пред.", command = to_6)
	last_q.place(relx = 0.1, rely = 0.8)
	otvetit = ttk.Button(tab8, text = "завершить", command = alert_proverka)
	otvetit.place(relx = 0.7, rely = 0.55)
	#задание 8
	random8 = randint(0,len(base8) - 1)
	zad_cont8 = Canvas(tab9,height = 300, width = 500)
	zad_cont8.place(relx = 0.40, rely = 0.1)
	zad_cont8_2 = Canvas(zad_cont8)
	zad_cont8_2.grid(row = 0, column = 1)
	#содержимое
	niz_chis8 = ttk.Label(zad_cont8, text = base8[random8][0])
	niz_chis8.grid(row = 1, column = 0, rowspan = 2)
	log_zad8 = ttk.Label(zad_cont8_2, text = base8[random8][1], style = "stepen.TLabel")
	log_zad8.grid(row = 0, column = 0)
	osn_zad8 = ttk.Label(zad_cont8_2, text = base8[random8][2], style = "Osn_v_stepen.TLabel")
	osn_zad8.grid(row = 0, column = 1, sticky = S)
	chis_zad8 = ttk.Label(zad_cont8_2, text = base8[random8][3], style = "stepen.TLabel")
	chis_zad8.grid(row = 0, column = 2)
	#кнопки
	ans8 = ttk.Entry(tab9)
	ans8.place(relx = 0.4, rely = 0.35)
	next_q = ttk.Button(tab9, text = "След.", command = to_9)
	next_q.place(relx = 0.4, rely = 0.8)
	last_q = ttk.Button(tab9, text = "Пред.", command = to_7)
	last_q.place(relx = 0.1, rely = 0.8)
	otvetit = ttk.Button(tab9, text = "завершить", command = alert_proverka)
	otvetit.place(relx = 0.7, rely = 0.55)
	#задание 9
	random9 = randint(0, len(base9) - 1)
	zad_cont9 = Canvas(tab10,height = 300, width = 500)
	zad_cont9.place(relx = 0.40, rely = 0.1)
	#контейнер
	comm9 = ttk.Label(zad_cont9, text = "найдите x:")
	comm9.grid(row = 0, column = 0, columnspan = 4)
	log_zad9 = ttk.Label(zad_cont9, text = base9[random9][0])
	log_zad9.grid(row = 1, column = 0)
	osn_zad9 = ttk.Label(zad_cont9, text = base9[random9][1], style = "sub.TLabel")
	osn_zad9.grid(row = 1, column = 1, sticky = S)
	chis_zad9 = ttk.Label(zad_cont9, text = base9[random9][2])
	chis_zad9.grid(row = 1, column = 2)
	#кнопки
	ans9 = ttk.Entry(tab10)
	ans9.place(relx = 0.4, rely = 0.4)
	next_q = ttk.Button(tab10, text = "След.", command = to_10)
	next_q.place(relx = 0.4, rely = 0.8)
	last_q = ttk.Button(tab10, text = "Пред.", command = to_8)
	last_q.place(relx = 0.1, rely = 0.8)
	otvetit = ttk.Button(tab10, text = "завершить", command = alert_proverka)
	otvetit.place(relx = 0.7, rely = 0.55)
	#задание 10
	random10 = randint(0, len(base10)-1)
	zad_cont10 = Canvas(tab11,height = 300, width = 500)
	zad_cont10.place(relx = 0.40, rely = 0.1)
	#контейнер
	comm10 = ttk.Label(zad_cont10, text = "найдите x:")
	comm10.grid(row = 0, column = 0, columnspan = 4)
	log_zad10 = ttk.Label(zad_cont10, text = base10[random10][0])
	log_zad10.grid(row = 1, column = 0)
	osn_zad10 = ttk.Label(zad_cont10, text = base10[random10][1], style = "sub.TLabel")
	osn_zad10.grid(row = 1, column = 1, sticky = S)
	chis_zad10 = ttk.Label(zad_cont10, text = base10[random10][2])
	chis_zad10.grid(row = 1, column = 2)
	#кнопки
	ans10 = ttk.Entry(tab11,)
	ans10.place(relx = 0.4, rely = 0.4)
	last_q = ttk.Button(tab11, text = "Пред.", command = to_9)
	last_q.place(relx = 0.1, rely = 0.8)
	otvetit = ttk.Button(tab11, text = "завершить", command = alert_proverka)
	otvetit.place(relx = 0.7, rely = 0.55)
	#форгеты
	tab_control.forget(tab1)
#Окно
tab_control = ttk.Notebook(root)
tab_control.pack(expand = 1, fill = BOTH)
#вкладки
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text = "главное меню")
#содержимое
btn = ttk.Button(tab1, text = "старт", command = prog)
btn.place(relx = 0.3, rely = 0.2)
btn2 = ttk.Button(tab1, text = "инструкция", command = info)
btn2.place(relx = 0.6, rely = 0.2)
l1 = ttk.Label(tab1,text = "Приветствуем в программе log1.4.6!")
l1.place(relx = 0.05, rely = 0.04)
root.mainloop()