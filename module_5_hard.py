from time import sleep
class Video:
    def __init__(self,title, duration, adult_mode=False):
        self.time_now = 0
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
    def __str__(self):
        return f'"{self.title}" длительностью {self.duration} минут.'
    def play(self):
        p=self.duration//5
        print(f'Воспроизводится "{self.title}" просмотрено: 0 сек --- ',end='')
        for i in range(5):
            sleep(1)
            self.time_now +=p
            print(f'{self.time_now} сек --- ',end='')
        self.time_now=0
        print('Конец.')
        return self


class User:
    def __init__(self,nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
    def __str__(self):
        return self.nickname

class UrTube:
    def __init__(self):
        self.dict_videos = dict()#Словарь видео
        self.dict_user = dict()#Словарь зарегистрированных пользователей доступ по хешу
        self.online_user = list()
        self.cur_user = None
    def add(self,*args):
        for v in args:
            if v.title in self.dict_videos.keys():
                print(f'Видео с названием "{v.title}" уже есть!')
            else:
                self.dict_videos.update({v.title:v})
    def get_all_video_title(self):
        return [(lambda x : x.title)(x) for x in self.dict_videos.values()]
    def get_videos(self,srch_str):
        srch_str = srch_str.casefold()
        all_vid = self.get_all_video_title()
        ans=list()
        for x in all_vid:
            if x.casefold().count(srch_str) > 0:
                ans.append(x)
        return ans
    def get_video(self,title):
        return self.dict_videos.get(title)
    def log_out(self,user_name):
        if user_name in self.online_user:
            self.online_user.remove(user_name)
            print(f'Пользователь {user_name} вышел из системы!')
        if user_name == self.cur_user:
            self.cur_user = self.online_user[0] if len(self.online_user) != 0 else None
        print(f'Текущий пользователь {self.dict_user[self.cur_user] if self.cur_user != None else None}')
        return self
    def register(self,name='',password='',age=0):
        if name == '':
            name = input('Введите имя пользователя:')
        if password == '':
            password = input('Введите пароль:')
        if age == 0:
            age = int(input('Введите возраст:'))
        if name in self.dict_user.keys():
            print(f'Пользователь {name} уже зарегистрирован в системе!')
        else:
            new_user = User(name,password,age)
            self.dict_user.update({new_user.nickname:new_user})
            self.online_user.append(new_user.nickname)
            self.cur_user=new_user.nickname
            print(f'Зарегистрирован новый пользователь {new_user}!')
            print(f'Текущий пользователь {self.dict_user[self.cur_user]}')
        return self
    def log_in(self,name_user,user_password):
        user = self.dict_user.get(name_user)
        if user == None:
            self.register(name,user_password)
        else:
            if hash(user_password) == user.password:
                if user.nickname not in self.online_user:
                    self.online_user.append(user.nickname)
                self.cur_user = user.nickname
                print(f'Текущий пользователь {user}')
            else:
                print(f'Для пользователя {user} введен неверный пароль')
        return self
    def print_active_user(self):
        if len(self.online_user) != 0:
            print('Сейчас смотрят видео:')
            al=list()
            n=1
            for x in self.online_user:
                print(f'{n}. {self.dict_user[x]}')
                n+=1
        else:
            print('Нет активных пользователей!')
        return self
    def print_user(self):
        if len(self.dict_user) != 0:
            print('В системе зарегистрированы:')
            al = list()
            n = 1
            for x in self.dict_user:
                print(f'{n}. {self.dict_user[x]}')
                n += 1
        else:
            print('Нет зарегистрированных пользователей!')
        return self
    def current_user(self):
        print(f'Текущий пользователь {None if self.cur_user == None else self.dict_user[self.cur_user]}')
        return self
    def change_acive_user(self,name):
        if name in self.dict_user.keys():
            if name in self.online_user:
                self.cur_user = name
                print(f'Текущий пользователь {self.dict_user[user]}')
            else:
                print(f'Пользователь {self.dict_user[user]} не вошол в систему!')
        else:
            print(f'Пользователь с именем {name} не зарегистрирован в системе!')
        return self
    def watch_video(self,title):
        if self.cur_user != None:
            vid = self.get_video(title)
            if vid != None:
                user=self.dict_user[self.cur_user]
                print(f'Текущий пользователь {user} - ',end='')
                if user.age <18 and vid.adult_mode:
                    print(f'не может просмотреть видео {vid} (Выставлено ограничение 18+)!')
                else:
                    vid.play()
            else:
                print('Ничего не найдено. :(')
        else:
            print('Нет активных пользователей! Войдите или зарегистрируйтесь!')

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
#v1.play()
#v2.play()

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_all_video_title())
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
ur.print_user().print_active_user().current_user()

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')